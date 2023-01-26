# print('I\'m \"ok\".')
# print('I\'m \tlearning\nPython.')
# print('\\\t\\')
# print(r'\\\t\\')

# print('''Hi,
# I am learning
# Python.''')

# age = 22 # modify this to ask user for their age
age = int(input("How old are you? >> "))
country = input("Which country are you in?")

# if you are older than 21, or you are not in USA
if age >= 21 or country.lower() not in ['usa', 'us', 'united states']:
    print('Yes, you can.')
else:
    print('Sorry, you cannot.')
