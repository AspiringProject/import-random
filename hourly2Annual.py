hourlyRate = float(input("How much do you make an hour?"))
hoursWorkedDaily = float(input("How many hours do you work in a day"))

weeksInAYear = 48
daysInAWeek = 5

annualEarnings = hourlyRate*hoursWorkedDaily*weeksInAYear*daysInAWeek

print(annualEarnings)
