"""
list
"""

stocks = ["AAPL", "MSFT", "NVDA"]
print(stocks[0])

"""
tuple
"""
stock = ("AAPL", 231.46, 20)
print(stock[1])

"""
dict
"""
portfolio = {
    "AAPL": {"price": 230.43, "shares": 10},
    "MSFT": {"price": 416.29, "shares": 20},
}
print(portfolio["MSFT"]["shares"])

"""
class
"""
class Stock:
    def __init__(self, ticker, current_price, shares):
        pass

    def buy(self, shares):
        self.shares += shares


class Portfolio:
    def __init__(self, owner, stocks=None):
        self.owern = owner
        if stocks is None:
            self.stocks = []
        else:
            self.stocks = stocks


stock = Stock("MSFT", 200, 20)
print(stock)  # We need to define __str__

"""
namedtuple
"""
from collections import namedtuple

Stock = namedtuple("Stock", ["symbol", "price", "shares"])
my_stock = Stock(symbol="AAPL", price=230, shares=10)
print(my_stock.price)

"""
dataclass
"""
from dataclasses import dataclass


@dataclass
class Stock:
    symbol: str = "N/A"
    price: float = 0
    shares: int = 0


# create an object of Stock
stock = Stock(symbol="AAPL", price=230, shares=10)
print(stock)
stock.shares += 5
print(stock.shares)

another_stock = Stock(symbol="Some stock")
print(another_stock)
