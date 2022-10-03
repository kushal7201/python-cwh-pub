# Health Management System
def getdate():
           import datetime
           return datetime.datetime.now()

while True:
    print("Welcome to the Health Management System!--made by Kushal\nDo make wise use of it.")
    print("Select the client:\npress '1' for Harry\npress '2' for Rohan\npress '3' for Hammad")
    client = int(input("Enter here: "))
    print("press '1' for exercise\npress '2' for diet")
    option = int(input("Enter here: "))
    print("press '1' for data reteiving\npress '2' for data logging")
    choice = int(input("Enter here: "))
    def health_log():
        """This function logs the data of exercise or diet of Harry, Rohan and Hammad"""
        if client==1:
            if option==1:
                with open("exharry.txt", "a") as a:
                    log = input("Just write here: ")
                    k = str(getdate())
                    a.write("\n[%s] %s"%(k,log))
                    print("You have successfully logged the data!")
            elif option==2:
                with open("dietharry.txt", "a") as a:
                    log = input("Just write here: ")
                    k = str(getdate())
                    a.write("\n[%s] %s"%(k,log))
                    print("You have successfully logged the data!")
        elif client==2:
            if option==1:
                with open("exrohan.txt", "a") as a:
                    log = input("Just write here: ")
                    k = str(getdate())
                    a.write("\n[%s] %s"%(k,log))
                    print("You have successfully logged the data!")
            elif option==2:
                with open("dietrohan.txt", "a") as a:
                    log = input("Just write here: ")
                    k = str(getdate())
                    a.write("\n[%s] %s"%(k,log))
                    print("You have successfully logged the data!")
        elif client==3:
            if option==1:
                with open("exhammad.txt", "a") as a:
                    log = input("Just write here: ")
                    k = str(getdate())
                    a.write("\n[%s] %s"%(k,log))
                    print("You have successfully logged the data!")
            elif option==2:
                with open("diethammad.txt", "a") as a:
                    log = input("Just write here: ")
                    k = str(getdate())
                    a.write("\n[%s] %s"%(k,log))
                    print("You have successfully logged the data!")

    def health_retreive():
        """This function retreives the data of exercise or diet of Harry, Rohan and Hammad"""
        if client==1:
            if option==1:
                with open("exharry.txt") as a:
                    for line in a:
                        print(line, end ="")
            elif option==2:
                with open("dietharry.txt") as a:
                    for line in a:
                        print(line, end ="")
        elif client==2:
            if option==1:
                with open("exrohan.txt") as a:
                    for line in a:
                        print(line, end ="")
            elif option==2:
                with open("dietrohan.txt") as a:
                    for line in a:
                        print(line, end ="")
        elif client==3:
            if option==1:
                with open("exhammad.txt") as a:
                    for line in a:
                        print(line, end ="")
            elif option==2:
                with open("diethammad.txt") as a:
                    for line in a:
                        print(line, end ="")

    if choice==1:
        health_retreive()
    elif choice==2:
        health_log()
    prompt = int(input("\npress '1' for again or press '0' to stop: "))
    if prompt==1:
        continue
    else:
        break



