"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
        функция, которая принимает N целых чисел,
        и возвращает список квадратов этих чисел
        def power_numbers():
        >>> power_numbers(1, 2, 5, 7)
        <<< [1, 4, 25, 49]
    """
    return ([i ** 2 for i in args] if type(sum(args)) == int else ("wrong type of variable"))




# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(number: int):
    '''
    функция, которая принимает целове число и возвращает True,
    если это число- простое, в противном случае возвращает
    False
    '''
    dividers = 0
    for divider in range(1, number + 1):
        if number % divider == 0:
            dividers += 1
    return True if dividers <= 2 else False





def filter_numbers(input_list: list, filter_type):
    """
       функция, которая на вход принимает список из целых чисел,
       и возвращает только чётные/нечётные/простые числа
       (выбор производится передачей дополнительного аргумента)

       >>> filter_numbers([1, 2, 3], ODD)
       <<< [1, 3]
       >>> filter_numbers([2, 3, 4, 5], EVEN)
       <<< [2, 4]
       """
    try:
        if filter_type == PRIME:
            return list(filter(lambda element: is_prime(element), input_list))
        elif filter_type == ODD:
            return list(filter(lambda element: element % 2 == 1, input_list))
        elif filter_type == EVEN:
            return list(filter(lambda element: element % 2 == 0, input_list))
        else:
            raise TypeError

    except TypeError:
        return ("wrong input!")


