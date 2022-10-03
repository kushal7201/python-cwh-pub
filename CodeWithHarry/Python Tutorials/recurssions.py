# def factorial_iterative(num):
#     """This function calculates factorial through iterative method"""
#     factorial = 1
#     for i in range(num):
#         factorial*=i+1
#     return factorial

# print("Factorial using Iterative Method: ",factorial_iterative(20))

# def factorial_recursive(num):
#     """This function calculates factorial through recursive method"""
#     if num==1 or num==0:
#         return 1
#     else:
#         return num*factorial_recursive(num-1)
#     # 5 * factorial_recursive(4)
#     # 5 * 4 * factorial_recursive(3)
#     # 5 * 4 * 3 * factorial_recursive(2)
#     # 5 * 4 * 3 * 2 * factorial_recursive(1)
#     # 5 * 4 * 3 * 2 * 1 = 120

# print("Factorial using Recursive Method: ",factorial_recursive(20))

def fibonacci(num):
    if num==0:
        return "None"
    elif num==1:
        return 0
    elif num==2:
        return 1
    else:
        return fibonacci(num-2)+fibonacci(num-1)

print(fibonacci(21))