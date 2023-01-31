# Exercise 4

a = input("Please enter number 1: >>> ")
b = input("Please enter number 2: >>> ")  # No validation yet

a = float(a)
b = float(b)


print(f'{a} + {b} = {a + b: 8.3f}')
print(f'{a} - {b} = {a - b: 8.3f}')
print(f'{a} * {b} = {a * b: 8.3f}')
print(f'{a} / {b} = {a / b: 8.3f}')
print(f'{a} ^ {b} = {a **b: 8.3f}')
print()


# Advanced solution

print('Advanced Solution:')
import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    # '//': operator.floordiv,
    '^': operator.pow,
}

max_int = max(len(str(int(ops[op](a, b)))) for op in ops)
print(max_int)

for op in ops:
    print(f'{a} {op} {b} = {ops[op](a, b):>{max_int+4}.3f}')
