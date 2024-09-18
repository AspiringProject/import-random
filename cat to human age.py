catAge = int(input("Enter age of cat: "))
humanAge = int(0)
if catAge == 1:
    humanAge = 15
elif catAge == 2:
    humanAge = 15 + 9
else:
    humanAge = (catAge - 2) * 4 + 15 +9
print("Your cat is " + str(humanAge) + " in human years")
