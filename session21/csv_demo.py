import csv

stocks = [
    ["AAPL", 100, 200],  # stock, shares, price
    ["NVDA", 50, 500],
    ["META", 200, 100],
]


# Write data to a csv file
# with open("data/stocks.csv", "w", newline="") as csv_file:
#     csv_writer = csv.writer(csv_file)
#     csv_writer.writerow(['Ticker', 'Shares', 'Price'])
#     for row in stocks:
#         csv_writer.writerow(row)


# Read data from a csv file
with open("data/stocks.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    # Skip the header row
    next(csv_reader)

    # calculate the total cost of all the stocks
    total = 0
    for row in csv_reader:
        shares= int(row[1])
        price = float(row[2])
        total += shares * price
    print(total)
