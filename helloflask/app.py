from flask import Flask, render_template
from stocks import get_price

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Babson! Let's build some web applications!"


@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    if name is None:
        name = "World"
    name = name.capitalize()
    return render_template("hello.html", name=name)


@app.route("/square/<int:number>")
def square(number):
    result = number ** 2    
    # return f"The square of {number} is {number**2}."
    return render_template("square.html", number=number, square=result)


# create another route that shows the current price of any stock or current temperature of any city
# /weather/<city>
# /stock/<ticker>

@app.route("/stock/<ticker>")
def stock(ticker):
    price = get_price(ticker)
    return f"The current price of {ticker.upper()} is ${price:.2f}."
    # return render_template("stock.html", ticker=ticker.upper(), price=price)


if __name__ == "__main__":
    app.run(debug=True)
