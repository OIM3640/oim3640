import turtle

from turtle_shape import arc, circle, move, polygon, square

# 3.3


def star(t, length=200):
    """Draws a star"""
    for i in range(5):
        t.forward(length)
        t.right(144)


def spiral_stars(t):
    """Draws a spiral of stars"""
    for i in range(60):
        length = 50 + 4 * i
        star(t, length)
        t.right(5)


def draw_shape(t):
    """Draws the final graphics"""
    spiral_stars(t)


def main():
    t = turtle.Turtle()
    t.speed(0)

    draw_shape(t)
    turtle.Screen().mainloop()


if __name__ == "__main__":
    main()
