#variables
x = 0
total = int(0)
add = 0
fortnite = 0
while add != -1 or fortnite >= 1:
#x to increment by one each iteration
    x = x + 1
#allow user to input a number
    add = int(input("State your number: "))
#add number to total
    total = total + add
    if total >=101:
        print("total: ",total)
        print("avg: ",avg)
#print total
    print(total)
#average
    avg = total / x
print(avg)
