x = 2
if x == 25:
    print("Yes")
else:
    print("No")

if x <= 4:
    print("You are baby")
elif x > 4 and x < 12:
    print("You are a kid")
elif x >= 12 and x < 19:
    print("You are a teenager")
else:
    print("You are old")

cars = ["bmv", "volvo", "audi", "skoda", "fiat", "lada"]

if "lada" in cars:
    print("Yes")
else:
    print("No")

german_cars = ["bmv", "audi", "skoda"]

for x in cars:
    if x in german_cars:
        print(x + " is german car")
    else:
        print(x + " is not German car")
