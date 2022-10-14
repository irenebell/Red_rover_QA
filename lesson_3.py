# task 1
my_list = ['a', 'b', [1, 2, 3], 'd']

print(*my_list[2])

# task 2

list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]

result = filter(lambda x: isinstance(x, int), list_1)
print(sum(result))

filtered = [x for x in list_1 if type(x) == int]
print(sum(filtered))
summa = 0
for i in list_1:
    if type(i) == int:
        summa += i
print(summa)


for item in list_1:
    if type(item) == str and 'a' in item:
        print(item)

# task 3

my_list = ['cat', 'dog', 'horse', 'cow']
print(tuple(my_list))

# task 4

family_1 = input('Enter your family: ').split(',')
family_2 = input('Enter your family: ').split(',')
if len(family_1) > len(family_2):
    print(f'{family_1} family_1 is bigger')
elif len(family_2) > len(family_1):
    print(f'{family_2} family_2 is bigger')
else:
    print('Equal')

# task 5

film = {
    'title': 'Sun',
    'director': 'Strow',
    'year': 1980,
    'budget': 1000000,
    'main_actor': 'Josh',
    'slogan': 'The best'
}

print(film.keys())
print(film.values())
print(film.items())

# task 6

my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}

print(sum(my_dictionary.values()))

# task 7

list_1 = [1, 2, 3, 4, 5, 3, 2, 1]
list_2 = list(set(list_1))

print(list_2)

# task 8

set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}

print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.difference(set1))
print(set1.issubset(set2))
print(set2.issubset(set1))


# ****************************


# enumerate

my_tuple = (1, 'name', 25, True, 'tree', 57)

for (index, item) in enumerate(my_tuple):
    print(index, item)

list_1 = [1, 5, 4, 21, 97, 3, 78]
print(sorted(list_1))
list_1.sort()
print(list_1)
list_2 = sorted(list_1, reverse=True)
print(list_2)

# list compehension

new_list = [x * x for x in list_1]
print(new_list)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

new_2 = []
for x in list_1:
    if x % 2 == 0:
        new_2.append(x * x)
print(new_2)

dict_1 = {}
for i in range(len(list_1)):
    dict_1[i] = list_1[i]
print(dict_1)
print(*dict_1)

for key in dict_1.keys():
    print(key)

for value in dict_1.values():
    print(value)

for item in dict_1.items():
    print(item)

for key, value in dict_1.items():
    print(key, value)

print(dict_1.get(3))  # 3 - key


# поменять местами слова


def name_shuffler(str_):
    return ' '.join(str_.split(' ')[::-1])


def double_char(s):
    return ''.join(list(map(lambda x: x * 2, s)))


def double_chars(s):
    return ''.join(x * 2 for x in s)


def reverse_seq(n):
    return [x for x in range(n, 0, -1)]


def invert(lst):
    return [x * -1 for x in lst]


def nth_even(n):
    return (n - 1) * 2


def merge_arrays(arr1, arr2):
    return list(sorted(set(arr1 + arr2)))
