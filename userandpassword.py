username = input("What is your username?")
password = input("What is your password?")
passchar = len(password)
if passchar < 6:
    print("Long enough")
else: print ("Too short")
if username == password:
    print("Password cannot be same as username")
else:
    print("Password unique")


