#Superheroes
heroes = ["Batman","Wonder Woman","Superman","Spiderman"]
print("Current Pilot: ",heroes[0])
print("Current Co-pilot: ",heroes[1])
heroes.remove("Superman")
heroes.insert(2,"Hit Girl")
heroes.append("Mermaid Man")
heroes.append("Barnacle Boy")
print(heroes)
num = int(input("What number hero do you want to swap (0-5)? "))
newHero = input("What should the new hero be called? ")
heroes[num] = newHero
print(heroes)


#Villains
villains = ["The Joker","Magneto","Red Mist","Doc Ock"]
wages = [21,17,3,5]
for counter in range(4):
    print(villains[counter],": £",wages[counter]," million")
totalWages = int(0)
for i in wages:
    totalWages += i
print("The total wage of all villains is: ",totalWages)
    


