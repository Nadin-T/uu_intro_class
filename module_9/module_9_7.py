def is_prime(func):
    def wrapper(*args):
        num = func(*args)
        if num > 1:
            for i in range(2, num):
                if i != num and num % i == 0:
                    print('Cоставное')
                    return num
            print('Простое')
        return num
    return wrapper

@is_prime
def sum_three(num_1, num_2, num_3):
    sum_num = num_1 + num_2 + num_3
    return sum_num

result = sum_three(2, 3, 0)
print(result)
