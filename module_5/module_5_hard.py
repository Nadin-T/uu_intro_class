import hashlib
import time

class User:
    """
    Класс пользователя, содержащий атрибуты: логин, пароль, возраст
    """
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def __str__(self):
        return f'Пользователь: никнейм {self.nickname}, {self.age} {self.get_age(self.age)}'

    def get_age(self, age):
        if 11 <= age <= 14:
            return 'лет'
        elif age % 10 == 1:
            return 'год'
        elif 2 <= age % 10 <= 4:
            return 'года'
        elif 5 <= age % 10 <= 9:
            return 'лет'


class Video:
    """
    Класс видео, содержащий атрибуты: название, продолжительность (в секундах), секунда остановки,
    ограничение по возрасту (18+)
    """
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return f'Видео "{self.title}", продолжительность {self.duration} сек'


class UrTube:
    def __init__(self, users=None, videos=None):
        self.users = []
        self.videos = []
        self.current_user = None


    def log_in(self, nickname, password):
        #Вход в систему
        for user in self.users:
            if user.nickname == nickname:
                if user.password == user.hash_password(password):
                    self.current_user = user
                    print('Вход выполнен успешно')
                    return
                else:
                    print('Неверный пароль.')
                    return
            print(f'Пользователь {nickname} не зарегистрирован')


    def register(self, nickname, password, age):
        #Добавляет нового пользователя в список
        for user in self.users:
            if user.nickname == nickname:
                print(f'Позьзователь {nickname} уже существует')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f'Пользователь {nickname} зарегистрирован и автоматически вошел в систему.')


    def log_out(self):
        #Выход пользователя из системы
        if self.current_user:
            print(f'Пользователь {self.current_user.nickname} вышел из системы.')
        self.current_user = None


    def add(self, *videos):
        #Добавление нового видео
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)
                print(f'Видео "{video.title}" добавлено.')
            else:
                print(f'Видео "{video.title}" уже существует.')


    def get_videos(self, search_word):
        result = [video.title for video in self.videos if search_word.lower() in video.title.lower()]
        return result

    def watch_video(self, film_name):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео.')
            return

        video = next((v for v in self.videos if v.title == film_name), None)

        if video is None:
            print(f'Видео "{film_name}" не найдено.')
            return

        if video.adult_mode and self.current_user.age < 18:
            print('Вам нет 18 лет, пожалуйста, покиньте страницу.')
            return
        else:
            print(f'Начинаем просмотр видео: "{video.title}"')
            for second in range(video.duration):
                time.sleep(1)
                print(f'{second + 1}')
            print('Конец видео.')


if __name__ == '__main__':

    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
    v3 = Video('Лучший язык программирования 2024 года', 180)

    # Добавление видео
    ur.add(v1, v2, v3)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')