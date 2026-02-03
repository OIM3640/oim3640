# a product would cost $100, how much tax do we pay?


# product = 100 # in dollars
# tax_rate = 0.0625
# tax = product * tax_rate
# print(f'The tax for a product which costs ${product} is ${tax}.') # f-string


def calc_tax(price, tax_rate):
    """Calculate product tax based on given price and tax rate, and return the tax amount."""
    tax = price * tax_rate
    # print(f'The tax for a product which costs ${price} is ${tax}.')
    # print(tax)
    # if the function does not explicitly return any value, it would return None
    return tax


computer_price = float(input('Enter the product price: '))
iphone_price = 1100
mass_rate = 0.0625
ny_rate = 8.875 / 100
tax_computer = calc_tax(computer_price, mass_rate)
tax_iphone = calc_tax(iphone_price, ny_rate)

total_tax = tax_computer + tax_iphone
print(total_tax)
