# Задача A
string = input()
letters = set(string)
output = ''
for char in letters:
    output += char
print(output)

"""
Решение с сайта
"""
string = set(input())
for char in string:
    print(char, end='')


# Задача B 
word_1 = set(input())
word_2 = set(input())

set_intersect = word_1.intersection(word_2)
for char in set_intersect:
    print(char, end='')


# Задача C
count = int(input())

unique_place = set()
for _ in range(count):
    unique_place |= set(input().split(' '))

for word in unique_place:
    print(word)


# Задача D
m = int(input())
o = int(input())

m_last_name = []
o_last_name = []

for _ in range(m):
    m_last_name.append(input())

for _ in range(o):
    o_last_name.append(input())

ov_last_name = set(m_last_name) & set(o_last_name)
count = len(ov_last_name)
if count > 0:
    print(count)
else:
    print('Таких нет')


# Задача E
"""
Решение с сайта
"""
m = int(input())
o = int(input())

m_last_name = []
o_last_name = []

for _ in range(m):
    m_last_name.append(input())

for _ in range(o):
    o_last_name.append(input())

ov_last_name = set(m_last_name) & set(o_last_name)
count = len(ov_last_name)
if count > 0:
    print(count)
else:
    print('Таких нет')


# Задача F
"""
Решение с сайта
"""
list1size = int(input())
list2size = int(input())

list1 = set()
list2 = set()


for _ in range(list1size + list2size):
    eater = input()
    if eater in list1:
        list2.add(eater)
    else:
        list1.add(eater)

# print(list1, list2)

if len(junction := (list1 ^ list2)) != 0:
    for eater in sorted(junction):
        print(eater)
else:
    print('Таких нет')



# Задача G
morze_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
        'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----',
        '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

string = input()
for word in string.split(' '):
    for char in word:
        print(morze_dict[char.upper()], end=' ')
    print()
        


# Задача H
"""
Мое решение (недоделанное)
"""
count = int(input())
dict = {}

for i in range(count):
    key, value = input().split(' ')
    dict[key] = value

target = input()
for k, v in dict.items():
    if k == target:
        print(v)

"""
Решение с сайта
"""
porridge_eaters = {}

for _ in range(int(input())):
    string = input()
    eater, *porridges = string.split()
    porridge_eaters[eater] = porridges

porridge = input()

names = []

for name in porridge_eaters:
    if porridge in porridge_eaters[name]:
        names.append(name)

if not names:
    print('Таких нет')
else:
    names.sort()
    for name in names:
        print(name)

"""
Второе решение с сайта здесь хорошее решение 
заполнения списка с использованием метода get()
"""
porridges_list = {}

for _ in range(int(input())):
    string = input()
    eater, *porridges = string.split()
    for porridge in porridges:
        porridges_list[porridge] = porridges_list.get(porridge, []) + [eater]

porridge = input()

if porridge in porridges_list:
    print('\n'.join(sorted(porridges_list[porridge])))
else:
    print('Таких нет')

# Задача I
objects = dict()

while (string := input()) != '':
    words = string.split()
    for item in words:
        if item in objects:
            objects[item] += 1
        else:
            objects[item] = 1
            
for item in objects:
    print(item, objects[item])


# Задача
"""
Решение с сайта
"""
TRANSLITERATE_DICT = {
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
    'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M',
    'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
    'Ф': 'F', 'Х': 'KH', 'Ц': 'TC', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH',
    'Ы': 'Y', 'Э': 'E', 'Ю': 'IU', 'Я': 'IA', 'Ь': '', 'Ъ': ''
}


result = ''

text = input()

for char in text:
    char_copy = char.upper()
    if char_copy in TRANSLITERATE_DICT:
        if char.isupper():
            char = TRANSLITERATE_DICT[char_copy].capitalize()
        else:
            char = TRANSLITERATE_DICT[char_copy].lower()
    result += char

print(result)


# Задача K
count = int(input())

lname_dict = {}
for _ in range(count):
    last_name = input()
    lname_dict[last_name] = lname_dict.get(last_name, 0) + 1

count = 0
for value in lname_dict.values():
    if value > 1:
        count += value
print(count)

# Задача L
count = int(input())

lname_dict = {}
for _ in range(count):
    last_name = input()
    lname_dict[last_name] = lname_dict.get(last_name, 0) + 1

lname_dict = dict(sorted(lname_dict.items()))

printed = False
for name in lname_dict:
    if lname_dict[name] > 1:
        print(f"{name} - {lname_dict[name]}")
        printed = True

if not printed:
    print('Однофамильцев нет')


# Задача M
porridges = set()

for _ in range(int(input())):
    if (porridge := input()) not in porridges:
        porridges.add(porridge)

for _ in range(int(input())):
    for _ in range(int(input())):
        if (porridge := input()) in porridges:
            porridges.remove(porridge)

menu = sorted(porridges)
if not menu:
    print('Готовить нечего')
else:
    for porridge in menu:
        print(porridge)

# Задача N 
products = []
recipes = {}
menu = []

for _ in range(int(input())):
    products.append(input())

for _ in range(int(input())):
    name = input()
    ingredients = []
    for _ in range(int(input())):
        ingredients.append(input())
    recipes[name] = recipes.get(name, []) + ingredients

for name in recipes:
    if (set(recipes[name]) & set(products) == set(recipes[name])):
        menu.append(name)

if menu:
    menu.sort()
    for name in menu:
        print(name)
else:
    print('Готовить нечего')


# Задача O
"""
Функции перевода числа в СС до 10 и обратно
"""
def converter(num, base):
    if num == 0:
        return '0'
    bit = ''
    while num > 0:
        bit = str(num % base) + bit
        num //= base
    return bit

def to_decimal(num, base):
    result = 0
    for digit in num:
        result = result * base + int(digit)
    return result
to_decimal('101', 2)

"""
Решение с сайта
"""
numbers = input().split()
total = []
result = dict()

for item in numbers:
    units = zeros = 0
    number = f'{int(item):b}'

    result['digits'] = len(number)
    result['units'] = number.count('1')
    result['zeros'] = number.count('0')
    total.append(result.copy())

print(total)


# Задача P
"""
Мое решение (что-то не так)
"""
places = set()
target = 'зайка'

while string := input():
    string = string.split(' ')
    if target in string:
        ind = string.index(target)
        # если цель - первый элемент
        if ind == 0:
            places.add(string[ind + 1])
        # если цель - последний элемент
        elif ind == (len(string)):
            places.add(string[ind - 1])
        # если цель - внутри строки
        else:
            places.add(string[ind + 1])
            places.add(string[ind - 1])
    else:
        pass

for place in places:
    print(place)
"""
Решение с сайта
"""
subject = 'зайка'
objects = []

while (nature := input().split()) != []:
    if len(nature) > 1 and subject in nature:
        for pos in range(length := len(nature)):
            if nature[pos] == subject:
                if pos == 0:
                    objects.append(nature[1])
                elif pos == (length - 1):
                    objects.append(nature[-2])
                else:
                    objects.append(nature[pos - 1])
                    objects.append(nature[pos + 1])

for item in set(objects):
    print(item)

# Задача Q
"""
Решение с сайта (до конца не понял задачу - сложная)
"""
friends = {}  # словарь прямых друзей

while pair := input():
    friend1, friend2 = pair.split()
    friends[friend1] = friends.get(friend1, set()) | set([friend2])
    friends[friend2] = friends.get(friend2, set()) | set([friend1])

friends_of_friends = {}  # словарь друзей друзей

for name in sorted(friends):
    for person in friends[name]:
        friends_of_friends[name] = friends_of_friends.get(
            name, set()) | friends[person]

for name in friends_of_friends:
    friends_of_friends[name].discard(name)  # удаляем самого себя
    friends_of_friends[name] -= friends[name]  # удаляем прямых друзей

    friends_of_friends[name] = sorted(friends_of_friends[name])

    print(f'{name}: {", ".join(friends_of_friends[name])}')


# Задача R
"""
Решение с сайта
"""
treasures = dict()

for _ in range(count := int(input())):
    x, y = input().split()
    index = (int(x) // 10, int(y) // 10)
    treasures[index] = treasures.get(index, 0) + 1

print(max(treasures.values()))


# Задача S
"""
Решение с сайта
"""
toys = []
unique = []

for _ in range(int(input())):
    name, str = input().split(': ')
    toys.extend(set(str.split(', ')))  

for i in range(len(toys)):
    toy = toys.pop(0)
    if toy not in toys:
        unique.append(toy)
    toys.append(toy)

print('\n'.join(sorted(unique)))


# Задача T
items = set(input().split('; '))

numbers = []

for item in items:
    numbers.append(int(item))

numbers.sort()

for num1 in numbers:
    mutually = []
    for num2 in numbers:
        if num1 != num2:
            a, b = num1, num2
            while b != 0:
                a, b = b, a % b
            if a == 1:
                mutually.append(str(num2))
    if mutually:
        print(num1, '-', ", ".join(mutually))