# операторы сравнения ,которые ставятся между аргументами: or|| and
# not (прописываем условия, которые долджны не выполняться. А так же сюда можем ставить or и and)
# not - самый высокий приоритет
# and - второй приоритет
# or - третий приоритет


# s = float(input())
# s1 = int(s) % 3
# if s1 == 0:
#     print(True)
# else:
#     print(False)


# s = float(input())
# s1 = int(s) % 3
# m = s1 == 0
# print(m)


# x = float(input())
# x1 = x - int(x)
# x2 = 0.50 < x1
# print(x2)


# a, b = map(int, input().split())
# v = a % b
# s = v == 0
# print(s)


# a, b = map(int, input().split())
# print(a % b == 0)


# a, b, c = map(int, input().split())
# v = (a + b) > c or (a + c) > b or (b + c) > a
# print(v)

s = float(input())
m = (s <= 2 and s >= 0) or (s >=10 and s <= 20)
print(m)