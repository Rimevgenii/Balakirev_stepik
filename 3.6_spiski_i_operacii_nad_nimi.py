# marks = [0,1,2,3,4,5] - это список
# marks[0] - обращение к конкретному индексу списка
# (marks[0] + marks[1]) - мат. операции со списками
# marks[-1] - обращение к последнему элементу списка
# -Списки это изменяемый тип данных
# marks[2] = 'другое значение' - изменение значения списка
# В списках можно хранить строки, целые числа, вещественные числа, другие списки
# a = [] или a = list() -cоздание пустых списков
# b = list(['raz', 'dva']) - создание нового, или копия другого списка
# функция лист делает список из всего. Можно даже запятые на ставить
# len() - определяет число элементом списка
# min() - мин значение элемента
# max() - макс значение элемента
# sum() - суммирует элементы
# sorted() - все это основные функции работы со списками.Сортед возвращает новый отсортированный список
# sum / len -получить среднее из списка
# Сортед по умолчанию сортирует по возрастанию, если хотим наоборот, то вторым аргументом пишем reverse
# Сортед и мин макс работает и со строками.
#
#
# + - соединение двух списоков в один [1,2,3] + [4]
# * - дублирование списка
# in - вхождение элемента в список 1320 in lst = True или [1,2] in lst = False
# del - удаление элемента списка. del lst[2]


# s = map(int, input().split())
# print(list(s))

# cities = input().split()
# list(cities)
# check = 'Москва' in list(cities)
# print(check)

# cities = input().split()
# print(list(cities)[-1])


# marks = list(map(int, input().split()))
# print(round(sum(marks)/len(marks),1))


# name = input()
# author = input()
# pages = input()
# price = float(input())
# book = [name, author, pages, price]
# book[1] = 'Пушкин'
# book[3] *= 2
# del book[2]
# print(book)

subs =list(map(int, input().split()))
print(max(subs), min(subs), sum(subs))


