from math import *
from functools import reduce
from my_calc import *
import re


list_10 = [1, 5, 4, 77, 33, 2]
print(list(map(lambda x: x * 3, list_10)))


# task 1
def square(a):
    return a * 4, a ** 2, sqrt(2) * a


print(square(5))


# task 2

def print_args(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')


print_args(name='John', last_name='Smith', age=35, position='web developer')


# task 3

my_list = [20, -3, 15, 2, -1, -21]
new_list = list(filter(lambda x: x > 0, my_list))
print(new_list)

# task 4

print(reduce(lambda x, y: x*y, my_list))
print(reduce(lambda x, y: x*y, new_list))

# task 5

print(multiply(5, 7))
print(addition(5, 7))
print(subtraction(5, 7))
print(division(5, 0))

# def tests():
#     assert addition(5, 7) == 12, 'Invalid result'
#     assert division(5, 0) == "Can't divide by zero"
#
# tests()


list_10 = [1, 5, -4, -77, 33, 2]
print(sum(filter(lambda x: x > 0, list_10)))

list_11 = [2, 1, 10]
print(max(list_11) - min(list_11))
# or

if len(list_11) <= 1:
    print(0)
diff = []
list_11.sort()
for i in range(len(list_11)):
    if i + 1 < len(list_11):
        t = abs(list_11[i] - list_11[i+1])
        diff.append(t)
print(sum(diff))


def remove_numbers(s):
    return re.sub(r'\d', '', s)

print(remove_numbers('dgtr454646hhhh cdrt5'))


def sum_of_digits(number):
    result = sum(map(int, str(number)))
    while result // 10 != 0:
        result = sum(map(int, str(result)))
    return result


print(sum_of_digits(6574888))

sample = {"Hello", "How", "Are", "You", "Bow"}
sample.discard("I'm fine")
print(sample)
print(type(sample))


def move_zeros(lst):
    new = filter(lambda x: x != 0, lst)
    new_2 = filter(lambda x: x == 0, lst)
    return list(new) + list(new_2)


print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))

def correct_polish_letters(st):
    return st.translate(str.maketrans('ąćęłńóśźż', 'acelnoszz'))

print(correct_polish_letters("Jędrzej Błądziński"))
