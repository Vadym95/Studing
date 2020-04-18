

def nap_privetstvie(name):
    print("Contratulations!!!" + name + " Pidrila")
    print("HELLO! ")


def aaa():
    print("aaa")\

def summa(x,y):
    print(x+y    )

def summa1(x,y):
    s = x + y
    return s

def summa2(x,y):
    return x + y

def fact(x):
    otvet = 1
    for i in range(1,x+1):
        otvet = otvet * i
    return otvet

nap_privetstvie("Denis")
aaa()
summa(5,10)
summa("lika",'LL')
x = summa1(33,22)
print(x)
x = summa2(3,3)
print(x)

print(fact(10))

for i in range (1,10):
    print(str(i) + "!\t = " + str(fact(i)))
