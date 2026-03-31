import yfinance as yf
from pprint import pprint # TODO: pprint will print a dictionary in a more readable format (after sorting?)

tickers = ['AAPL', 'NVDA', 'MSFT', 'META', 'GOOG']
stocks = {} 

for t in tickers:
    stocks[t] = yf.Ticker(t).info['currentPrice'] # create a dictionary with the current price of each stock

print(stocks)

print('After sorting ...')

# def sort_by_price(t):
#     return t[1] # sort by the second item in the tuple (the price)


# print(sorted(stocks.items(), key=sort_by_price))
print(sorted(stocks.items(), key=lambda t: t[1], reverse=True)) # same as above, but using a lambda function instead of defining a separate function