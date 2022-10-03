file = open("wolverine.txt")
print(file.tell())
print(file.readline())
print(file.tell())   # to know the current location of the file pointer
print(file.readline())
print(file.tell())
file.seek(0)    # for resetting the fiel pointer to mentioned position
print(file.tell())
print(file.readline())
print(file.tell())

file.close()
