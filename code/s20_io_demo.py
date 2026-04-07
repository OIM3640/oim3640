# Read entire file
# with open("data/s20.txt", "r") as f:
#     # text = f.read()
#     # text = f.readline()
#     text = f.readlines()

#     print(text)

# Read line by line (best for large files)
# with open("data/s20.txt", "r") as f:
#     for line in f:
#         print(line.strip())  # strip() removes \n

# Write to file ('w' = overwrite, 'a' = append)
with open("data/s20_output.txt", "a") as f:
    f.write('Hello, World!\n')
