
def number_div(number):
    number_list = list(range(1, number+1))  # включая 1 и само число
    div_list = []   # создаем пустой список
    for i in number_list:
        if number % i == 0: div_list.append(i)  # если в итерации находится число, на которое нацело делится number - то этот делитель добавляется в список div_list
    return div_list


