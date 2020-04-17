import divisor_master_1

# Тест 1 Правильно ли формируется список делитетелей числа 27? (не включая 1 и само число):

def test_1():
    assert divisor_master_1.number_div(27) == [3, 9]

# Тест 2 Максимальным делитетем числа 36 является число 18?:

def test_2():
    assert max(divisor_master_1.number_div(36)) == 18

