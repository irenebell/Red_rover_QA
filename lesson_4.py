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


# def remove_numbers(s):
#     return re.sub(r'\d', '', s)
#
# print(remove_numbers('dgtr454646hhhh cdrt5'))


# def subtract_sum_(number):
#     new = number - sum(map(int, str(number)))
#     if len(str(new)) > 1:
#         new = sum(map(int, str(new)))
#     fruits = {
# 1: 'kiwi',
# 2: 'pear',
# 3: 'kiwi',
# 4: 'banana',
# 5: 'melon',
# 6: 'banana',
# 7: 'melon',
# 8: 'pineapple',
# 9: 'apple',
# 10: 'pineapple',
# 11: 'cucumber',
# 12: 'pineapple',
# 13: 'cucumber',
# 14: 'orange',
# 15: 'grape',
# 16: 'orange',
# 17: 'grape',
# 18: 'apple',
# 19: 'grape',
# 20: 'cherry',
# 21: 'pear',
# 22: 'cherry',
# 23: 'pear',
# 24: 'kiwi',
# 25: 'banana',
# 26: 'kiwi',
# 27: 'apple',
# 28: 'melon',
# 29: 'banana',
# 30: 'melon',
# 31: 'pineapple',
# 32: 'melon',
# 33: 'pineapple',
# 34: 'cucumber',
# 35: 'orange',
# 36: 'apple',
# 37: 'orange',
# 38: 'grape',
# 39: 'orange',
# 40: 'grape',
# 41: 'cherry',
# 42: 'pear',
# 43: 'cherry',
# 44: 'pear',
# 45: 'apple',
# 46: 'pear',
# 47: 'kiwi',
# 48: 'banana',
# 49: 'kiwi',
# 50: 'banana',
# 51: 'melon',
# 52: 'pineapple',
# 53: 'melon',
# 54: 'apple',
# 55: 'cucumber',
# 56: 'pineapple',
# 57: 'cucumber',
# 58: 'orange',
# 59: 'cucumber',
# 60: 'orange',
# 61: 'grape',
# 62: 'cherry',
# 63: 'apple',
# 64: 'cherry',
# 65: 'pear',
# 66: 'cherry',
# 67: 'pear',
# 68: 'kiwi',
# 69: 'pear',
# 70: 'kiwi',
# 71: 'banana',
# 72: 'apple',
# 73: 'banana',
# 74: 'melon',
# 75: 'pineapple',
# 76: 'melon',
# 77: 'pineapple',
# 78: 'cucumber',
# 79: 'pineapple',
# 80: 'cucumber',
# 81: 'apple',
# 82: 'grape',
# 83: 'orange',
# 84: 'grape',
# 85: 'cherry',
# 86: 'grape',
# 87: 'cherry',
# 88: 'pear',
# 89: 'cherry',
# 90: 'apple',
# 91: 'kiwi',
# 92: 'banana',
# 93: 'kiwi',
# 94: 'banana',
# 95: 'melon',
# 96: 'banan',
# 97: 'melon',
# 98: 'pineapple',
# 99: 'apple',
# 100: 'pineapple'}
#
#     return fruits[new]
#
#
# print(subtract_sum_(1907))


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
