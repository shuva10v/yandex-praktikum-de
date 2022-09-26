#!/usr/bin/env python
import requests
import pandas as pd
from tabulate import tabulate

def fetch():
	status = requests.get("https://www.githubstatus.com/api/v2/summary.json").json()['components']
	df = pd.DataFrame(status)[['name', 'status']]
	print(tabulate(df, headers='keys', tablefmt='fancy_grid'))

if __name__ == "__main__":
	fetch()

	
	
