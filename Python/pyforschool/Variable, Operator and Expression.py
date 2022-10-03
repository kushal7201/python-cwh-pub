# ###1
# name = input("Enter your name: ")
# print("Hello %s"%name)

# ###2
# num1 = int(input("enter a number: "))
# num2 = int(input("enter another number: "))
# print(num1+num2)

# ###3 
# temp = int(input("enter temperature in celsius: "))
# print((9*temp)/5 + 32)

# ###4
# print("Let's calculate Simple interest...")
# principle = float(input("Enter principle = "))
# rate = float(input("Enter rate = "))
# time = float(input("Enter time = "))
# print("Simple interest = %s"%((principle*rate*time)/100))

# ###5
# sec = int(input("Enter time in seconds: "))
# hours = sec//3600
# minutes = sec%3600//60
# seconds = sec%60
# print("Hours: %s"%hours)
# print("Minutes: %s"%minutes)
# print("Seconds: %s"%seconds)

# ###6
# num1 = float(input("Enter 1st number: "))
# num2 = float(input("Enter 2nd number: "))
# temp = num1
# num1 = num2
# num2 = temp
# print("After swapping, the 1st, 2nd number is: %s"%num1,num2)

###7
# num1 = float(input("Enter 1st number: "))
# num2 = float(input("Enter 2nd number: "))
# num1,num2 = num2,num1
# print("After swapping, the 1st, 2nd number is: %s"%num1,num2)

# ###8
# import math
# radius = float(input("Enter the radius of circle = "))
# area = math.pi*(radius**2)
# circumference = 2*math.pi*radius
# print("Area of the circle is: %s"%area)
# print("Circumference of the circle is: %s"%circumference)

# ###9
# similarly can be done

# ###10
# from math import sqrt
# a = float(input("Enter side a: "))
# b = float(input("Enter side b: "))
# c = float(input("Enter side c: "))
# s = (a+b+c)/2
# area = sqrt(s*(s-a)*(s-b)*(s-c))
# print(area)

# ###11
# p = float(input("Enter the principle = "))
# r = float(input("Enter interest rate = "))
# t = float(input("Enter time(in years) = "))
# ci = p*((1+r/100)**t) -p
# print("Compound interest is: %s"%ci)