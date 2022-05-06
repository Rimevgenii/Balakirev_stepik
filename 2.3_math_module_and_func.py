# abs - вычисляет модуль числа () принимает только числа
# min - вычисляет минимальные числа
# max - вычисляет максимально чило
# pow - возводит число в степень pow (6, 2) = 6**2 = 36
# round - округление до ближайшего целого. Так же в раунде можно указать до какой степени после запятой округлять round( 7.8888, 2) = 7.88
# Все эти функции могут работать вложено: max(1, 2, abs(min(10, 5, 3)), - 18)
# import math
#
# math.ceil() - округление числа до наиольшего целого.
# math.floor() - округление числа до наименьшего целого.
# math.factorial(6) - вычисление факториала числа (1*2*3*4*5*6 )
# math.trunc(5.8) - просто отбрасывает дробную часть, как и int


x = int(input())
discount_cost = 10 * x / 100
real_cost = x - discount_cost
total_amount = 500 / real_cost
print(int(total_amount))
