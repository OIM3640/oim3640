# Exercise 4

a = input("Please enter number 1: >>> ")
b = input("Please enter number 2: >>> ")  # No validation yet

a = int(a)
b = int(b)


print(f"{a} + {b} = {a + b: 5d}")
print(f"{a} - {b} = {a - b: 5d}")
print(f"{a} * {b} = {a * b: 5d}")
print(f"{a} / {b} = {a / b: 5.2f}")
print(f"{a} ^ {b} = {a ** b: 5d}")
print()


# Advanced solution

print("Advanced Solution:")
import operator

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    # '//': operator.floordiv,
    "^": operator.pow,
}

max_res_len = (
    max(len(str(int(ops[op](a, b)))) for op in ops) + len(str(a)) + len(str(b)) + 1
)

# print(max_int)

for op in ops:
    print(f"{a} {op} {b} = {ops[op](a, b):{max_res_len}.2f}")
