# Exercise 3

import time


print(time.time())

current = time.time()
seconds = current % 60
minutes = current // 60 % 60
hours = current // 60 // 60 % 24
days = current // 60 // 60 // 24

# print(seconds, minutes, hours, days)

print(
    f"Current time: {int(days):d} days, {int(hours):d} hours, {int(minutes):d} minutes and {seconds:.2f} seconds from Epoch."
)
