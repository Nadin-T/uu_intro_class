from random import choice


class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    """
    Класс пользователя, содержащий атрибуты: логин, пароль
    """
    def __init__(self, username, password, password_confirm):
        self.username = username
        if  password == password_confirm and password_validation(password):
            self.password = password
        else:
            print('Пароль неверен')
            self.password = None

def password_validation(password):
    password_valid = False
    if len(password) >= 8:
        int_count = str_upper_count = 0
        for char in password:
            if char.isdigit():
                int_count += 1
            elif char == char.upper():
                str_upper_count += 1
        if int_count >= 1 and str_upper_count >= 1:
            password_valid = True
    else:
        print('Неверный размер пароля. Пароль должен содержать не менее 8 символов, '
              'иметь минимум 1 заглавную букву и минимум 1 цифру.')
    return password_valid


if __name__ == '__main__':
    database = Database()
    print('Приветствую!')
    while True:
        choice = input('Выберите действие: \n1 - Вход в систему\n2 - Регистрация\n0 - Выход\n')
        if choice == '1':
            login = input('Введите логин: ')
            if login in database.data:
                print('ok')
            else:
                print('Пользователь не найден.')
            password = input('Введите пароль: ')
            if password == database.data[login]:
                print(f'Вход выполнен, {login}!')
                break
            else:
                print('Неверный пароль')
        if choice == '2':
            user = User(
                input('Введите логин: '),
                password := input('Введите пароль: '),
                password2 := input('Повторите пароль: ')
            )
            if password != password2:
                print('Пароли не совпадают, попробуйте ещё раз.')
                continue
            if user.username is not None and user.password is not None:
                database.add_user(user.username, user.password)
                print(database.data)
            else:
                print('Регистрация не удалась')
        if choice == '0':
            break