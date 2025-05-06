
#region Строки

text = "Привет, мир!"
print(text[8:11])
print(text[:6])
print(text[8:])
print(text[:])
print(text[::2])

num = 13
base = 2

def foo_1():
    a = 1 + 2
    print(a, end=' ')

def foo_2():
    global a
    a = 1 + 2
    print(a, end=' ')

foo_1()
print(a)

foo_2()
print(a) 

# методы строк
s = 'hello, World'
s.capitalize()
s.count('l')
s.islower()
s.endswith('rld')
s.find('ello')
s.index('o')
s.isalnum()
s.isalpha()
s.isdigit()
s.islower()
s.isupper()

a = ['1', '2', '3']
'->'.join(a)

s = 'text'
s.ljust(10, '=')
s.rjust(10, '=')

s = 'BCCAstring'
s.lstrip('ABC')
s = 'stringBCCA'
s.rstrip('ABC')
s = 'BCCAstringBCCA'
s.strip('ABC')

s = 'one, two, three'
s.split(',')

s = 'Hello, World!'
s.startswith('He')
s = 'hello, world!'
s.title()
s.upper()

s = '123'
s.zfill(5)

#endregion

#region Списки

numbers = [10, 20, 30, 40, 50]
print(numbers[0])
print(numbers[-1])
print(numbers[1:3])
print(numbers[0])
print(numbers[::-1])
print(numbers[0])
numbers[2] = 100
print(numbers)
numbers.append(300)
numbers.pop(0)
del numbers[-1] # удалить элемент или группу элементов

numbers = [10, 20, 30, 40, 50]
10 in numbers
10 not in numbers
[1, 2] + [3, 4, 5]
[1, 2, 3] * 3
len(numbers)
min(numbers)
max(numbers)
numbers.index(50)
numbers.count(10)
numbers.append(200)
numbers.extend([6 ,7, 8])
numbers.insert(3, 999)
numbers
numbers.remove(999)
numbers.reverse()
print(numbers)

numbers.sort()
print(numbers)
sorted(numbers)

#endregion

#region Кортеж

text = 'Привет, мир!'
text[0:-3]
text[-3:-1]
list_symbols = list(text)
tuple_symbols = tuple(text)
str(list_symbols)

#endregion