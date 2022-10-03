# f = open("wolverine.txt")
# f.close()   # These two lines are handled in the "with" "as" syntax, normally as we write in between these lines

with open("wolverine.txt") as k:
    a = k.read(11)
    print(a)

# YES: Because eith block automatically close the file after we come out from it.

f = open("wolverine.txt")
print(f.readlines())
f.close()