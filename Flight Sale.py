clas = input("What class are you flying? (standard or first): ")

def aes(standard,distance):
    if clas.lower() == "standard":
        if distance >1000:
            standard = standard*0.85
            return standard
        else:
            standard = standard*0.925
            return standard

def sha(standard,first,distance):
    if clas.lower() == "standard":
        if distance >1000:
            standard = standard*0.85
            return standard
        else:
            standard = standard*0.925
            return standard
    elif clas.lower() == "first":
        if distance >1000:
            first = first*0.70
            return first
        else:
            first = first*0.9
            return first

def otp(standard,first,distance):
    if clas.lower() == "standard":
        if distance >1000:
            standard = standard*0.85
            return standard
        else:
            standard = standard*0.925
            return standard
    elif clas.lower() == "first":
        if distance >1000:
            first = first*0.70
            return first
        else:
            first = first*0.9
            return first

def tls(standard,first,distance):
    if clas.lower() == "standard":
        if distance >1000:
            standard = standard*0.85
            return standard
        else:
            standard = standard*0.925
            return standard
    elif clas.lower() == "first":
        if distance >1000:
            first = first*0.70
            return first
        else:
            first = first*0.9
            return first

flight = input("Where is the destination? (3 letters): ")
if flight.lower() == "aes":
    print("The cost of your ticket is £",aes(106,700))
elif flight.lower() == "sha":
    print("The cost of your ticket is £",sha(1000,2200,5700))
elif flight.lower() == "otp":
    print("The cost of your ticket is £",otp(95,190,1400))
elif flight.lower() == "tls":
    print("The cost of your ticket is £",tls(115,210,690))