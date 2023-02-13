# http://www.python-course.eu/towers_of_hanoi.php


def move(n, source, bridge, destination):
    """
    Use recursion to solve tower of Hanoi problem.
    """
    if n == 1:
        print(f"{source} --> {destination}")
    else:
        # move n-1 plates from origin to bridge
        move(n - 1, source, destination, bridge)
        # move the largest plate from origin to destination
        print(f"{source} --> {destination}")
        # move n-1 plates from bridge to destination
        move(n - 1, bridge, source, destination)


def main():
    move(6, "A", "B", "C")


if __name__ == "__main__":
    main()
