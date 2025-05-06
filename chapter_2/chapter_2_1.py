#Ввод и вывод данных. Операции с числами, строками. Форматирование

phrase = input("Введите строку: ")
print(phrase)

name = 'Denis'
print('Hello, ', name, '.', sep='')

print(f"{123:0>9}")
print(f"{123:0<9}")
print(f"{123:-^9}")

print(f"first \n second")
print(f"first \t second")
print(f"first \r second")
print(f"first \b second")

print("-" * 10)
print(f"{'':->10}")

n = 25
x = 0.5

print(n + x)
print(n - x)
print(n * x)
print(n / x)
print(n ** x)

print(f"{2 ** 0.5:.2f}")

1234 % 10           # последняя цифра
1234 // 1000        # первая цифра
1234 % 100 // 10    # предпоследняя цифра

binary_value = '1001'
print(int(binary_value, 2))

# задачи:
## задача A:
print('Привет, Яндекс!')

## задача B:
name = input('Как Вас зовут?')
print(f"Привет, {name} ")

## задача C:
text = input()
print((text + '\n') * 3)

## задача D:
money = int(input())
price = 38
weight = 2.5
value = price * weight
res = int(money - value)
print(res)

## задача E:
price = int(input())
weight = int(input())
money = int(input())
value = price * weight
res = money - value
print(res)

## задача F:
name = input()
price = int(input())
weight = int(input())
money = int(input())
value = price * weight
res = money - value
print('Чек')
print(f"{name} - {weight}кг - {price}руб/кг")
print(f"Итого: {value}руб")
print(f"Внесено: {money}руб")
print(f"Сдача: {res}руб")

## задача G:
X = int(input())
print('Купи слона!\n' * X)

## задача H:
rep = int(input())
phrase = input()
print(("Я больше никогда не буду писать \"" + phrase + "\"!\n") * rep)

## задача I:
x1 = int(input())
x2 = int(input())
y = x1 * x2 / 2
print(int(y))

## задача J:
name = input()
value = int(input())
group_num = value // 100
bed_num = value // 10 % 10
child_num = value % 10
line1 = f"Группа №{group_num}."
line2 = f"{child_num}. {name}."
line3 = f"Шкафчик: {value}."
line4 = f"Кроватка: {bed_num}."
print(line1, line2, line3, line4, sep='\n')

## задача K:
number = int(input())
first = number // 1000
second = number // 100 % 10
third = number % 100 // 10
fourth = number % 10
new_number = int(str(second) + str(first) + str(fourth) + str(third))
print(new_number)

## задача L:
value1 = int(input())
value2 = int(input())
x3 = (value1 % 10 + value2 % 10) % 10
x2 = (value1 // 10 % 10 + value2 // 10 % 10) % 10
x1 = (value1 // 100 + value2 // 100) % 10
res = int(str(x1) + str(x2) + str(x3))
print(res)

## задача M:
childs = int(input())
cakes = int(input())
value1 = cakes // childs
value2 = cakes - value1 * childs
print(value1)
print(value2)

## задача N:
value1 = int(input())
value2 = int(input())
value3 = int(input())
sum_value = value1 + value3 + 1
print(sum_value)

## задача O:
value1 = int(input())
value2 = int(input())
value3 = int(input())
time = (value1 * 60 + value2 + value3) % (60 * 24)
hours = time // 60
minutes = time % 60
print(f"{hours:0>2}:{minutes:0>2}")

## задача P:
a = int(input())
b = int(input())
v = int(input())
t = (b - a) / v
print(f"{t:.2f}")

## задача Q:
a = int(input())
b = str(input())
summ = a + int(b, 2)
print(summ)

## задача R:
total = str(input())
cash = int(input())
res = cash - int(total, 2)
print(int(res))

## задача S:
name = input()
price = int(input())
weight = int(input())
cash = int(input())
purchase = price * weight
res = cash - purchase
line1 = f"{'Чек':=^35}"
line2 = f"Товар:{name:>29}"
price_weight_str = f"{weight}кг * {price}руб/кг"
line3 = f"Цена:{price_weight_str:>30}"
line4 = f"Итого:{purchase:>26}руб"
line5 = f"Внесено:{cash:>24}руб"
line6 = f"Сдача:{res:>26}руб"
line7 = '=' * 35
print(line1, line2, line3, line4, line5, line6, line7, sep='\n')

## задача T:
weight = 32 #int(input())
price = 285 #int(input())
value1 = 300 #int(input())
value2 = 240 #int(input())
m1 = (weight * price - value2 * weight) / (value1 - value2)
m2 = weight - m1
print(int(m1), int(m2), sep=', ')