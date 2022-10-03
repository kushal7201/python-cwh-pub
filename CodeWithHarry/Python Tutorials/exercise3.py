n= 4112

print("Welcome to the Number Guessing Quiz!--made by Kushal")
i=1
while i<=6:
    num= float(input("Guess a number between 2500 to 5000: "))
    if num<n:
        print("Please kuch bada socho!!")
        print("Number of guesses left: %s"%(6-i))
        i+=1
        continue

    elif num>n:
        print("Apne paon zameen par hi rakho!!")
        print("Number of guesses left: %s"%(6-i))
        i+=1
        continue

    elif num==n:
        print("Kudos! after %s attempts, you have got it right"%i)
        break
print("Game Over!")