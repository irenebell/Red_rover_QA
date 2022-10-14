from animal import Animal

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age, color)


    def is_meowing(self):
        print(f'{self.name} is meowing')

    def print_info(self):
        print(f'Cat is {self.name}, {self.color} color, {self.age} years old')


