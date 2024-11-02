numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_primes = True

for num in numbers:
    if num > 1:
        for i in range(2, num):
            if i != num and num % i == 0:
                is_primes = False
                break
            else:
                is_primes = True
        if is_primes:
            primes.append(num)
        else:
            not_primes.append(num)


print(f'Primes: {primes}')
print(f'Not Primes: {not_primes}')