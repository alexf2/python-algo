def is_palindrome(word):
    if not word or not isinstance(word, str):
        return False

    for i in range(0, len(word) // 2):
        if word[i] != word[-(i + 1)]:
            return False

    return True


def main():
    data = [
        '',
        1,
        '  ',
        '123',
        'казак',
        '11',
        '121',
    ]

    for word in data:
        print(f'{word}: {is_palindrome(word)}')


if __name__ == '__main__':
    main()
