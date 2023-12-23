def get_common(list1, list2):
    return set(list1 or []).intersection(list2 or [])


def main():
    data = [
        [[], None],
        [[], []],
        [[1, 2, 3], []],
        [[5, 8, 9, 1], [8]],
        [[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]]
    ]

    for l1, l2 in data:
        print(f'{l1} - {l2}: {get_common(l1, l2)}')


if __name__ == '__main__':
    main()
