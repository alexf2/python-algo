"""
Дана строка букв. Строка может быть пустой, цифр быть не может.
Требуется сжать повторяющиеся друг за другом символы, заменив буквой и счётчиком.
Например: abcsssv меняем на abcs2v, aaazz меняем на a2z1.
Тоесть, чтобы повторяющуюся букву можно было восстановить по счётчику, вставив её несколько раз: bbbb --> b3 - тут мы при распаковске увидим, что b нужно вставить три раза.
Это алгоритм RLE.
"""


def rle(data: str) -> str:
    val = str(data)
    result = []  # для экономии памяти будем собирать строку в списке
    stop_limit = len(val)

    if stop_limit > 0:

        prev_char = val[0]
        count = 0
        # тут намеренно выходим за пределы строки, чтобы у нас был стоповый символ для подчистки
        # накопленного хвоста, иначе код result.append(f'{prev_char}{count}') пришлось бы
        # повторять после цикла for.
        for i in range(1, stop_limit + 1):
            curr_char = None if i == stop_limit else val[i]

            if prev_char != curr_char:
                if count == 0:
                    result.append(prev_char)
                else:
                    result.append(f'{prev_char}{count}')
                    count = 0
                prev_char = curr_char
            else:
                count += 1

    return ''.join(result)


# Тесты
test_data = ('', 'abccccaggz', 'aab', 'm', 'mmm', 'azz', 'azzzz', 'aazz', 'abcxxxxyyzzzzabc')
for value in test_data:
    print(value, ' --> ', rle(value))
