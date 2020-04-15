cars = ["bmv", "volvo", "audi", "skoda", "fiat", "lada"]

for car in cars:  # вывод всех елементов массива
    print(car.upper())

for car in range(1, 7):
    print(car)

mynumber_list = list(range(0, 10))  # создание массива с диапазоном от нуля до 9
print(mynumber_list)

for x in mynumber_list:
    x = x * 2
    print(x)

mynumber_list.sort(reverse=True)
print(mynumber_list)

print(max(mynumber_list))
print("Min number is: " + str(min(mynumber_list)))
print("Summ of list is: " + str(sum(mynumber_list)))

mycars = cars[1:3]
print(mycars)
mycars = cars[:4]
print(mycars)
mycars = cars[-3:]
print(mycars)

mycars = cars[:]  # копирование всего массива
