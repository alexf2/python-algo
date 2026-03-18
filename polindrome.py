# Написать функцию, принимающую на вход строку
# и возвращающую True / False в зависимости от того
# является ли она полиндромом.
# Для пустой строки вернуть True.

def is_polindrome(str_val):
    if not isinstance(str_val, str):
        raise TypeError('Ожидается строка')

    i1, i2 = 0, len(str_val) - 1
    while i1 < i2:
        if str_val[i1] != str_val[i2]:
            return False
        i1 += 1
        i2 -= 1

    return True


# Проверка
print(is_polindrome(''))
print(is_polindrome('123'))
print(is_polindrome('казак'))
print(is_polindrome('121'))
print(is_polindrome('5'))
print(is_polindrome('51'))
print(is_polindrome('552212255'))
print(is_polindrome('5522123255'))
print(is_polindrome('1  1'))
