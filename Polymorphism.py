class Animal:
    def move(self):
        pass

class Dog(Animal):
    def move(self):
        print("The dog runs on four legs 🐕.")

class Bird(Animal):
    def move(self):
        print("The bird flies in the sky 🦅.")

class Fish(Animal):
    def move(self):
        print("The fish swims in the water 🐟.")

dog = Dog()
bird = Bird()
fish = Fish()

animals = [dog, bird, fish]
for animal in animals:
    animal.move()
