def test_odd(value):
    return not bool(value % 2)


def main():
    while True:
        try:
            text = input('Введите целове число>').strip()
        except KeyboardInterrupt:
            exit(0)
        except EOFError:
            exit(0)

        if not text:
            continue

        try:
            print('\t', 'Чётное' if test_odd(int(text)) else 'Нечётное')
        except ValueError:
            print(f'Ошибка разбора числа "{text}"')


if __name__ == '__main__':
    main()
