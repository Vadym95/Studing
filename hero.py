class Hero():
    def __init__(self, name, level, race):
        self.name = name
        self.level = level
        self.race = race
        self.health = 100
    def show_hero(self):
        discription = (self.name + " Level is: " +  str(self.level) + " Race is: " + self.race + " Health is: " + str(self.health)).title()
        print(discription)

    def level_up(self):
        self.level = self.level + 1

    def move(self):
        print("Hero " + self.name + " start moving...")\

    def set_health(self, new_health):
        self.health = new_health