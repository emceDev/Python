class FirstClass:
    x=4
print(FirstClass.x)

fo = FirstClass()
print(fo.x)

class Narcotics:
    def __init__(self, name, dose):
        self.name = name
        self.dose = dose
    
n1 = Narcotics("marihuanen", "enough")

print(n1.dose)
print(n1.name)

class A:
    def __init__(self, name):
        self.name = name

object1 = A("objectA")
print(object1.name)

class B(A):
    pass
object2 = B("Mathew")
print(object2.name)

class C(B):
    def __init__(self, name, gender):
        B.__init__(self, name)
        self.gender = gender
    def introduce(self):
        print("Bark! bark! " + self.name + " " + self.gender)

object3 = C("Millieu", "female")
object3.introduce()

class Animals:
    def __init__(self, specie ,gender):
        self.specie = specie
        self.gender = gender

class Dogs(Animals):
    def __init__(self,specie,gender,name):
        Animals.__init__(self,specie,gender)
        self.name = name
    def Sound(self):
        print("bark! or HOW! WOW!" +self.gender+self.specie+self.name)

mili = Dogs("female","doggo","Millie")
mili.Sound()

class Human(Dogs):
    def __init__(self,specie,gender,name,lname):
        Dogs.__init__(self,specie,gender,name)
        self.lname = lname

    def Introduce(self):
        print("Hi I am "+self.gender+self.specie+self.name+self.lname)
    def Sound(self):
        print("I speak :)")
mateusz= Human(" Human", " male", " mattgew", " kwalsy " + "i dont take any " + n1.name)
mateusz.Introduce()
mateusz.Sound()