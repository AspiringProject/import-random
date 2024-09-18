import re

name = input("Enter your name: ")

valid = re.match("[A-Z]",name)

if valid:
    print("That looks ok")

while not valid:
    print("Try Again With A Capital")
    name = input("Enter your name: ")
    valid = re.match("[A-Z]",name)
    print("That looks ok")

#Task 2

import re

email = input("Enter your email address: ")
valid = re.match("[a-z]",email)
if valid:
    print("That looks ok")
while not valid:
    print("Erm, try again")
    email = input("Enter your email address: ")
    valid = re.match("[a-z]",email)
    print("That looks ok")


import re

phnum = input("Enter your phone number: ")
valid = re.match("[0-9]",phnum)
if valid:
    print("That looks ok")
while not valid:
    print("Try again")
    phnum = input("Enter your phone number: ")
    valid = re.match("[0-9]",phnum)
    print("That looks ok")

#Task 3

import re
code = input("Enter your postcode: ")
valid = re.match("[A-Z]{2}[0-9]{2}[A-Z]{2}",code)

if valid:
    print("That looks ok")
while not valid:
    print("Try again")
    code = input("Enter your postcode: ")
    valid = re.match("[A-Z]{2}[0-9]{2}[A-Z]{2}",code)
    print("That looks ok")
    


