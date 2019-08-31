a = 34
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

if a > b: print("a is greater than b") 

c=3

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

    #while
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1