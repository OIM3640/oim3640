import turtle

from turtle_shape import arc, circle, move, polygon, square

# 3.1


def square_circle(t):
    """Draws a circle of squares"""
    for i in range(60):
        square(t, 200)
        t.right(5)


def draw_shape(t):
    """Draws the final graphics"""
    square_circle(t)


def main():
    t = turtle.Turtle()
    t.speed(0)

    draw_shape(t)
    turtle.Screen().mainloop()


if __name__ == "__main__":
    main()
