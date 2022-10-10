def is_leap_yr():
    n=int(input("Enter a natural number: "))
    if n%100==0:
        if n%400==0:
            return "It is leap year"
        else:
            return "It is not a leap year"
    elif n%4==0:
        return "It is leap year"
    else:
        return "It is not a leap year"

print(is_leap_yr())