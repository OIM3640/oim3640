from flask import Flask, redirect, render_template, request
from weather import get_temp

app = Flask(__name__)


# If the website domain is www.xyz.com, https://www.xyz.com/ or https://www.xyz.com/hello will trigger this function
@app.route("/")
@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    if name is not None:
        return render_template("index.html", username=name)
    return render_template("index.html", username="guest")


# Create another route like "/square/<number>", so the web app will display the square of the integer
@app.route("/square/")
# @app.route("/square/<number>")
@app.route("/square/<int:number>")
def square(number=None):
    if number is not None:
        return f"{number} ^ 2 = {number ** 2}"
    return "You should prove a number after"


"""
Weather API + Form
"""


@app.get("/temp/")
def temp_get():
    return render_template("weather-form.html")


@app.post("/temp/")
def temp_post():
    city_name = request.form["city"]
    temperature = get_temp(city_name)
    return render_template("weather-result.html", city=city_name, temp=temperature)


"""
404
"""


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


"""
Course Registration
"""
STUDENTS = {}  # name: course
COURSES = ["Python", "Web", "Blockchain", "UIUX"]


@app.get("/register/")
def get_register():
    return render_template("register-form.html", courses=COURSES)


@app.post("/register/")
def post_register():
    name = request.form.get("fullname")
    course = request.form.get("course")
    if course not in COURSES:
        return "Get out of here, Moises/hacker!"
    STUDENTS[name] = course
    return redirect("/students/")


@app.route("/students/")
def show_students():
    return render_template("students.html", students=STUDENTS)


if __name__ == "__main__":
    app.run(debug=True)
