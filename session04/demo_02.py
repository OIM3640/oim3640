# print('I\'m \"ok\"!')
# print('I\'m \tlearning\nPython!')

# print('\\\t\\')
# print(r'\\\t\\')

# print('''Hi,
# I am learning
# Python''')

# """
# Multiline comments
# Another line
# """


# age = 22 # modify the code to ask user for age 
age = int(input('How old are you? '))
# age = int(age)

country = input('Which country are you in? ')

# if user is older than 21, or he/she is not in US
if age >= 21 or country != 'US':
    print('Yes, you can.')
else:
    print('Sorry, you cannot.')