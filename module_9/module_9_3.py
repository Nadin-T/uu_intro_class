import random
from random import choice

from django.utils.lorem_ipsum import words

first = 'Мама мыла раму'
second = 'Рамена мало было'

bool_list = list(map(lambda x, y: x == y, first, second))
print(*bool_list)

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for data in data_set:
                # Проверяем, является ли data списком
                if isinstance(data, list):
                    # Преобразуем список в строку и записываем
                    file.write(' '.join(map(str, data)) + '\n')
                else:
                    file.write(str(data) + '\n')
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

class MysticBall:
    def __init__(self, *words):
        self.words = list(words)

    def __call__(self):
        return random.choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())