class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def use_power(self):
        print(f"{self.name} uses their {self.power} to save {self.city}!")

    def __str__(self):
        return f"{self.name}, the superhero with {self.power}, protects {self.city}."

class Villain(Superhero):
    def __init__(self, name, power, city, evil_plan):
        super().__init__(name, power, city)
        self.evil_plan = evil_plan

    def use_power(self):
        print(f"{self.name} uses their {self.power} to execute their evil plan: {self.evil_plan}!")

hero = Superhero("Iron Man", "Armor Suit", "New York")
villain = Villain("Thanos", "Infinity Stones", "New York", "Eliminate half of the universe")

print(hero)
hero.use_power()

print(villain)
villain.use_power()
