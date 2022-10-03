# def range(l,num,h):
#     return l<=num<=h
# print(range(402,4023,7260))
# import re
# string = input("Enter the string: ")
# k= re.findall("[A-Z]",string)
# print(len(k))

# k =float(input("Enter a real number: "))
# if k>0:
#     print("The number is positive")
# elif k<0:
#     print("The number is negative")
# else:
#     print("The number is zero")

# Collatz Conjecure:
# n= int(input("Enter a natural number: "))
# def collatz(n):
#     if n%2==0:
#         return int(n/2)
#     else:
#         return int(3*n+1)

# print(collatz(n))

# def f1(n):
#     if n%3==0 or n<5:
#         return 2*n
#     elif n%3!=0 and n>10:
#         return 3*n
#     else:
#         return n

# print(f1(6))

# def is_leap_yr():
#     n=int(input("Enter a natural number: "))
#     if n%100==0 and n%400==0:
#         return "It is leap year"
#     elif n%100==0 and n%400!=0:
#         return "It is not a leap year"
#     elif n%100!=0 and n%4==0:
#         return "It is leap year"
#     else:
#         return "It is not a leap year"
# print(is_leap_yr())

# def is_leap_yr():
#     n=int(input("Enter a natural number: "))
#     if n%100==0:
#         if n%400==0:
#             return "It is leap year"
#         else:
#             return "It is not a leap year"
#     elif n%4==0:
#         return "It is leap year"
#     else:
#         return "It is not a leap year"

# print(is_leap_yr())


# # Assignment Q1:
# def fxn(n):
#     k= int(n**0.5)
#     if n%3==0 or n<10 or k**2==n:
#         return 2*n
#     else:
#         return n
# print(fxn(7))

# # Assignment Q2:
# def max(a,b,c):
#     if (a>b and a>c) or (a==b and a>c) or (a==c and a>b):
#         return "Maximum: %s"%a
#     elif (b>a and b>c) or (b==a and b>c) or (b==c and b>a):
#         return "Maximum: %s"%b
#     elif (c>a and c>b) or (c==a and c>b) or (c==b and c>a):
#         return "Maximum: %s"%c
# # Note: This automarically works if two or more numbers are equal
# print(max(344,3356,344))

# Assignment Q3:

# def tri_spec(a,b,c):
#     if a<(b+c) and b<(c+a) and c<(a+b):
#         if (a**2 +b**2==c**2) or (a**2 +c**2==b**2) or (c**2 +b**2==a**2):
#             print("Yes, these form a triangle \nIt is a right-angled triangle")
#         elif (a==b==c):
#             print("Yes, these form a triangle \nIt is an equilateral triangle")
#         elif (a==b and a!=c) or (b==c and b!=a) or (c==a and c!=b):
#             print("Yes, these form a triangle \nIt is an isosceles triangle")
#         else:
#             print("Yes, these form a triangle \nIt is a scalene triangle")
#     else:
#         print("These sides doesn't form a triangle")

# print(tri_spec(2,1,3))

# Assignment Q3:
# def is_phone_num(string):
#     if len(str(string))!=10:
#         print("It is not a valid phone number")
#     elif len(str(string))==10:
#         if int((stkumuja@098765r(string))[0])==(1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9):
#             if int((str(string))[1])==(0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9):
#                 if int((str(string))[2])==(0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9):
#                     if int((str(string))[3])==(0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9):
#                         if int((str(string))[4])==(0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9):
#                             if int((str(string))[5])==(0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9):
#                                 if int((str(string))[6])==(0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9):
#                                     if int((str(string))[7])==(0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9):
#                                         if int((str(string))[8])==(0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9):
#                                             if int((str(string))[9])==(0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9):
#                                                 print("It is a valid phone number")
        


# print(is_phone_num(5209548909))
# def is_leap(year):
#     if year%100==0:
#         if year%400==0:
#             return True
#         else:
#             return False
#     elif year%4==0:
#         return True
#     else:
#         return False
    
# year = int(input())
# print(is_leap(year))

