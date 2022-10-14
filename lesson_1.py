import pyautogui
import time

# task 1
# health = float(input('Enter your health: '))
# print(health > 0)

# task 2
# number = int(input('Enter the integer number: '))
# if number % 2 == 0:
#     print('Even')
# else:
#     print('Odd')

# or

# number = int(input('Enter the integer number: '))
# if number % 2:
#     print('Odd')
# else:
#     print('Even')


# task 3
# year = int(input('Enter the year: '))
# if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#     print('Leap year')
# else:
#     print('Non-leap year')

# task 4
# text = input('Enter your text: ')
# number = int(input('Enter the integer number: '))
# for i in range(number):
#     print(text)


def fibonacci(n):
    f0 = 0
    f1 = 1
    for k in range(2, n + 1):
        fib = f0 + f1
        f0 = f1
        f1 = fib
        print(fib)


fibonacci(10)

# press the key

# while True:
#     pyautogui.press('shift')
#     print('shift')
#     time.sleep(10)


def to_csv_text(array):
    new = ''
    for elem in array:
        new += ','.join(str(j) for j in elem) + '\n'
    print(new[:-1])


to_csv_text([
            [0, 1, 2, 3, 45],
            [10, 11, 12, 13, 14],
            [20, 21, 22, 23, 24],
            [30, 31, 32, 33, 34]])


def to_csv_text_2(array):
    print('\n'.join(','.join(map(str, line)) for line in array))


to_csv_text_2([
            [0, 1, 2, 3, 45],
            [10, 11, 12, 13, 14],
            [20, 21, 22, 23, 24],
            [30, 31, 32, 33, 34]
        ])

# ROT13


def rot13(message):
    abc = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM'
    r = ''
    for c in message:
        if c in abc:
            r += abc[abc.index(c) + 13]
        else:
            r += c
    return r


tuple_1 = (1, 2, 3)
tuple_2 = (4, 5, 6)
tuple_3 = tuple_1 + tuple_2
print(tuple_3)
print(tuple_1 < tuple_2)
