def calculate_structure_sum(data_structure):
    """
    Рекурсивно вычисляет сумму чисел и длин строк во вложенной структуре данных.

    Аргументы:
        data_structure: Вложенная структура данных (списки, кортежи, словари, строки).

    Возвращаемое значение:
        Сумма чисел и длин строк.
    """
    total_sum = 0
    if isinstance(data_structure, (list, tuple)):
        for item in data_structure:
            total_sum += calculate_structure_sum(item)
    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            total_sum += calculate_structure_sum(value)
            total_sum += calculate_structure_sum(key)
    elif isinstance(data_structure, str):
        total_sum += len(data_structure)
    elif isinstance(data_structure, (int, float)):
        total_sum += data_structure
    elif isinstance(data_structure,(set,frozenset)):
        for item in data_structure:
            total_sum += calculate_structure_sum(item)

    return total_sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)  # Output: 99
