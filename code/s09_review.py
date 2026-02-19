# score = int(input("Enter your score: "))

# if score >= 60:
#     print("Congratulations! You passed the exam.")
# elif score >= 90:
#     print("Excellent work! You scored an A.")
# else:
#     print("Unfortunately, you did not pass. Better luck next time.")

# if score >= 90:
#     print("Excellent work! You scored an A.")
# if score >= 60:
#     print("Congratulations! You passed the exam.")
# else:
#     print("Unfortunately, you did not pass. Better luck next time.")


def evaluate_score(score):
    if score >= 60:
        return "Congratulations! You passed the exam."
    if score >= 90:
        return "Excellent work! You scored an A."
    else:
        return "Unfortunately, you did not pass. Better luck next time."


# score = int(input("Enter your score: "))
# result = evaluate_score(score)
# print(result)


def mystery(x):
    if x > 0:
        print("done")
        return "positive"
    else:
        print("done")
        return "non-positive"
    # print("done")


# result = mystery(0)
# print(result)

# x = 15
# y = x > 10 or x < 2
# print(type(y))
# print(y)


def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False


# Test cases
# print(is_leap_year(2026))  # True
# print(is_leap_year(2027))  # True
# # print(is_leap_year(2023))  # False
# # print(is_leap_year(1900))  # False
# # print(is_leap_year(2000))  # True

# how to find the next leap year after a given year?


def check(n):
    if n % 2 == 0:
        if n % 3 == 0:
            print(f"{n} is divisible by both 2 and 3")
        else:
            print(f"{n} is divisible by 2 but not by 3")
    else:
        print(f"{n} is not divisible by 2")


# check(8)
# check(6)


def check(n):
    if n % 2 == 0 and n % 3 == 0:
        print(f"{n} is divisible by both 2 and 3")
    elif n % 2 == 0:
        print(f"{n} is divisible by 2 but not by 3")
    else:
        print(f"{n} is not divisible by 2")


check(8)
check(6)
