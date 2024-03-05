# data = {
#     "time": {
#         "updated": "Mar 5, 2024 20:59:33 UTC",
#         "updatedISO": "2024-03-05T20:59:33+00:00",
#         "updateduk": "Mar 5, 2024 at 20:59 GMT",
#     },
#     "disclaimer": "This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org",
#     "chartName": "Bitcoin",
#     "bpi": {
#         "USD": {
#             "code": "USD",
#             "symbol": "&#36;",
#             "rate": "61,876.874",
#             "description": "United States Dollar",
#             "rate_float": 61876.8744,
#         },
#         "GBP": {
#             "code": "GBP",
#             "symbol": "&pound;",
#             "rate": "48,713.683",
#             "description": "British Pound Sterling",
#             "rate_float": 48713.6832,
#         },
#         "EUR": {
#             "code": "EUR",
#             "symbol": "&euro;",
#             "rate": "57,014.404",
#             "description": "Euro",
#             "rate_float": 57014.404,
#         },
#     },
# }


# print(type(data))
# print(len(data))
# print(data.keys())
import urllib.request
import json
import pprint

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

with urllib.request.urlopen(url) as f:
    response_text = f.read().decode("utf-8")
    data = json.loads(response_text)

bitcoin_usd = data["bpi"]["USD"]["rate_float"]
print(bitcoin_usd)
