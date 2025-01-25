from multiprocessing import Pool
import time


def read_info(name):
    all_data = []
    try:
        with open(name, 'r') as f:
            data_str = f.readline()
            while data_str:
                all_data.append(data_str)
                data_str = f.readline()
    except FileNotFoundError:
        print(f"Ошибка: Файл {name} не найден.")
        return []
    except Exception as e:
        print(f"Произошла ошибка при чтении файла {name}: {e}")
        return []


filenames = [f'./file {number}.txt' for number in range(1, 5)]
# # Линейный вызов функции
# start = time.time()
# for filename in filenames:
#     read_info(filename)
# end = time.time()
# print(end - start)


# Многопроцессный вызов функции
if __name__ == '__main__':
    start = time.time()
    with Pool() as p:
        p.map(read_info, filenames)
    end = time.time()
    print(end - start)