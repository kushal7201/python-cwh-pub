# f = open("wolverine.txt", "r") # default mode
# content = f.read()
# print(content)
# f.close()
# f = open("wolverine.txt", "rt") # default mode
# content = f.read()
# print(content)
# f.close()
# f = open("wolverine.txt", "rb")
# content = f.read()
# print(content)
# f.close()

# f = open("wolverine.txt", "r") # default mode
# content = f.read(19991)
# for line in content:
#     print(line)
# content12 = f.read(19991)
# print(2, content12)

# f.close()

# f = open("Wolverine.txt", "r") # default mode
# # content = f.read()
# # print(content)
# for line in f:
#     print(line, end="")
# f.close()


# f = open("wolverine.txt", "r") # default mode
# content = f.read()
# print(content)
# f.close()

f = open("Wolverine.txt", "rt")
# print(f.readline())
# print(f.readline())
# print(f.readline())
print(f.readlines())