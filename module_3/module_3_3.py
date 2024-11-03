def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
print_params(a='@')
print_params(a=45, c=False)

print_params(b = 25)
print_params(c = [1,2,3])

values_list = ['l', 1.2, 11]
print_params(*values_list)
values_dict = {'a': 15, 'b': '@', 'c': False}
print_params(**values_dict)


values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)