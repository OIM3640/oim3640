import weather
from flask import Flask, render_template, request

app = Flask(__name__)


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
def weather(city=None):
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
404
"""


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return render_template("404.html")


"""
Course Registration Example
"""
STUDENTS = {}  # registration information, e.g. {'Zhi': 'Python'}


@app.get("/register")
def show_registeration_form():
    """Show the registration form."""
    return render_template("register-form.html")


@app.post("/register")
def register_course():
    """Register a student for a course."""
    name = request.form.get("fullname")
    course = request.form.get("course")
    STUDENTS[name] = course
    return "Successfully registered!"


@app.route("/enrollments")
def show_enrollments():
    """Show all the enrollments"""
    return render_template("enrollments.html", students=STUDENTS)


if __name__ == "__main__":
    app.run(debug=True)
