# print("39 + 41 + 33")

# print(2024 - 2020)

# print(15 / 3)

# print(16 // 3)


"""
Ex. 2.1
"""
minutes = 42
seconds = 42

print(minutes * 60 + seconds)

print(f"The time duration is {minutes * 60 + seconds} seconds.")
print()

"""
Ex. 2.2
"""
km_per_mile = 1.61
km = 10
miles = km / km_per_mile

print(miles)

print(f"There are {miles} miles in {km} kilometers.")
print()

"""
Ex. 2.3
"""
minutes = 42 + 42 / 60
hours = minutes / 60

km_per_mile = 1.61
km = 10
miles = km / km_per_mile

pace = minutes / miles
mph = miles / hours

print("Pace in minutes per mile:", pace)
print("Average speed in mph:", mph)
