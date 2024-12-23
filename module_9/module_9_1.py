first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(str) for str in first_strings if len(str) >= 5]
print(first_result)

second_result = [(str_1, str_2) for str_1 in first_strings for str_2 in second_strings if len(str_1) == len(str_2)]
print(second_result)

third_result = {str: len(str) for str in (first_strings + second_strings) if len(str) % 2 == 0}
print(third_result)