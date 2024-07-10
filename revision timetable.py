#Timetable contents
mondayAM = "Computer Science"
tuesdayAM = "Maths"
tuesdayPM = "Science"
wednesdayPM = "English"
thursdayAM = "Computer Science"
thursdayPM = "Computer Science"
fridayAM = "Music"

 #Ask user for the day of the week
day = input("What day of the week is the exam? ")
time = input("What time is the exam? ")
if time > "12:00":
    time = "pm"
else:
    time = "am"

#Display exam
if day.lower() == "monday" and time == "am":
    print("You have a", mondayAM, "exam on Monday morning.")
elif day.lower() == "tuesday" and time == "am":
    print("You have a", tuesdayAM, "exam on Tuesday morning.")
elif day.lower() == "tuesday" and time == "pm":
    print("You have a", tuesdayPM, "exam on Tuesday afternoon.")
elif day.lower() == "wednesday" and time == "pm":
    print("You have a", wednesdayPM, "exam on Wednesday afternoon.")
elif day.lower() == "thursday" and time == "am":
    print("You have a", thursdayAM, "exam on Thursday morning.")
    study1 = True
    study2 = True
elif day.lower() == "thursday" and time == "pm":
    study = True
    print("You have a", thursdayPM, "exam on Thursday afternoon.")
elif day.lower() == "friday" and time == "am":
    print("You have a", fridayAM, "exam on Friday morning.")
else:
    print("There is no exam scheduled for that time.")

#Study for exams
if study == True:
    print("\nStudy for the exam on Thursday morning:")
    print("CPU Architecture, Memory, Storage, Networks:\n")
    print("Study for the exam on Thursday afternoon:")
    print("System Software, Security, Databases, Programming.\n")