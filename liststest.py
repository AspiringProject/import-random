#Create list
primes = [2,3,5,7]
print("Before: ",primes)
#Add 11 to the end of the list
primes.append(11)
print("After: ",primes)


buses = ["31","5","63","331"]

#Places bus U9 in index 2
buses.insert(2,"U9")
#Removes bus 31
buses.remove("31")
print("Fleet:",len(buses),"buses")
print("Latest:",buses[-1])
print("All:",buses)


chars = ["?","a","D","%","a"]
#Finds the position of a in the list
print("Index of a:",chars.index("a"))





