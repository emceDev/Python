x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(z))
b = int(y)
print(type(b))
u = int(y) # y will be 2
print(u)
import random

print(type(random.randrange(1,10)))

print(random.triangular(20, 60, 30))

#first array
o="-st,m"
print(str(x)+o[0:3]+" not array taking characters")
print(len(o))

txt = "The rain in Spain kurwa mainly in the plain"
p = "kurwa" in txt
print("niedozwolone slownictwo: " + str(p))

age = 20
txt = "My name is not John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


#ArrayS
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
thislist.append("bluange")
thislist.insert(1, "organge")
thislist.pop(0)

for x in thislist:
  print(x)

del thislist[1:3]

theselist=["meat","fishies"]
thoselist=theselist+thislist
print thoselist

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

#for x in list2:
  #list1.append(x)
list1.extend(list2)
print(list1)
