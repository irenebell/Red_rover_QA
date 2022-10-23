from animal import Animal

class Dog(Animal):
    def __init__(self, name, age, color, breed='Terrier'):
        super().__init__(name, age, color)
        self.breed = breed

    def is_barking(self):
        print(f'{self.name} is barking')



