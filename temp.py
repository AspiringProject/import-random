temp1 = 0
temp2 = 0
total = 0
count = 0
while count < 366:
    temp = int(input("what is the temperature?"))
    if temp < 15:
        temp1 = temp1 + 1
    elif temp > 20:
        temp2 = temp2 + 1
    total = total + temp
    print(total)
    count = count + 1
print(temp1, temp2, total/365)
    
