firstnum = int(input("What is your first integer?"))
secondnum = int(input("What is your second integer?"))

sub = firstnum - secondnum
print(sub,"is",firstnum,"-",secondnum)

mult = firstnum * secondnum
print(mult,"is",firstnum,"*",secondnum)

add = firstnum + secondnum
print(add,"is",firstnum,"+",secondnum)

div = firstnum / secondnum
print(div,"is",firstnum,"/",secondnum)

if firstnum > secondnum:
  print(firstnum,">",secondnum)
else:
  print(firstnum,"is not >",secondnum)

if firstnum < secondnum:
  print(firstnum,"<",secondnum)
else:
  print(firstnum,"is not <",secondnum)

if firstnum == secondnum:
  print(firstnum,"=",secondnum)
else:
  print(firstnum,"!=",secondnum)