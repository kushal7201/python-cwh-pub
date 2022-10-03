try:
    a = int(input("Enter 1st: "))
    b = int(input("Enter 2nd: "))
    c = int(input("Enter 3rd: "))
    """This is a function which will calculate the average of numbers.
    It works only for three inputs in float"""
    print((a+b+c)/3)

except Exception as i:
    print(i)

print("You know! this line is very important")