
print("Welcome to the problem solver!--made by Kushal")
num= int(input("Enter number: "))
maxi= int(input("Enter limit: "))

def total_multiple_of(num,maxi):
    s=0
    i=num
    while i<=maxi:
        s+=i
        i+=num
    return ["The number of such multiples, their sum: ",(i-num)//num,s]
print(total_multiple_of(num,maxi))