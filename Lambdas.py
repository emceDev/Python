x = lambda a : a + 10
print(x(1))

y = lambda q, x: q + x
print(y(2, x(1)))

def anon(e):
    return lambda r : e * r
    
doubler = anon(2)

print doubler(3)