

import os
import json
from pprint import pprint

from dotenv import load_dotenv
import requests
from plotly.express import line
from statistics import mean
load_dotenv()

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

request_url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={API_KEY}"

response = requests.get(request_url)

parsed_response = json.loads(response.text)
print(type(parsed_response))
pprint(parsed_response)

#breakpoint()


data = parsed_response["data"]


# Challenge A
#
#Latest unemployment rate

print("-------------------------")
print("Latest unemployment rate:")
#print(data[0])
print(f"{data[0]['value']}%", "as of", data[0]["date"])

this_year = [d for d in data if "2022-" in d["date"]]

rates_this_year = [float(d["value"]) for d in this_year]
#print(rates_this_year)

print("-------------------------")
print("AVG UNEMPLOYMENT THIS YEAR:", f"{mean(rates_this_year)}%")
print("NO MONTHS:", len(this_year))
breakpoint()

