"""
Reading text file
"""

# file = open('data/hey_jude.txt')

# print(file.read())
# print(type(file.read()))

# print(file.readline())
# print(file.readline())

# print(file.readlines())
# print(type(file.readlines()))


"""
Writing data into a file
"""

# file = open("data/output.txt", "w")
# file.write("How many roads must a man walk down\n")

# file.write("Before we call him a man\n")

# lyrics = ["How many roads must a man walk down\n", 'Before we call him a man\n']
# file.writelines(lyrics)

# file.close()

"""
Context manager
"""
# with open("data/output.txt", 'w') as file:
#     lyrics = ["How many roads must a man walk down\n", 'Before we call him a man\n']
#     file.writelines(lyrics)

"""
os module
"""
import os

cwd = os.getcwd()
# print(cwd)

# print(os.path.abspath('data/output.txt'))
# print(os.path.exists('data'))
# print(os.path.exists('dataset'))

# try:
#     file = open("dataset/output.txt")
# except FileNotFoundError:
#     print("File not found. Now making a new folder")


# print(os.listdir(cwd))

"""
Pickling
"""
import pickle

t = ["1", 2, 3]

with open("data/t.pkl", "wb") as file:
    pickle.dump(t, file)
