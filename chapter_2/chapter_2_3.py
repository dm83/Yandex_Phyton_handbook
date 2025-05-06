# задача A
while input() != 'Три!':
    print('Режим ожидания...')
print('Ёлочка, гори!')


# задача B
count = 0

while (s := input()) != 'Приехали!':
    if 'зайка' in s:
        count += 1
print(count)


# задача C
start = int(input())
end = int(input())
for i in range(start, end + 1, 1):
    print(i, end=' ')


# задача D
start = int(input())
end = int(input())
if end < start:
    for i in range(start, end - 1, -1):
        print(i, end=' ')
else:
    for i in range(start, end + 1, 1):
        print(i, end=' ')


# задача E
result = 0

while check := float(input()):
    if check >= 500:
        result += check * 0.9
    else:
        result += check
print(result)


# задача F
a = 12
b = 0

while b:
    a, b = b, a % b

print(a)


# задача G
a = 2
b = 8
p = a * b

while b:
    a, b = b, a % b
res = p / a
print(int(res))

# задача H
a = input()
b = int(input())

for _ in range(b):
    print(a)


# задача I
factorial = 1

for i in range(1, int(input()) + 1):
    factorial *= i

print(factorial)


# задача J
a = 0
b = 0

while (direction := input()) != "СТОП":
    steps = int(input())
    
    match direction:
        case 'СЕВЕР':
            a += steps
        case 'ЮГ':
            a -= steps
        case 'ЗАПАД':
            b -= steps
        case 'ВОСТОК':
            b += steps

print(a)
print(b)


# задача K
num = 123
s = 0

while num:  # while num != 0:
    s += num % 10
    num = num // 10

print(s)


# задача L
num = 123
s = 0
max_val = 0

while num:
    s = num % 10
    if max_val < s:
        max_val = s
    num //= 10

print(max_val)


# задача M
n = int(input())
result = '\u1000'

for _ in range(n):
    name = str(input())

    if name < result:
        result = name

print(result)


# задача N
n = int(input())
prime = ''
count = 1

if n <= 1:
    prime = False
else:
    for div in range(2, n // 2 + 1): # тут заморочка с симметрией делителей надо отдельно изучить (см. подсказки)
        if n % div == 0:
            prime = False
            break
        else:
            prime = True
        
if prime:
    print('YES')
else:
    print('NO')


# задача O
n = int(input())
count = 0

for _ in range(n):
    text = str(input())
    if 'зайка' in text:
        count += 1

print(count)


# задача P
num = str(input())

if num == num[::-1]:
    print('YES')
else:
    print('NO')


# задача Q
n = 123
out = ''

while n:
    res = n % 10
    if res % 2 != 0:
        out += str(res)
    n //= 10 

print(out[::-1])


# задача R
num = 36
out = ''
i = 0

if num < 2:
    print(num)
else:

    while num > 2:
        for div in range(2, num + 1):
            if not num % div:
                num //= div
                print(div, end='')
                if num > 1:
                    print(' * ', end='')
                break


# задача S
num = 231
min, max = 1, 1000
attemts = 10

while attemts < 11:
     guess = (min + max) // 2
     if num > guess:
         min = guess + 1
         print('Больше')
     elif num < guess:
         max = guess - 1
         print('Меньше')
     elif num == guess:
         print('Угадал')
         break

"""
Решение взял с сайта https://reshebnik.mumuproject.com/frontpage/yandex-python-handbook/yandex-python-2-3-cikly/yandex-handbook-igra-v-ugadayku/
мое решение ниже, не так понял задачу (бинарный поиск)
"""
begin, end = 1, 1001
ask = (begin + end) // 2
print(ask)

while (answer := input()) != 'Угадал!':
    if answer == 'Меньше':
        end = (begin + end) // 2
    elif answer == 'Больше':
        begin = (begin + end) // 2
    ask = (begin + end) // 2
    print(ask)


# задача T
"""
Решение взял с сайта https://reshebnik.mumuproject.com/frontpage/yandex-python-handbook/yandex-python-2-3-cikly/yandex-handbook-haypanem-nemnozhko/
"""
q = int(input())

last_hash = 0
err = 0
is_error = False

for i in range(q):
    block = int(input())
    current_hash = block % 256
    r = (block // 256) % 256
    m = block // 256 ** 2
    new_hash = (37 * (m + r + last_hash)) % 256
    if new_hash != current_hash or new_hash >= 100:
        if is_error is False:
            err = i
            is_error = True
    last_hash = current_hash

if is_error is False:
    print(-1)
else:
    print(err)