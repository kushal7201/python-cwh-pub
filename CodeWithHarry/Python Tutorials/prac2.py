
# def read_file():
#     """"This function prints the content in poem.txt line by line"""
#     k = open("poem.txt")
#     for line in k:
#         print(line, end="")
#     k.close()
# read_file()
# print()
# print(read_file.__doc__)

# def read_line():
#     with open("poem.txt") as k:
#         for i in k:
#             print(i, end="")
# read_line()

with open("exharry.txt") as k:
    for line in k:
        print(line, end ="")