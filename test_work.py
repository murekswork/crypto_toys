def count_ways(matrix):
    rows, cols = len(matrix), len(matrix[0])
    ways = sum(
        matrix[i][j] == '-' and
        (i == 0 or matrix[i - 1][j] == '-') and
        (i == rows - 1 or matrix[i + 1][j] == '-') and
        (j == 0 or matrix[i][j - 1] == '-') and
        (j == cols - 1 or matrix[i][j + 1] == '-')
        for i in range(rows) for j in range(cols)
    )
    return ways


def main():
    # Запрашиваем у пользователя размеры матрицы
    N = int(input("Введите число N (1 <= N <= 100): "))
    M = int(input("Введите число M (1 <= M <= 100): "))

    # Запрашиваем у пользователя матрицу
    matrix = [
        input(f"Введите строку {i + 1} из {M} символов (- или *): ")
        for i in range(N)
    ]

    # Выводим количество способов поставить крестик
    ways = count_ways(matrix)
    print(f"Количество способов поставить крестик: {ways}")


if __name__ == "__main__":
    main()