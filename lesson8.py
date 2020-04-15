cities = ["New York", "Moscov", "new dehli", "singapure", "Kiev"]
print(cities)
print(len(cities))
print(cities[0])
print(cities[2].title())
print(cities[3].upper())

cities[4] = "Tula"
print(cities[4])
cities.append("Kursk")
print(cities)
cities.insert(1, "lviv")
print(cities)
del cities[3]
print(cities)

cities.remove("Tula")
print(cities)

deleted_city = cities.pop()
print(cities)
print(deleted_city)
cities.sort()
print(cities)
cities.sort(reverse=True)
print(cities)
