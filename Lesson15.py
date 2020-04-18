def create_record(name, tel, adress):
    record = {
        'name': name,
        'phone': tel,
        'adress': adress
    }
    return record

user1 = create_record('Vasya', ' +11231', "Tunis")
user2 = create_record("petya", '1823479', "Ukr")

print(user1)
print(user2)

def give_award(medal, *person):
    for person1 in person:
        print("Tovarisch " + person1.title() + " nagrazhdaetsya medaliyu " + medal)

give_award("Za Berlin", "Vasya", "petya")
give_award('Za London',"petya")
