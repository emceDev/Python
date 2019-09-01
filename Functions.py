def function(food):
    i=1
    for x in food: 
        i += 1
        print(i)
        if i == 4:
            continue
        print x

fruits = ["apple", "banana", "cherry","gatery","gatery","gatery"]

function(fruits)


def func(login = "Nie podano loginu"):
    print("to jest login " + login)

func("marcello")
func()

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

