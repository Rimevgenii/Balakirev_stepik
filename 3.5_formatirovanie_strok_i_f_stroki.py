# как работает .format:
# age = 18
# name = 'Сергей'
# 'Меня зовут {0}, мне {1} и я люблю язык Python'.format(name,age)
# string.format(args)
#
# Так же аргументам в формате можно присваивать и ключи
# 'Меня зовут {fio}, мне {old} и я люблю язык Python'.format(fio = name,old = age)
#
# f"" - ф-строка
# f'Меня зовут {name}, мне {age} и я люблю язык Python'
# А так же можно оперировать переменными:
# f'Меня зовут {name.upper()}, мне {age*2} и я люблю язык Python'
#
# f'Меня зовут {len(name)}, мне {age*2} и я люблю язык Python'

# a = input()
# b = input()
# c = input()
#
# print("Уважаемый {0} {1}! Поздравляем Вас с {2}-летием!".format(a,b,c))

# a,b,c = map(int, input().split())
# print("Габариты: {0} x {1} x {2}".format(a,b,c))


# a,b = map(int, input().split())
# print(f' {min(a,b)} {max(a,b)}')



# a = input()
# b = input()
# c = input()
# d = input()
#
# print(f"г. {a}, ул. {b}, д. {c}, кв. {d}")



a = float(input())
b = int(input())
c = b // a
print(f"Вы можете получить {round(c)}$ за {b} рублей по курсу {a}")