class Dog:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

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



