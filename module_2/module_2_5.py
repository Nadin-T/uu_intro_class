def get_matrix(n, m, value):
    """Возвращает матрицу размером n на m со значениями value."""
    matrix = []

    for i in range(0, n):
        new_list = []
        for j in range(0, m):
            new_list.append(value)
        matrix.append(new_list)
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print(result1)
print(result2)
print(result3)