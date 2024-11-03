def get_multiplied_digits(number):
    str_number = str(number)
    if str_number[0] == '0':
        str_number = str_number[1:]
    else:
        first = int(str_number[0])
        if len(str_number) == 1:
            return first
        return first * get_multiplied_digits(int(str_number[1:]))


result = get_multiplied_digits(40203)
print(result)

