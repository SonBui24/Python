class Dog:
    species = 'mammal'
    is_hungry = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        self.is_hungry = False

    def description(self):
        return f'{self.name} is {self.age} years old'

    def speak(self, sound):
        return f'{self.name} says {sound}'


class RussellTerrier(Dog):
    def run(self, speed):
        return f'{self.name} runs {speed}'


class Bulldog(Dog):
    def run(self, speed):
        return f'{self.name} runs {speed}'

class Pet:
    dogs = []
    def __init__(self, dogs):
        dogs = self.dogs

dogs = [Dog('Tom', 6), Dog('Jerry', 9), Dog('But', 3), Dog('Wine', 1)]

print(f'I have {len(dogs)} dogs')
for dog in dogs:
    print(f'{dog.name} is {dog.age}', end=". ")
print(f"\nAnd they're all {dog.species}, of course")

my_dogs_are_not_hungry = False
for dog in dogs:
    if dog.is_hungry:
        my_dogs_are_not_hungry = True
if my_dogs_are_not_hungry:
    print("My dogs are not hungry")
else:
    print("My dogs are hungry")
