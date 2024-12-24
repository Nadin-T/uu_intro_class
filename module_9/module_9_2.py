first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Генераторная сборка для разницы длин строк, если они не равны
first_result = (len(first_str) - len(second_str) for first_str, second_str in zip(first, second)
                if len(first_str) != len(second_str))
print(list(first_result))

# Генераторная сборка для сравнения длин строк в одинаковых позициях
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))
print(list(second_result))