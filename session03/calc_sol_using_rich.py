import math

from rich.console import Console

console = Console()
"""
Exercise 2
"""
# exercise 2.1

radius = 5
volume = 4 / 3 * math.pi * radius**3
console.print(f"The volume of a sphere with radius 5 is {volume:.2f}.\n", style="bold")
# console.print()

# exercise 2.2
book_count = 60
price = 24.95
discount = 0.4
cost = price * (1 - discount) * book_count
shipping_cost_first = 3
shipping_cost_per_book = 0.75
shipping_cost = shipping_cost_first + shipping_cost_per_book * (book_count - 1)
total_cost = cost + shipping_cost
console.print(f"The total wholesale cost for {book_count} copies is ${total_cost:.2f}.")
console.print()

# exercise 2.3
# All variables use hours as unit, unless otherwise specified in their names.
start_time = 6 + 52 / 60
easy_pace = (8 + 15 / 60) / 60
tempo_pace = (7 + 12 / 60) / 60
running_time = 2 * easy_pace + 3 * tempo_pace
breakfast = start_time + running_time
breakfast_min = (breakfast - int(breakfast)) * 60
breakfast_sec = (breakfast_min - int(breakfast_min)) * 60

console.print(
    f"Breakfast time is {int(breakfast):02d}:{int(breakfast_min):02d}:{int(breakfast_sec):02d}."
)
console.print()

# exercise 2.4
percentage = (89 - 82) / 82
console.print(f"The percentage of the increase is {percentage * 100:04.1f}%.")

# or
console.print(f"The percentage of the increase is {percentage:05.1%}.")

console.print()
