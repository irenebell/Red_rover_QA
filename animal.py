class Animal:
    def __init__(self, name='Animal', age=0, color="red"):
        self.name = name
        self.age = age
        self.color = color
        print('Create object of Animal class')

    def print_info(self):
        print(f'Name animal is {self.name}, {self.color} color, {self.age} years old')

    # def get_name(self):
    #     return self.__name
    #
    # def set_name(self, name):
    #     self.__name = name