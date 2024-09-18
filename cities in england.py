def question():
    print("How many cities are there in England?")
    answer = int(input())
    while answer !=51:
        print("No,that's not correct")
        print("Try again")
        answer = int(input())
    print("That's correct! ")
question()
