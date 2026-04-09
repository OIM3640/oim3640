import yfinance as yf

def get_price(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    return info['currentPrice']

if __name__ == "__main__":
    print(get_price('AAPL'))