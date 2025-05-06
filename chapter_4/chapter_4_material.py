#region Множества
vowels = {'a', 'b', 'b'}
vowels

s_1 = {1, 2, 3}
s_2 = {3, 4, 5}

# объединение множеств
s_1 | s_2
s_1.union(s_2)

# пересечение множеств
s_1 & s_2
s_1.intersection(s_2)

# вычитание множеств
s_1 - s_2
s_1.difference(s_2)

# симметрическая разность
s_1 ^ s_2
s_1.symmetric_difference(s_2)

vowels = {"а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"}
letters = set("коллекция")
print(", ".join(letters & vowels))

# методы множеств
s_1.add(6)
s_1.remove(6)
s_1.discard(10)
s_1.pop()
s_1.clear()
len(s_1)

#endregion

# region Словари
dict = {"Россия": "Москва",
        "США": "Вашингтон",
        "Франция": "Париж"}
dict
print(dict["Россия"])

if "Сербия" in dict:
    print(dict["Сербия"])
else:
    print('Такой страны нет в словаре!')


# методы словарей
len(dict)

d = {"a": 1, "b": 2, "c": 3}
del d["b"]
print(d)

d.clear()

d = {"a": 1, "b": 2, "c": 3}
d.copy()

d.get('aaa', 0)

d.items()

list(d.keys())

d.pop('a', 0)

d.keys()
list(d.values())

# запоминаем номера индексов цифр
string = '10111100202003033330044440506060700'
d = dict()
char_num = 0
for char in string:
    d[char] = d.get(char, []) + [char_num]
    char_num += 1






#endregion