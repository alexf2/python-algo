import enum


class Direction(enum.Enum):
    right = 0
    left = 1
    top = 2

    bottom = 3
    if bottom is None:
        pass


def fill_matrix(n):
    if n < 1:
        return [[]]
    if n == 1:
        return [[1]]

    result = [[None for _ in range(n)] for _ in range(n)]

    left = 0; right = n - 1
    top = 0; bottom = n - 1
    row = 0; col = 0
    count = 0
    direction = Direction.right

    while left <= right and top <= bottom:
        count += 1
        result[row][col] = count

        match direction:
            case Direction.right:
                if col < right:
                    col += 1
                else:
                    top += 1
                    row = top
                    direction = Direction.bottom
                    col = right

            case Direction.left:
                if col > left:
                    col -= 1
                else:
                    bottom -= 1
                    row = bottom
                    direction = Direction.top
                    col = left

            case Direction.top:
                if row > top:
                    row -= 1
                else:
                    left += 1
                    col = left
                    direction = Direction.right
                    row = top

            case Direction.bottom:
                if row < bottom:
                    row += 1
                else:
                    right -= 1
                    col = right
                    direction = Direction.left
                    row = bottom

            case _:
                raise Exception("Invalid direction")

    return result


def dump_matrix(m):
    for row in m:
        res = ""
        for col in row:
            res += f"{col:5}"
        print(res)


def main():
    print(dump_matrix(fill_matrix(5)))


if __name__ == "__main__":
    main()
