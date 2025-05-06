# match
color = input()
match color:
    case 'красный' | 'жёлтый':
        print('Стоп.')
    case 'зелёный':
        print('Можно ехать.')
    case _:
        print('Некорректное значение.')

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
        
# fibonachi series less than n
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(10)

# задача A
print('Как Вас зовут?')
name = input()
print(f"Здравствуйте, {name}! \nКак дела?")
status = input()
if status == 'хорошо':
    print('Я за вас рада!')
else:
    print('Всё наладится!')

# задача B
speed1 = int(input())
speed2 = int(input())
distance = 43872
time1 = distance / speed1
time2 = distance / speed2
if time1 > time2:
    print('Вася')
else:
    print('Петя')

# задача C
speed1 = int(input())
speed2 = int(input())
speed3 = int(input())
distance = 43872
time1 = distance / speed1
time2 = distance / speed2
time3 = distance / speed3
if time1 < time2 and time1 < time3:
    print('Петя')
elif time2 < time1 and time2 < time3:
    print('Вася')
elif time3 < time1 and time3 < time2:
    print('Толя')
else:
    print('Где-то ошибка!')
print(f"1. Петя\n2. Валя\n3. Толя")

# задача D
speed1 = int(input())
speed2 = int(input())
speed3 = int(input())
distance = 43872
time1 = distance / speed1
time2 = distance / speed2
time3 = distance / speed3
if time1 < time2 and time1 < time3:
    if time2 < time3:
        print(f"1. Петя\n2. Вася\n3. Толя")
    else:
        print(f"1. Петя\n2. Толя\n3. Вася")
elif time2 < time1 and time2 < time3:
    if time1 < time3:
        print(f"1. Вася\n2. Петя\n3. Толя")
    else:
        print(f"1. Вася\n2. Толя\n3. Петя")
elif time3 < time1 and time3 < time2:
    if time1 < time2:
        print(f"1. Толя\n2. Петя\n3. Вася")
    else:
        print(f"1. Толя\n2. Вася\n3. Петя")
else:
    print('Где-то ошибка!')

# задача E

N = int(input())
M = int(input())
petya = 6 + N
vasya = 12 + M
if petya > vasya:
    print('Петя')
else:
    print('Вася')

# задача F
year = int(input())
if year % 4 != 0:
    print('NO')
elif year % 100 == 0:
    if year % 400 == 0:
        print('YES')
    else:
        print('NO')
else:
    print('YES')

# задача G
number = int(input())
first = number // 1000
second = number // 100 % 10
third = number // 10 % 10
fourth = number % 10
rev_number = int(str(fourth) + str(third) + str(second) + str(first))
if number == rev_number:
    print('YES')
else:
    print('NO')

# задача H
text = 'березка елочка зайка волк березка'
if 'зайка' in text:
    print('YES')
else:
    print('NO')

# задача I
n1 = 'Аня'
n2 = 'Аня'
n3 = 'Вася'
if n1 < n2 and n1 < n3:
    print(n1)
elif n2 < n1 and n2 < n3:
    print(n2)
elif n3 < n1 and n3 < n2:
    print(n3)

# задача J
number = int(input())
first = number // 100
second = number // 10 % 10
third = number % 10
n1 = first + second
n2 = second + third
if n1 > n2:
    print(int(str(n1) + str(n2)))
else:
    print(int(str(n2) + str(n1)))

# задача K
number = int(input())
number = 135
first = number // 100
second = number // 10 % 10
third = number % 10
min_val = min(first, second, third)
max_val = max(first, second, third)
if first != min_val and first != max_val:
    if first * 2 == (min_val + max_val):
        print('YES')
    else:
        print('NO')
elif second != min_val and second != max_val:
    if second * 2 == (min_val + max_val):
        print('YES')
    else:
        print('NO')
elif third != min_val and third != max_val:
    if third * 2 == (min_val + max_val):
        print('YES')
    else:
        print('NO')
else:
    print('NO')

# задача L
a = int(input())
b = int(input())
c = int(input())
a_check = a < (b + c)
b_check = b < (a + c)
c_check = c < (a + b)
check = a_check and b_check and c_check
if check is True:
    print('YES')
else:
    print('NO')

# задача M
a = int(input())
b = int(input())
c = int(input())
a, b, c = [12, 13, 14]
a1 = a // 10
a2 = a % 10
b1 = b // 10
b2 = b % 10
c1 = c // 10
c2 = c % 10
check1 = a1 == b1 == c1
check2 = a2 == b2 == c2
if check1 is True:
    print(a1)
elif check2 is True:
    print(a2)
else:
    print('error')

# задача N
number = 103
n1 = number // 100
n2 = number // 10 % 10 
n3 = number % 10
v1 = int(str(n1) + str(n2))
v2 = int(str(n1) + str(n3))
v3 = int(str(n2) + str(n1))
v4 = int(str(n2) + str(n3))
v5 = int(str(n3) + str(n1))
v6 = int(str(n3) + str(n2))
min_val, max_val = 1000, 0
if v1 // 10 != 0:
    min_val = min(min_val, v1)
    max_val = max(max_val, v1)
if v2 // 10 != 0:
    min_val = min(min_val, v2)
    max_val = max(max_val, v2)
if v3 // 10 != 0:
    min_val = min(min_val, v3)
    max_val = max(max_val, v3)
if v4 // 10 != 0:
    min_val = min(min_val, v4)
    max_val = max(max_val, v4)
if v5 // 10 != 0:
    min_val = min(min_val, v5)
    max_val = max(max_val, v5)
if v6 // 10 != 0:
    min_val = min(min_val, v6)
    max_val = max(max_val, v6)
print(min_val, max_val)

# задача O
number1 = 31
number2 = 11
v1 = number1 // 10
v2 = number1 % 10
v3 = number2 // 10
v4 = number2 % 10
max_val = max(v1, v2, v3, v4)
min_val = min(v1, v2, v3, v4)
other_vals = (v1 + v2 + v3 + v4 - min_val - max_val) % 10
super_val = str(max_val) + str(other_vals) + str(min_val)
print(int(super_val))

# задача P
p = 100
v = 15
t = 27
first, second, third = '', '', ''
max_val = max(p, v, t)
min_val = min(p, v, t)
middle = (p + v + t) - max_val - min_val
if p == middle:
    if v == max_val:
        first = 'Вася'
        second = 'Петя'
        third = 'Толя'
    else:
        first = 'Толя'
        second = 'Петя'
        third = 'Вася'
if v == middle:
    if p == max_val:
        first = 'Петя'
        second = 'Вася'
        third = 'Толя'
    else:
        first = 'Толя'
        second = 'Вася'
        third = 'Петя'
if t == middle:
    if p == max_val:
        first = 'Петя'
        second = 'Толя'
        third = 'Вася'
    else:
        first = 'Вася'
        second = 'Толя'
        third = 'Петя'
print(f"  {first:^20}  \n  {second:<20}  \n  {third:>20}  \n   II      I      III   ")

# задача Q
a = 1
b = 1
c = 1
root_cond1 = (a == 0) and (b == 0) and (c != 0)
root_cond2 = (a == 0) and (b != 0) and (c == 0)
root_cond3 = (a == 0) and (b == 0) and (c == 0)
root_cond4 = (a == 0) and (b != 0) and (c != 0)
dscr = b ** 2 - (4 * a * c)
if root_cond1 is True:
    print('No solution')
elif root_cond2 is True:
    print(0)
elif root_cond3 is False:
    if root_cond4 is True:
        x1 = (-c / b)
        print(f"{x1:.2f}")
    elif dscr > 0:
        x1 = (-b + (dscr ** 0.5)) / (2 * a)
        x2 = (-b - (dscr ** 0.5)) / (2 * a)
        min_root = min(x1, x2)
        max_root = max(x1, x2)
        print(f"{min_root:.2f} {max_root:.2f}")
    elif dscr == 0:
        x1 = (-b) / (2 * a)
        print(f"{x1:.2f}")
    else:
        print('No solution')
else:
    print('Infinite solutions')

# задача R
a, b,c  = 6, 3, 4
ang1, ang2, ang3 = ''
# angle1
summ = a**2 + b**2
if summ > c**2:
    ang1 = 'острый'
elif summ == c**2:
    ang1 = 'прямой'
else:
    ang1 = 'тупой'
# angle2
summ = c**2 + b**2
if summ > a**2:
    ang2 = 'острый'
elif summ == a**2:
    ang2 = 'прямой'
else:
    ang2 = 'тупой'
# angle3
summ = a**2 + c**2
if summ > b**2:
    ang3 = 'острый'
elif summ == b**2:
    ang3 = 'прямой'
else:
    ang3 = 'тупой'
# проверка типа треугольника:
tupoy = (ang1 == 'тупой') or (ang2 == 'тупой') or (ang3 == 'тупой')
pryamoy = (ang1 == 'прямой') or (ang2 == 'прямой') or (ang3 == 'прямой')
if tupoy is True:
    print('велика')
elif pryamoy is True:
    print('100%')
else:
    print('крайне мала')

# задача S
x = float(input())
y = float(input()) 
if (x ** 2 + y ** 2) ** 0.5 > 10:
    print('Вы вышли в море и рискуете быть съеденным акулой!')
elif x >= 0 and y >= 0 and (x ** 2 + y ** 2) ** 0.5 <= 5:
    print('Опасность! Покиньте зону как можно скорее!')
elif -4 <= x < 0 and 0 <= y <= 5:
    print('Опасность! Покиньте зону как можно скорее!')
elif -7 <= x < -4 and 0 <= y <= 5 and (5 * x - 3 * y) > -35:
    print('Опасность! Покиньте зону как можно скорее!')
elif (0.25 * x ** 2 + 0.5 * x - 9) <= y <= 0:
    print('Опасность! Покиньте зону как можно скорее!')
else:
    print('Зона безопасна. Продолжайте работу.')

# задача T
nature1 = input()
nature2 = input()
nature3 = input()

if nature1 > nature2:
    nature1, nature2 = nature2, nature1
if nature1 > nature3:
    nature1, nature3 = nature3, nature1
if nature2 > nature3:
    nature2, nature3 = nature3, nature2

if 'зайка' in nature1:
    print(nature1, len(nature1))
elif 'зайка' in nature2:
    print(nature2, len(nature2))
elif 'зайка' in nature3:
    print(nature3, len(nature3))