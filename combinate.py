def combinations(word):
    if not word or not isinstance(word, str):
        yield []

    for i in range(0, len(word) + 1):
        for j in range(0, len(word) - i + 1):
            yield list(word[j:j + i])
            if not i:
                break


def main():
    data = [
        '',
        'a',
        'ab',
        'afz',
        'xymk',
    ]

    for word in data:
        print(f'{word}: {list(combinations(word))}')


if __name__ == '__main__':
    main()
