import sys
import re
import pyppeteer
import datetime

async def get_product_url(page, code):
	await page.goto(f'https://www.zoom.com.br/search?q={code}', waitUntil='load')
	url = await page.evaluate('''document.querySelector('div[data-testid="product-card"] > a').getAttribute('href')''')

	if not url or url.startswith('http'):
		print("Could not find product with code: " + code)
		sys.exit(1)

	return f'https://www.zoom.com.br{url}'

async def get_product_info(page, url):
	await page.goto(url, waitUntil='load')

	name = str(await page.evaluate('''document.querySelector('div[data-testid="OverviewComponent"] h1').innerHTML'''))
	currency = await page.evaluate('''document.querySelector('div[class^="Price_ValueContainer"] strong').innerHTML''')
	price = float(re.sub(r'[^\d.]', '', currency.replace('.', '').replace(',', '.')))

	if not name or not price:
		sys.exit(1)

	return {"name": name, "url": url, "date": datetime.date.today().isoformat(), "price": price, }

async def get_products(codes):
	browser = await pyppeteer.launch()
	page = await browser.newPage()

	obj_list = []

	for code in codes:
		url = await get_product_url(page, code)
		obj = await get_product_info(page, url)
		obj_list.append(obj)

	await browser.close()
	return obj_list
