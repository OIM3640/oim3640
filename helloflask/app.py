from flask import Flask, render_template, request

from weather import get_temp

app = Flask(__name__)


# If the website domain is www.xyz.com, https://www.xyz.com/ or https://www.xyz.com/hello will trigger this function
@app.route("/")
@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    if name is not None:
        return render_template("index.html", username=name)
    return "Hello, world!"


# Create another route like "/square/<number>", so the web app will display the square of the integer
@app.route("/square/")
# @app.route("/square/<number>")
@app.route("/square/<int:number>")
def square(number=None):
    if number is not None:
        return f"{number} ^ 2 = {number ** 2}"
    return "You should prove a number after"


@app.get("/temp/")
def temp_get():
    return render_template("weather-form.html")


@app.post("/temp/")
def temp_post():
    city_name = request.form["city"]
    temperature = get_temp(city_name)
    return render_template("weather-result.html", city=city_name, temp=temperature)


if __name__ == "__main__":
    app.run(debug=True)
