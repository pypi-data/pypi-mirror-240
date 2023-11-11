"""
Пример линейного поиска количества повторений элемента

Что ищем, массив -> Количество повторений
"""


def lin_amount(element, massive):
    counter = 0
    for i in range(len(massive)):
        if massive[i] == element:
            counter += 1
    return counter


"""
Проверка встречается ли элемент в массиве

Что ищем, массив -> YES или NO
"""


def lin_flag(element, massive):
    flag = 'NO'
    for i in range(len(massive)):
        if massive[i] == element:
            flag = 'YES'
    return flag


"""
Поиск максимального элемента

Массив -> Цифра максимального элемента
"""


def mx(massive):
    max_element = massive[0]
    for i in range(len(massive)):
        if massive[i] > max_element:
            max_element = massive[i]
    return max_element


"""
Поиск Минимального элемента

Массив -> Цифра минимального элемента
"""


def mn(massive):
    min_element = massive[0]
    for i in range(len(massive)):
        if massive[i] < min_element:
            min_element = massive[i]
    return min_element


"""
Поиск индекса максимального элемента

Массив -> Индекс максимального элемента
"""


def mx_i(massive):
    max_index = 0
    for i in range(len(massive)):
        if massive[i] > massive[max_index]:
            max_index = i
    return max_index


"""
Поиск индекса минимального элемента

Массив -> Индекс минимального элемента
"""


def mn_i(massive):
    min_index = 0
    for i in range(len(massive)):
        if massive[i] < massive[min_index]:
            min_index = i
    return min_index
