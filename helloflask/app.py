from flask import Flask

app = Flask(__name__)


# If the website domain is www.xyz.com, https://www.xyz.com/ or https://www.xyz.com/hello will trigger this function
@app.route("/")
@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    if name is not None:
        return f"Hello, {name}!"
    return "Hello, world!"


# Create another route like "/square/<number>", so the web app will display the square of the integer
@app.route("/square/")
# @app.route("/square/<number>")
@app.route("/square/<int:number>")
def square(number=None):
    if number is not None:
        return f"{number} ^ 2 = {number ** 2}"
    return "You should prove a number after"


if __name__ == "__main__":
    app.run(debug=True)
