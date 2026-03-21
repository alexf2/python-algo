# Даны два массива/Питон-списка чисел, каждый из которых уже отсортирован по возрастанию.
# Требуется написать функцию, которая принмает на вход два обязательных параметра в которых эти массивы
# И возвращает новый объединённый list, состоящий из этих двух, который полностью отсортирован по возрастанию.

import heapq
from collections.abc import Sequence

# Это самый очевидный, простой вариант грубой силы. Он не оптимален по производительности.


def brute_force_merge_sorted_lists(list_a, list_b):
    if not isinstance(list_a, Sequence) or not isinstance(list_b, Sequence):
        raise TypeError('Ожидаются два отсортированных по возрастанию массива в форме MutableSequence')

    result = list_a + list_b
    result.sort()  # тут сложность O(n * log(n)), а нам нужно достичь O(n + m)
    return result


def std_lib_merge_sorted_lists(list_a, list_b):
    if not isinstance(list_a, Sequence) or not isinstance(list_b, Sequence):
        raise TypeError('Ожидаются два отсортированных по возрастанию массива в форме MutableSequence')

    # Пример с использованием функции merge встроенного библиотечного модуля heapq Python: O(n + m)
    return list(heapq.merge(list_a, list_b))

# Пробуем сделать всю работу в одном цикле, но выходит много кода, так как исходные массивы могут быть разной длины.
# O(n + m)


def merge_sorted_lists(list_a, list_b):
    if not isinstance(list_a, Sequence) or not isinstance(list_b, Sequence):
        raise TypeError('Ожидаются два отсортированных по возрастанию массива в форме MutableSequence')

    len_a = len(list_a)
    len_b = len(list_b)
    result = []
    i_a = i_b = 0

    while i_a < len_a or i_b < len_b:
        if i_a >= len_a and i_b < len_b:
            result.append(list_b[i_b])
            i_b += 1
        elif i_b >= len_b and i_a < len_a:
            result.append(list_a[i_a])
            i_a += 1
        elif i_a >= len_a and i_b >= len_b:
            break
        else:
            if list_a[i_a] < list_b[i_b]:
                result.append(list_a[i_a])
                i_a += 1
            else:
                result.append(list_b[i_b])
                i_b += 1

    return result

# Меньше кода получится, если поменять условие wjile с OR на AND. Тогда в цикле останется обработка только общих
# отрезков массивов. А после завершения while, нам останется докинуть в result хвост того массива, который длиннее.
# Это проще.


def merge_sorted_lists_optimal(list_a, list_b):
    if not isinstance(list_a, Sequence) or not isinstance(list_b, Sequence):
        raise TypeError('Ожидаются два отсортированных по возрастанию массива в форме MutableSequence')

    len_a = len(list_a)
    len_b = len(list_b)
    result = []
    i_a = i_b = 0

    while i_a < len_a and i_b < len_b:
        if list_a[i_a] <= list_b[i_b]:
            result.append(list_a[i_a])
            i_a += 1
        else:
            result.append(list_b[i_b])
            i_b += 1

    if i_a < len_a:
        result.extend(list_a[i_a:])
    elif i_b < len_b:
        result.extend(list_b[i_b:])

    return result


# Проверка
TEST_DATA = (
    ([1, 5, 8], []),
    ([], [2, 7, 9]),
    ([1, 7, 12, 15], [2, 8, 16]),
    ([10, 11, 12], [21, 22, 23]),
    ([21, 22, 23], [10, 11, 12]),
    ([1], [5]),
    ([5], [1]),
    ([2, 10], [1]),
    ([1], [2, 10]),
    ([1, 12, 15], [0, 13, 22]),
    ([0, 13, 22], [1, 12, 15]),
    ([1, 1], [1, 2, 10]),
)

for list1, list2 in TEST_DATA:
    print(list1, ' + ', list2, '=', brute_force_merge_sorted_lists(list1, list2))
    print(list1, ' + ', list2, '=', std_lib_merge_sorted_lists(list1, list2))
    print(list1, ' + ', list2, '=', merge_sorted_lists(list1, list2))
    print(list1, ' + ', list2, '=', merge_sorted_lists_optimal(list1, list2), '\n----\n')
