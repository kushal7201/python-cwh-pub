# ### Exercise1
# num1 = int(input("Enter a number = "))
# num2 = int(input("Enter another number = "))
# if (num1*num2)<=1000:
#     print(num1*num2)
# else:
#     print(num1+num2)

### Exercise2
# print("Printing current and previous number and their sum in a range(10)")
# i = 0
# j = i-1
# sum = 0
# while i<10:
#     if i==0:
#         print("Current Number 0 Previous Number  0  Sum:  0")
#         i+=1
#         j+=1
#     elif 1<=i<10:
#         print("Current Number %s Previous Number  %s  Sum:  %s"%(i,j,i+j))
#         i+=1
#         j+=1


# print("Printing current and previous number and their sum in a range(10)")
# previous_num = 0
# for i in range(1, 11):
#     x_sum = previous_num + i
#     print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)
#     previous_num = i

# ### Exercise3
# print("Orginal String is  pynative")
# print("Printing only even index chars")
# string = "pynative"
# length = len(string)
# i = 0
# while i<int(length):
#     if i%2==0:
#         print(string[i])
#     i+=1

# print("Orginal String is  pynative")
# print("Printing only even index chars")
# string = "pynative"
# for i in string[0::2]:
#     print(i)

### Exercise4
# def remove_chars(a,b):
#     s1 = ""
#     for i in range(int(b),len(a)):
#         s1+=a[i]
#     return s1
# print(remove_chars("pynative",10))
###### OR
# def remove_chars(a,b):
#     x = a[int(b):]
#     return x
# print(remove_chars("pynative",4))

# ### Exercise5
# number_x = [10,20,30,40,10]
# number_y = [75,65,35,75,30]
# def first_last_same(a):
#     print("Given list: %s"%a)
#     print("result is %s"%(a[0]==a[-1]))

# first_last_same(number_x)

# ### Exercise6

# list = [10, 20, 33, 46, 55]
# print("Given list is  [10, 20, 33, 46, 55]")
# print("Divisible by 5")
# for i in list:
#     if i%5==0:
#         print(i)

### Exercise7
# str_x = "Emma is good developer. Emma is a writer"
# print("Emma appeared %s times"%str_x.count("Emma"))
### OR:
# def count_emma(statement):
#     print("Given String: ", statement)
#     count = 0
#     for i in range(len(statement) - 1):
#         count += statement[i: i + 4] == 'Emma'
#     return count
# count = count_emma("Emma is good developer. Emma is a writer")
# print("Emma appeared", count, "times")

### Exercise8
# i = 1
# while i<11:
#     print(str(i)*i)
#     i+=1
####OR
# for num in range(11):
#     for i in range(num):
#         print(num, end =" ")
#     print()

### Exercise9
# while True:
#     i = 0
#     reverse_num = ""
#     num = input("Enter a number: ")
#     length = len(num)
#     while i<length:
#         reverse_num+= num[length-i-1]
#         i+=1
    # if num == reverse_num:
    #     print("Yes. given number is palindrome number")
    # else:
    #     print("No. given number is not palindrome number")
#######  OR:
# def palindrome(num):
#     reverse_num = 0
#     original_num = num
#     while num>0:
#         remainder = num%10
#         reverse_num = (reverse_num*10) + remainder
#         num = num//10
#     if original_num == reverse_num:
#         return True
#     else:
#         return False
# print(palindrome(111))

# ### Exercise10
# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# final_list = []
# for i in list1:
#     if i%2!=0:
#         final_list.append(i)
# for i in list2:
#     if i%2==0:
#         final_list.append(i)
# print(final_list)


### Exercise11
while True:
    num = input("Enter a number: ")
    for i in range(0,len(num)):
        print(num[len(num)-i-1], end = " ")
    print()