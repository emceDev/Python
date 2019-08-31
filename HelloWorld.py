print("hello World via python")
print 2+2

#Fajne komentarze w tym pythonie
if 2 is not 3:print("2-ka nie jest 3-ka")

    #Wiele zmiennych 
u , y, z, w="2","3","3","2"
print(u+y+z+w)

q,e=2,3
print(q+e)

#Globalna funkcja w Pythonie

x="Global"
def firstFunc():
    print("fist function and it is "+x)

firstFunc()

def localFunc():
    x="local"
    print("first "+ x + " function")

localFunc()

def globalToLocalFunc():
    global x
    x="Became global"
    print("it will use "+x+" variable")

globalToLocalFunc()
print x