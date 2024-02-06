import turtle

from turtle_shape import arc, circle, move, polygon, square

# 3.2


def spiral_squares(t):
    """Draws a spiral of squares"""
    for i in range(60):
        length = 30 + 4 * i
        square(t, length)
        t.right(5)


def draw_shape(t):
    """Draws the final graphics"""
    spiral_squares(t)


def main():
    t = turtle.Turtle()
    t.speed(0)

    draw_shape(t)
    turtle.Screen().mainloop()


if __name__ == "__main__":
    main()
