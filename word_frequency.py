from collections import Counter, defaultdict


# Написать функцию, которая подсчитывает встречаемость слов в тексте.
# Частоты вернуть в виде отсортированного по убыванию (DESC) списка картежей (слово, частота использования).
def word_count(text):
    if not isinstance(text, str):
        raise TypeError('Ожидается строка')

    counter = defaultdict(int)
    for word in text.split():
        counter[word] += 1

    return sorted(counter.items(), key=lambda it: it[1], reverse=True)


def word_count2(text):
    if not isinstance(text, str):
        raise TypeError('Ожидается строка')

    counter = Counter(text.split())

    return sorted(counter.items(), key=lambda it: it[1], reverse=True)

# Проверка


text = 'The value of the key parameter should be a function (or other callable) that takes a single argument and returns a key to use for sorting purposes. This technique is fast because the key function is called exactly once for each input record.'

print(word_count(text))
print()
print(word_count2(text))
