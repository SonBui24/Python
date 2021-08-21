class Pets:

    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs

    def walk(self):
        for dog in self.dogs:
            print(dog.walk())


class Dog:
    species = 'mammal'
    is_hungry = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is walking'

    def description(self):
        return f'{self.name} is {self.age} years old'

    def speak(self, sound):
        return f'{self.name} says {sound}'

    def eat(self):
        self.is_hungry = False


class RussellTerrier(Dog):
    def run(self, speed):
        return f'{self.name} runs {speed}'


class Bulldog(Dog):
    def run(self, speed):
        return f'{self.name} runs {speed}'

dogs = [Dog('Tom', 6), Dog('Jerry', 9), Dog('But', 3)]
a = Pets(dogs)
a.walk()
