"""
Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
Например: 'Aaron' - [5, 3, 3, 5, 4]
Множество students содержит неупорядоченную последовательность имён всех учеников в классе.

Напишите программу, которая составляет словарь, используя grades и students, где ключом будет имя ученика,
а значением - его средний балл.

Вывод в консоль:
{'Aaron': 4.0, 'Bilbo': 2.25, 'Johhny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}
"""

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

#1
"""Создание списка средних баллов."""
average_score_list = []
average_score_list.append(sum(grades[0]) / len(grades[0]))
average_score_list.append(sum(grades[1]) / len(grades[1]))
average_score_list.append(sum(grades[2]) / len(grades[2]))
average_score_list.append(sum(grades[3]) / len(grades[3]))
average_score_list.append(sum(grades[4]) / len(grades[4]))

"""Создание отсортированного списка студентов."""
students_list = sorted(list(students))

"""Создание словаря"""
average_score_dict = {}
average_score_dict.update({students_list[0]: average_score_list[0]})
average_score_dict.update({students_list[1]: average_score_list[1]})
average_score_dict.update({students_list[2]: average_score_list[2]})
average_score_dict.update({students_list[3]: average_score_list[3]})
average_score_dict.update({students_list[4]: average_score_list[4]})

print(average_score_dict)


#2
"""Создание списка средних баллов."""
average_score_list = []
for i in range(0, len(grades)):
    average_score_list.append(sum(grades[i]) / len(grades[i]))

"""Создание отсортированного списка студентов."""
students_list = sorted(list(students))

"""Создание словаря"""
average_score_dict = {}
for j in range(0, len(students_list)):
    average_score_dict.update({students_list[j]: average_score_list[j]})
print(average_score_dict)