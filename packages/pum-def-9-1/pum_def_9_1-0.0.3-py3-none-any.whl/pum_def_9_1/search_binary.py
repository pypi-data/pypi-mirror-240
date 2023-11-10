"""
Бинарный поиск слева направо

Элемент, массив -> индекс элемента
"""

def left_bound(element, massive):
    left = -1
    right = len(massive)
    while right - left > 1:
        middle = (left + right) // 2
        if massive[middle] < element:
            left = middle
        else:
            right = middle
    return left + 1

"""
Бинарный поиск справа налево

Элемент, массив -> индекс элемента
"""

def right_bound(element, massive):
    left = -1
    right = len(element)
    while right - left > 1:
        middle = (left + right) // 2
        if element[middle] <= massive:
            left = middle
        else:
            right = middle
    return right - 1


