import csv


def write_data_to_csv(data, file_path):
    """"""
    with open(file_path, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Ticker", "Shares", "Price"])
        for row in data:
            csv_writer.writerow(row)


def read_data_from_csv(file_path):
    """"""
    with open(file_path, "r", newline="") as csv_file:
        csv_reader = csv.reader(csv_file)
        # skip the header row
        next(csv_reader)
        stocks = []
        for row in csv_reader:
            stocks.append([row[0], int(row[1]), float(row[2])])
        return stocks


def find_expensive_stock(threshold_price, file_path):
    with open(file_path, "r", newline="") as csv_file:
        csv_reader = csv.reader(csv_file)
        # skip the header row
        next(csv_reader)
        stocks = []
        for row in csv_reader:
            price = float(row[2])
            if price >= threshold_price:
                stocks.append([row[0], int(row[1]), float(row[2])])
        return stocks


def main():
    # Check out Yahoo Finance API/Python lib
    stocks = [
        ["AAPL", 100, 223.78],
        ["NVDA", 50, 145.33],
        ["GOOG", 200, 181.71],
    ]
    file_path = "data/stocks.csv"
    # write_data_to_csv(stocks, file_path)
    data = read_data_from_csv(file_path)
    print(data)

    expensive_stocks = find_expensive_stock(150, file_path)
    print(expensive_stocks)

    write_data_to_csv(expensive_stocks, "data/expensive_stocks.csv")


main()
