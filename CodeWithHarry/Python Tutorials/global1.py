# l = 11   # Global Variable
# z = 41   # Global Variable
# def func1(a):
#     # l = 9  # Local Variable
#     k = 18  # Local Variable
#     global z    # This gives the permission to function to change the global variable z
#     z = z+32 ## ERROR
#     print(k, l, a,"this one")
# func1("thsi")
# print(l)
# # print(k)   # ERROR
k = 88
def func1():
    k = 11
    def func2():
        global k
        k =32
    print("before calling func2()",k)
    func2()
    print("after calling func2()",k)

func1()
print(k)