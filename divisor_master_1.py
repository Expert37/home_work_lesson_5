# функция, которая возвращает список делителей числа
def number_div(number):
    number_list = list(range(2, number))  # включая 1 и само число
    div_list = []   # создаем пустой список
    for i in number_list:
        if number % i == 0: div_list.append(i)  # если в итерации находится число, на которое нацело делится number - то этот делитель добавляется в список div_list
    return div_list

# функция, которая возвращает факториал числа
def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

# функция, которая возвращает среднее арифметическое трех чисел:
def average_func(x,y,z):
    return (x+y+z)/3

# функция, которая возвращает длину списка:
def len_func(*args):
    return len(args)



