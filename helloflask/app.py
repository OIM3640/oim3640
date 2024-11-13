import os
from dotenv import load_dotenv
import weather
from flask import Flask, redirect, render_template, request

app = Flask(__name__)


load_dotenv()


# Root URL ('/') displays the homepage message.
# Example: Visiting http://www.xyz.com/ will trigger this function.
@app.route("/")
def index():
    """Returns the homepage message."""
    return "This is the homepage. I am excited to learn Flask."


# URL '/hello' displays a generic greeting. URL '/hello/<name>' displays a personalized greeting.
# Example: Visiting http://www.xyz.com/hello/Andrew will trigger this function with 'Andrew' as the name.
@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    """Returns a generic or personalized greeting."""
    if name is not None:
        # return f'<h1 style="color:red">Hello, {name}!</h1><p style="color:blue">I am also excited to learn Flask.</p>'
        return render_template("hello.html", username=name)
    return "Hello world!"


"""
Task: Create a new route /square/<number> that calculates and displays the square of <number> when the user visits this URL. If <number> is not provided or is invalid, display an appropriate message.
"""


# Example: Visiting http://www.xyz.com/square/3 will return '9.0'.
@app.route("/square")
@app.route("/square/<number>")
def square(number=None):
    """Returns the square of the given number."""
    if number is not None:
        try:
            return str(float(number) ** 2)
        except ValueError as e:
            print(e)
            return "Invalid input. Please provide a valid number after /square/"
    return "You need to provide a number."


# Task: Create a route that returns weather information for a specific location.
# Example: '/weather/Wellesley' could return current weather details for Wellesley.


"""
Weather API + Form
"""


@app.route("/weather/<city>")
def show_weather(city=None):
    """Returns the current temperature in the given city."""
    temp = weather.get_temp(city)
    return f"{temp}°C"


@app.get("/weather")
def get_weather():
    """Displays a form for the user to input a city name."""
    return render_template("weather-form.html")


@app.post("/weather")
def post_weather():
    """Displays the current temperature in the city provided by the user after submitting the form."""
    city_name = request.form["city"]
    result = weather.get_temp(city_name)
    return render_template("weather-result.html", temp=result, city=city_name.title())


"""
Course Registration Example
"""
STUDENTS = {}  # registration information, e.g. {'Zhi': 'Python'}
COURSES = ["Excel", "Web", "Tax", "AI"]


@app.get("/register/")
def show_registeration_form():
    """Show the registration form."""
    return render_template("register-form.html", courses=COURSES)


@app.post("/register/")
def register_course():
    """Register a student for a course."""
    # Validate
    name = request.form.get("fullname")
    course = request.form.get("course")
    if course not in COURSES:
        return "Get out of here, hacker!"
    STUDENTS[name] = course
    # return "Successfully registered!"
    # return render_template("enrollments.html", students=STUDENTS)
    return redirect("/enrollments/")


@app.route("/enrollments/")
def show_enrollments():
    """Show all the enrollments"""
    return render_template("enrollments.html", students=STUDENTS)


"""
404
"""


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return render_template("404.html")


"""
After MBTA project
"""


@app.route("/map/")
def show_map():
    MAPBOX_ACCESS_TOKEN = os.getenv("MAPBOX_ACCESS_TOKEN")

    lat, lng = 42.298022697548475, -71.26653426988861

    zoom = 16
    width = 600
    height = 400

    mapbox_url = f"https://api.mapbox.com/styles/v1/mapbox/streets-v12/static/{lng},{lat},{zoom}/{width}x{height}?access_token={MAPBOX_ACCESS_TOKEN}"

    return (
        f'<img src="{mapbox_url}" width="{width}" height="{height}" alt="Mapbox Map">'
    )


if __name__ == "__main__":
    app.run(debug=True)
