# задача A
n = 121

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i * j, end=' ')
    print()
      

# задача B
n = 3

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f'{j} * {i} = {i * j}')

# задача C
max_number = 133
number = 1
row = 0

while number <= max_number:
    row += 1
    col = 1
    while col <= row and number <= max_number:
        print(number, end=' ')
        col += 1
        number += 1
    print()
    

# задача D
max_iters = 2

iter = 1
sum1 = 0

while iter <= max_iters:
    iter += 1
    number = int(input())
    sum2 = 0

    while number:
        sum2 += number % 10
        number = number // 10
    sum1 += sum2

print(sum1)


# задача E
max_iters = 2
iter = 1
count = 0

while iter <= max_iters:
    found = False
    
    while (word := input()) != 'ВСЁ':
        if word == 'зайка':
            found = True

    if found:
        count += 1
    iter += 1

print(count)


# задача F
max_number = int(input())
i = 1

while i < max_number:
    if i == 1:
        a = int(input())
            
    b = int(input())
    while b:
        a, b = b, a % b
    i += 1

print(a)

# задача G
num = 3

for i in range(1, num + 1):
    max_count = 3 + i
    for j in range(max_count - 1, 0, -1):
        print(f'До старта {j} секунд(ы)')
    print(f'Старт {i}!!!')


# задача H
count = 2
max_sum = 0
max_sum_name = None

for i in range(count):
    name, number = input(), int(input())
    number_sum = 0

    while number > 0:
        number_sum += number % 10
        number //= 10
        
    if number_sum > max_sum:
        max_sum = number_sum
        max_sum_name = name
    elif number_sum == max_sum:
        max_sum_name = name
        
print(max_sum_name)



# задача I
num_count = 2
i = 0

while i < num_count:
    max_val = 0
    a = int(input())
    while a:
        v = a % 10
        if max_val < v:
            max_val = v
        a //= 10
    print(max_val, end='')
    
    i += 1


# задача J
juice_count = 3 # int(input())

print('А Б В')
for i in range(1, juice_count + 1):
    for j in range(1, juice_count + 1):
        for k in range(1, juice_count + 1):
            if (i + j + k) == juice_count:
                print(i, j, k, sep=' ')


# задача K
num_count = int(input())
counter = 0

for _ in range(num_count):
    num = int(input())
    prime = True
    
    if num < 2:
        prime = False
    elif num == 2:
        prime = True
    else:
        for div in range(2, num):
            if num % div == 0:
                prime = False
                break
    if prime:
        counter += 1

print(counter)

# задача L
rows = 6 #int(input())
cols = 5 #int(input())
n = 0
cell_width = len(str(rows * cols))
for _ in range(rows):
    for _ in range(cols):
        print(f"{n + 1:>{cell_width}}", end=' ')
        n += 1
    print()

# задача M
"""
Решение с сайта, уже лень было выводить формулу значения
"""
height = int(input())
width = int(input())

cell_width = len(str(height * width))

for i in range(1, height + 1):
    for j in range(i, i + height * (width - 1) + 1, height):
        print(f'{j:>{cell_width}}', end=' ')
        if j == i + height * (width - 1):
            print()


# задача N
"""
Решение с сайта, уже лень было выводить формулу значения
"""
height = int(input())
width = int(input())

ceil_width = len(str(width * height))

if height > 0 and width > 0:
    for row in range(height):
        for column in range(width):
            if (row % 2) == 0:
                num = row * width + column + 1
            else:
                num = (row + 1) * width - column
            print(f'{num:>{ceil_width}}', end=' ')
        print()


# задача O
"""
Решение с сайта, уже лень было выводить формулу значения
"""
height = int(input())
width = int(input())

ceil_width = len(str(width * height))

for row in range(height):
    for column in range(width):
        if column % 2 == 0:
            num = column * height + row + 1
        else:
            num = (column + 1) * height - row
        print(f'{num:>{ceil_width}}', end=' ')
    print()


# задача P
"""
Решение с сайта, уже лень было выводить формулу значения
"""
size = int(input())
ceil_width = int(input())

string_length = size * ceil_width + (size - 1)

for row in range(size):
    for column in range(size):
        print(f'{((row + 1) * (column + 1)): ^{ceil_width}}', end='')
        if column == size - 1:
            print()
        else:
            print('|', end='')
    if row + 1 != size:
        print('-' * string_length)


# задача Q
num_count = 3 #int(input())
counter = 0

for _ in range(num_count):

    num = int(input())
    if num == int(str(num)[::-1]):
        counter += 1

print(counter)


# задача R
"""
Мое решение (не доделал)
"""
max_num = 17
start = 0
end = 1
sum = 0
check = True
max_row = 1

# разрядность максимального числа
lenght_counter = 0
while max_num:
    lenght_counter += 1
    max_num //= 10

# находим номер строки где находится число
for row in range(0, max_num + 1):
    print()
    if row == 0:
        start, end = 0, 1
        if (max_num >= start) and (max_num <= end):
            max_row = row
            break
    else:
        start, end = end + 1,  end + row + 1
        for i in range(start, end + 1):
            if (max_num >= start) and (max_num <= end):
                max_row = row
                break

# заполняем елочку
for row in range(0, max_num + 1):
    print()
    if row == 0:
        start, end = 0, 1
        print(end, end=' ')
        
    else:
        start, end = end + 1,  end + row + 1
        for i in range(start, end + 1):
            print(i, end=' ')
    

"""
Решение с сайта
"""
limit = int(input())

counter = 0
width = 1
max_length = 0

while counter <= limit:
    string_length = 0
    for position in range(width):
        counter += 1
        if counter <= limit:
            string_length += len(str(counter))
        if position < width - 1 and counter < limit:
            string_length += 1

    if max_length < string_length:
        max_length = string_length

    width += 1

counter = 0
width = 1

while counter <= limit:
    string = ''
    for position in range(width):
        counter += 1
        if counter <= limit:
            string += str(counter)
        if position < width - 1 and counter < limit:
            string += ' '
    width += 1
    print(f'{string:^{max_length}}')


# задача S
size = int(input())

cell_width = len(str((size + 1) // 2))

for i in range(size):
    for j in range(size):
        print(f'{min(i + 1, j + 1, size - i, size - j):>{cell_width}}', end=' ')
    print()



# задача T
number = int(input())

best_value = 0
best_base = 0

for base in range(10, 1, -1):
    summa = 0
    num = number
    while num > 0:
        summa += (num % base)
        num //= base
    if summa >= best_value:
        best_value = summa
        best_base = base



