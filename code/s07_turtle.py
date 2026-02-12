import turtle


def draw_square(turtle_obj, size=100):
    """Draw a square with the given length of side."""
    for _ in range(4):
        turtle_obj.forward(size)
        turtle_obj.left(90)



def draw_spiral(t):
    """
    draw one square, turn a angle, then drawn another square and so on
    """
    for i in range(72):
        draw_square(t, 50 + i * 2)
        t.left(5)


def main():
    t = turtle.Turtle()
    t.speed(0)
    # draw_square(t)
    # draw_square(t, size=50)
    draw_spiral(t)
    turtle.mainloop()


if __name__ == "__main__":
    main()
