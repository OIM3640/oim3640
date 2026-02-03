# How many seconds are there in 42 minutes 42 seconds?

print(42 * 60 + 42)

# How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.

print(10 / 1.61)

# If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace in seconds per mile?

print((42 * 60 + 42) / (10 / 1.61))

# What is your average pace in minutes and seconds per mile?

print((42 * 60 + 42) // (10 / 1.61) // 60, (42 * 60 + 42) // (10 / 1.61) % 60)

# What is your average speed in miles per hour?

print((10 / 1.61) / ((42 * 60 + 42) / 3600))
