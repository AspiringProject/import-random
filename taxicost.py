time = int(input("What is the hour (24 Hour Clock): "))
cost = 0
firstcost = 3
extracost = 2
miles = int(input("How many miles are you traveling?: "))
extramiles = miles - 1
cost1 = extramiles * extracost
cost = cost1 + 3
latecost = cost * 2
if time > 8 and time < 20:
    print("This trip will cost £",cost)
elif time < 8 and time > 20:
    print("This trip will cost £",latecost)

