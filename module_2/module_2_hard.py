def decoder(num):
    password = []
    for i in range(1, 20):
        for j in range(2, 20):
            if i != j and num % (i + j) == 0:
                if i and j not in password:
                    password.append(i)
                    password.append(j)

    result = ''
    for char in password:
        result += str(char)
    return result


num = int(input('Введите целое число от 3 до 20: '))
result = decoder(num)
print(f'Ваш пароль: {result}')