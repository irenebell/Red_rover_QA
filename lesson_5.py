from animal import Animal
from cat import Cat
from dog import Dog

animal = Animal()
print(animal.__dict__)
animal = Animal(name="Jack", age=2, color='white')
print(animal.__dict__)
animal.print_info()

dog1 = Dog('Chuck', 3, 'black', 'york')
print(dog1.__dict__)

dog1.print_info()
dog1.is_barking()

cat1 = Cat('Basya', 5, 'red')
print(cat1.__dict__)
cat1.print_info()
cat1.is_meowing()

cat2 = Cat("Pete")
print(cat2.__dict__)
