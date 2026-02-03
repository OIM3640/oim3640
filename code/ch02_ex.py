# Part 1


import math

radius = 5  # in centimeters
volume = (4 / 3) * math.pi * radius**3  # in cubic centimeters
print(volume)

# Use f-strings for formatted output
print(f"The volume of a sphere with radius {radius} is {volume:.2f} cubic centimeters.")


# Part 2

x = 42
result = math.cos(x) ** 2 + math.sin(x) ** 2
print(result)
print(f"The result of cos^2(42) + sin^2(42) is {result:.2f}.")


from rich.console import Console

console = Console()
console.print(f"The result of cos^2(42) + sin^2(42) is {result:.2f}.", style="red")


# Part 3

print(math.e**2)
print(math.pow(math.e, 2))
print(math.exp(2))
