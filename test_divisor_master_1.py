import divisor_master_1

# Тест 1 Правильно ли формируется список делитетелей числа 27? (не включая 1 и само число):

def test_1():
    assert divisor_master_1.number_div(27) == [3, 9]

# Тест 2 Максимальным делитетем числа 36 является число 18?:

def test_2():
    assert max(divisor_master_1.number_div(36)) == 18

# Тест 3 Факториал 5 = 120?:

def test_3():
    assert divisor_master_1.factorial(5) == 120

# Тест 4 Среднее арифметическое чисел 10,20,30 = 20?:

def test_4():
    assert divisor_master_1.average_func(10,20,30) == 20

# Тест 5 Проверка функции, которая возвращает длину списка длины списка:
def test_5():
    assert divisor_master_1.len_func('Sergey', 2, 5.1, 456) == 4





