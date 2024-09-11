mark = int(input("Enter your mark: "))
if mark <50:
    print("Unsatisfactory")
elif mark >= 50 and mark < 60:
    print("Satisfactory")
elif mark >= 60 and mark < 70:
    print("Good")
elif mark >= 70 and mark < 90:
    print("Very Good")
else:
    print("Excellent")