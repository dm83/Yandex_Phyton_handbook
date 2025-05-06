# Задача A
word_count = 2 #int(input())
lst = []

for _ in range(word_count):
    word = str(input())
    lst.append(word[0] in 'абв')
    
if all(lst):
    print('YES')
else:
    print('NO')


# Задача B
word = list(input())
for letter in word:
    print(letter)


# Задача C
title_lenght = 25 # int(input())
title_count = 3 #int(input())

for _ in range(title_count):
    text = input()
    if len(text) >= (title_lenght - 3):
        text = text[:(title_lenght - 3)]
        print(text.ljust(title_lenght, '.'))
    else:
        print(text)
    
"""
Мое решение не проходит проверку на третьем шаге..
Решение с сайта:
"""
length = int(input())
count = int(input())

for _ in range(count):
    string = input()
    if len(string) <= length:
        print(string)
    else:
        print(f'{string[:length - 3]}...')


# Задача D
while text := input():

    if text.endswith('@@@'):
        pass
    elif text.startswith('##'):
        print(text[2:])
    else:
        print(text)


# Задача E
text = 'aнна'
if text == text[::-1]:
    print('YES')
else:
    print('NO')


# Задача F
text = 'березка елочка зайка волк березка'
num_count = 3
counter = 0

for _ in range(num_count):
    text_lst = input().split(' ')
    for w in text_lst:
        if w == 'зайка':
            counter += 1

print(counter)


# Задача G
numbers = input()
a, b = numbers.split(' ')
print(f"{int(a) + int(b)}")


# Задача H
count = int(input())
target = 'зайка'

for _ in range(count):
    text = input()
    if target in text:
        print(text.index(target) + 1)
    else:
        print('Заек нет =(')


# Задача I
"""
Мое решение тренажер не принимает по непонятной причине.
"""
while text := input():
    if text.startswith('#'):
        pass
    else:
        print(text[:text.index('#')])
"""
Решение с сайта
"""
while string := input():
    if not (pos := string.find('#')) + 1:
        print(string)
    elif string[:pos]:
        print(string[:pos])




# Задача J 
text = ''
while (string := input()) != 'ФИНИШ':
    text += string.lower().replace(' ', '')

unique_letter = []
for char in text:
    if char not in unique_letter:
        unique_letter.append(char)

most_frequent_char = ''
max_count = 0
for letter in unique_letter:
    letter_count = 0
    for char in text:
        if letter == char:
            letter_count += 1
    
    if letter_count > max_count:
        most_frequent_char = letter
        max_count = max(max_count, letter_count)
print(most_frequent_char)


# Задача K
count = int(input())

text_list = []
for _ in range(count):
    text_list.append(input())

target = input().lower()

for titles in text_list:
    if target in titles.lower():
        print(titles)



# Задача L
"""
Мое решение - зачтено
"""
count = int(input())
list_of_dishes = ('Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая')

num_of_round = count // 5
res_round = count % 5

if num_of_round > 0:
    for _ in range(num_of_round):
        for dishes in list_of_dishes:
            print(dishes)
if res_round > 0:
    for i in range(res_round):
        print(list_of_dishes[i])
"""
Решение с задачника
"""
porridges = ['Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая']

days = 12
for day in range(days):
    print(porridges[day % len(porridges)])

# Задача M
count = int(input())
list_of_numbers = []
for _ in range(count):
    list_of_numbers.append(int(input()))
power = int(input())

for num in list_of_numbers:
    print(num ** power)


# Задача N
"""
Мое решение - зачтено
"""
list_of_numbers = input().split(' ')
power = int(input())
output_list = []
for num in list_of_numbers:
    output_list.append(str(int(num) ** power))
print(' '.join(output_list))

"""
Решение с задачника
"""
numbers = []
string = input()
power = int(input())
numbers = string.split()
for number in numbers:
    print(int(number) ** power, end=' ')


# Задача O
"""
Решение с задачника (алгоритм Эвклида)
"""
string = input().split(' ')

numbers = []
for num in string:
    numbers.append(int(num))

gcd = numbers[0]
for number in numbers:
    while number: 
        gcd, number = number, gcd % number
print(gcd)


# Задача P
"""
Решение с сайта, я даже не могу толком понять что от меня хотят..
"""
length = int(input())

newline = '\n'
header = ''
newlines = []

for _ in range(stings_number := int(input())):
    header += input() + newline

header.strip('\n')

for pos in range(len(header)):
    if header[pos] == newline:
        newlines.append(pos)

header = header.replace(newline, "")

if len(header) > length:
    header = header[:length - 3] + '...'

for pos in newlines:
    if (header[-3:] != '...') or (length - pos >= 4):
        header = header[:pos] + newline + header[pos:]
        length += 1

print(header)


# Задача Q
string = input().lower().replace(' ', '')
if string == string[::-1]:
    print('YES')
else:
    print('NO')


# Задача R
string = '010000100001111111110111110000000000000011111111'
counter = 1

if len(string) == 1:
    print(string, counter)
else:
    for i in range(1, len(string)):
        a, b = string[i], string[i - 1]
        if a == b:
            counter += 1
        else:
            print(f"{b} {counter}")
            counter = 1
    print(f"{string[-1]} {counter}")

# Задача S
"""
Решение с сайта, я даже не могу толком понять что от меня хотят..
"""
string = input()
tokens = string.split(' ')

stack = []

while tokens != []:
    value = tokens.pop(0)
    if value.isdigit():
        stack.append(int(value))
    else:
        match value:
            case '+':
                stack.append(stack.pop() + stack.pop())
            case '-':
                stack.append(stack.pop(-2) - stack.pop())
            case '*':
                stack.append(stack.pop() * stack.pop())
            case '/':
                stack.append(stack.pop(-2) / stack.pop())

print(stack[-1])


# Задача T
"""
Решение с сайта, я даже не могу толком понять что от меня хотят..
"""
expression = input()
tokens = expression.split()

uno = ['~', '#', '!']
duo = ['+', '-', '*', '/']
trio = ['@']
operators = uno + duo + trio

stack = []

while tokens != []:
    token = tokens.pop(0)
    if token in uno:
        a = stack.pop()
        match token:
            case '~':
                stack.append(-a)
            case '!':
                res = 1
                for i in range(1, a + 1):
                    res *= i
                stack.append(res)
            case '#':
                stack.append(a)
                stack.append(a)
    elif token in duo:
        a = stack.pop()
        b = stack.pop()
        match token:
            case '+':
                stack.append(b + a)
            case '-':
                stack.append(b - a)
            case '*':
                stack.append(b * a)
            case '/':
                stack.append(b // a)
    elif token in trio:
        a = stack.pop()
        b = stack.pop()
        c = stack.pop()
        match token:
            case '@':
                stack.append(b)
                stack.append(a)
                stack.append(c)
    else:
        stack.append(int(token))

print(int(stack[-1]))