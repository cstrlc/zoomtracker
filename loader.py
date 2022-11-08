import csv
import pandas as pd

def load_input():
	codes = []

	with open('input.csv', newline='') as csvfile:
		codes = csv.reader(csvfile, delimiter=',')
		codes = [item.strip() for sublist in codes for item in sublist]
		codes = list(filter(bool, codes))

	return codes

def save_output(objs):
	df = pd.read_csv("output.csv")
	df = pd.concat([df, pd.DataFrame(objs)]).sort_values(by=["name"]).drop_duplicates()

	df.to_csv("output.csv", index=False)
