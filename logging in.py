def logging_in():
    attempts = 0
    print("Enter your password on the next line ")
    password = input()
    while password != "secret":
        attempts = attempts + 1
        print("That password is not the one stored")
        print("Failed attempts: ",attempts)
        print("Try again")
        password = input()
    print("Yes thats the correct password")

logging_in()
