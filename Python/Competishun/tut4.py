# def max(a,b,c):
#     if a>=b and a>=c:
#         return "Maximum: %s"%a
#     elif b>=c and b>=a:
#         return "Maximum: %s"%b
#     else:
#         return "Maximum: %s"%c 

# print(max(32,3,2))

# import re
# def is_phone_number():
#     x= str(input("Write: "))
#     n= len(re.findall('[0-9]',x))
#     if len(x)!= 10:
#         return "Not a phone number, because it's not 10 digits"
#     elif n!=10:
#         return "Not a phone number, because it contains characters other than numbers"
#     elif x[0]==str(0):
#         return "Not a phone number, as it starts with zero"
#     else:
#         return "Is a phone number"
# print(is_phone_number())

# def distance(x1,y1,x2,y2):
#     return ((x1-x2)**2+(y1-y2)**2)**0.5
# # print(distance(23,22,21,20))

# # Coordinates of 1st Point:
# x1=1
# y1=2
# # Coordinates of 2nd Point:
# x2=-2
# y2=1
# # Coordinates of 3rd Point:
# x3=-1
# y3=-2
# # Coordinates of 4th Point:
# x4=2
# y4=-1

# d1=distance(x1,y1,x2,y2)
# d2=distance(x2,y2,x3,y3)
# d3=distance(x3,y3,x4,y4)
# d4=distance(x4,y4,x1,y1)
# d5=distance(x1,y1,x3,y3)
# d6=distance(x2,y2,x4,y4)

# def is_square():
#     if d1==d2==d3==d4 and d5==d6:
#         print("These points form a square")
#     elif d1==d2 and d3==d4==d5==d6:
#         print("These points form a square")
#     else:
#         print("These points do not form a square")

# is_square()

# def times_table(n):
#     for i in range(10):
#         print(n*(i+1))
        
# def times_table1(n):
#     for i in range(1,10):
#         print(n*i)

# def times_table2(n):
#     i=1
#     while i<=10:
#         print(i,n*i)
#         i+=1


# for i in range(1,6):
#     print(i,"A"*i)


# i=1
# while i<=5:
#     print("A"*i)
#     i+=1


# i=1
# j=1
# while i<=5:
#     while j<=i:
#         print("A"*j)
#         j+=1
#     i+=1

# def total(n):
#     sum =0
#     i=1
#     numb=n
#     while numb<100:
#         sum+=numb
#         print(i, numb)
#         numb+=n
#         i+=1
#     return sum

# a=total(3)
# b=total(5)
# c=total(15)
# print(a+b-c)
# palindrome = True

# n=str(input("Enter number: "))
# for i in range(int(len(n)/2)):
#     if n[i]!=n[len(n)-i-1]:
#         palindrome=False

# print(palindrome)


# palindrome=True
# n= 12345654321
# temp1= n
# reverse =0
# while temp1>0:
#     temp2=temp1%10
#     reverse= reverse*10+temp2
#     temp1//=10
# if n!=reverse:
#     palindorme=False
# print(palindrome)  
    
# print(reverse)


# Assignment Q1:
# import re
# string = "iuds dshcewe isadskj"
# def vow_cons_spac(string):
#     a=len(re.findall(("a","e","i","o","u"),string))
#     b=len(re.findall(" ",string))
#     c=len(re.findall("b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z",string))
#     return "Vowels: %s"%a, "Consonants: %s"%c, "Spaces: %s"%b

# print(vow_cons_spac(string))

# Assignment Q2:
# string1="ojef"
# string2="aefodw"
# for i in range(len(string1)):
#     for j in range(len(string2)):
#         if string1[i]==string2[j]:
#             print(string1[i])
#         else:
#             print("None")
#             break

# Assignment Q3:
# def collatz(n):
#     temp1 =n
#     print(temp1)
#     while temp1!=1:
#         if temp1%2==0:
#             temp1=temp1/2
#         else:
#             temp1=3*temp1+1
#         print(int(temp1))

# collatz(35987327177102465061134257892345)

