import turtle

from turtle_shape import square


def spiral(t, n):
    """
    Ask user to enter the initial length,
    draw a spiral shape - that is drawing a square multiple times,
    after one square, turn 5 degrees

    t: a turtle
    n: int, number of squares to draw for the spiral
    """
    # Pseudocode
    # 1. Ask the user to enter the initial length of the square's side and store it in a variable.
    # 2. Convert the variable to an integer.
    # 3. Repeat the following task/steps repeat n times:
    #    a. Draw a square with the current length.
    #    b. Turn the turtle right by 5 degrees.

    length = input("Enter the length of square's side: ")
    length = int(length)
    for i in range(n):
        square(t, length)
        t.right(5)


def main():
    turtle.speed(0)

    leo = turtle.Turtle()
    spiral(leo, 10)
    turtle.mainloop()


if __name__ == "__main__":
    main()
