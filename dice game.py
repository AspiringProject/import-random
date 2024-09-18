username1 = input("Username (lowercase) : ")

password1 = input("Password (case sensative) : ")

import time

import time

username2 = input("Username : ")

password2 = input("Password : ")


#Account System

if username1 == "tyler" and password1 == "PizzaMan6969":

    print("Authenticated Account")

elif username1 == "shrub" and password1 == "shrublybubbly":

    print("Authenticated Account")

else:

    print("Account not recognised")


#Round 1 

time.sleep(5)

print("Player 1 dice will be rolled now..")

score1 = random.randint(0,6)

print (score1)

score2 = random.randint(0,6)

print(score2)



time.sleep(5)

print("Player 2 dice will be rolled now..")

score3 = random.randint(0,6)

print (score3)

score4 = random.randint(0,6)

print(score4)


round1_player1score = score1 + score2

round1_player2score = score3 + score4

print("Overall Player1 got",round1_player1score,"and Overall Player2 got",round1_player2score)


#Round 2

time.sleep(5)

print("Player 1 dice will be rolled now..")

score5 = random.randint(0,6)

print (score5)

score6 = random.randint(0,6)

print(score6)



time.sleep(5)

print("Player 2 dice will be rolled now..")

score7 = random.randint(0,6)

print (score7)

score8 = random.randint(0,6)

print(score8)


round2_player1score = score5 + score6

round2_player2score = score7 + score8

print("Overall Player1 got",round2_player1score,"and Overall Player2 got",round2_player2score)


#Round 3

time.sleep(5)

print("Player 1 dice will be rolled now..")

score9 = random.randint(0,6)

print (score1)

score10 = random.randint(0,6)

print(score2)



time.sleep(5)

print("Player 2 dice will be rolled now..")

score11 = random.randint(0,6)

print (score3)

score12 = random.randint(0,6)

print(score4)


round1_player1score = score1 + score2

round1_player2score = score3 + score4

print("Overall Player1 got",round1_player1score,"and Overall Player2 got",round1_player2score)






#rules

num = int (input ("Enter any number to test whether it is odd or even: "))


if (num % 2) == 0:

    print ("The number is even")


else:

    print ("The provided number is odd")
