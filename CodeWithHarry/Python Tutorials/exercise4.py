# Pattern Printing:
while True:
    try:
        num= int(input("How many lines to print? "))
        Bool = int(input("Enter the boolean value 0 or 1: "))
        if Bool==True:
            i=1
            while i<=num:
                print("*"*i)
                i+=1
        elif Bool==False:
            j=num
            while j>=1:
                print("*"*j)
                j-=1
    except Exception as e:
        print(e)