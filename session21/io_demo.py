import os

# file = open("data/pride and prejudice.txt", "r", encoding="utf-8")
# print(file.read())
# print(file.readline())
#
# print(len(file.readlines()))


def write_data():
    # context manager, a better way to handle io
    with open("data/output.txt", "a", encoding="utf-8") as file:
        # file.write("Hey Jude\n")
        # file.write("Don't make it bad\n")
        lyrics = [
            "Hey Jude\n",
            "Don't make it bad\n",
            "Take a sad songs\n",
            "And make it better",
        ]
        file.writelines(lyrics)


def read_data():
    with open("data/output.txt", "r", encoding="utf8") as file:
        print(file.read())


def os_example():
    cwd = os.getcwd()  # the current working directory
    # print(cwd)
    print(os.path.isdir("data"))
    print(os.path.isdir("data/output.txt"))
    data_list = os.listdir("data")
    for data_file in data_list:
        if data_file.endswith(".csv"):
            pass  # process the csv files


def main():
    # write_data()
    # read_data()
    os_example()


main()
