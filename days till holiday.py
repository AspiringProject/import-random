autumndays = 73
springdays = 56
summerdays = 66

term = str(input("What term are you in?"))
dayscomp = int(input("How many days have you been in school?"))
if term.lower() == "autumn":
    daysleft = 73 - dayscomp

if term.lower() == "spring":
    daysleft = 56 - dayscomp

if term.lower() == "summer":
    daysleft = 66 - dayscomp

print(daysleft)

