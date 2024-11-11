import sqlite3


def create_portfolio_table():
    """Create a table to store stock portfolio data."""
    with sqlite3.connect("data/stocks.db") as db:
        cursor = db.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS portfolio (
                symbol TEXT,
                shares INTEGER,
                price REAL
            )
            """
        )


def insert_stocks(stocks):
    """Insert multiple stocks into the portfolio table."""
    with sqlite3.connect("data/stocks.db") as db:
        cursor = db.cursor()
        cursor.executemany("INSERT INTO portfolio VALUES (?,?,?)", stocks)


def display_portfolio():
    """Display all the stocks in the portfolio table."""
    with sqlite3.connect("data/stocks.db") as db:
        cursor = db.cursor()
        for row in cursor.execute("SELECT * FROM portfolio"):
            print(row)


def display_expensive_stocks(threshold_price):
    """Display stocks with price greater than a given value."""
    with sqlite3.connect("data/stocks.db") as db:
        cursor = db.cursor()
        results = cursor.execute(
            "SELECT * FROM portfolio WHERE price > ?", (threshold_price,)
        )
        for row in results:
            print(row)


def main():
    """"""
    create_portfolio_table()

    stocks = [
        ["AAPL", 100, 223.78],
        ["NVDA", 50, 145.33],
        ["GOOG", 200, 181.71],
    ]
    insert_stocks(stocks)

    display_portfolio()

    print("\nExpensive Stocks:")
    min_price = 150
    display_expensive_stocks(min_price)


if __name__ == "__main__":
    main()
