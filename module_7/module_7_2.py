def custom_write(file_name, strings):
    strings_positions = dict()
    file = open(file_name, 'w', encoding='utf-8')
    num_of_str = 0
    for string in strings:
        num_of_str += 1
        strings_positions.update({(num_of_str, file.tell()): string})
        file.write(f'{string}\n')
    file.close()

    return strings_positions


if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)