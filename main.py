import asyncio
import scraper
import loader
import graph

async def main():
	codes = loader.load_input()
	products = await scraper.get_products(codes)

	loader.save_output(products)
	graph.show()

asyncio.get_event_loop().run_until_complete(main())
