class Dog:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

phake = Dog('Fake', 2)

chuot = Dog('Mickey', 7)

phuc = Dog('Fuk', 5)

def get_biggest_number(*args):
    return max(args)

print(f'The oldest dog is {get_biggest_number(phake.age, chuot.age, phuc.age)} years old.')
