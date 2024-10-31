my_dict = {'Denis': 1991, 'Alla': 1989, 'Alex': 1990}
print(f'Dict: {my_dict}')
existing_value = my_dict.get('Alla')
print(f'Existing value: {existing_value}') #выводит значение по ключу без ошибок
not_existing_value = my_dict.get('Anton')
print(f'Not existing value: {not_existing_value}')
my_dict.update({'Anton': 1994, 'Bella': 2001})
deleted_value = my_dict.pop('Alex')
print(f'Deleted value: {deleted_value}')
print(f'Modified dictionary: {my_dict}')


my_set = {1, 3, 5, 6, 3, 'Apple', 5, 1, 4.15}
print(f'Set: {my_set}')
my_set.add(2)
my_set.add('6')
my_set.remove(3)
print(f'Modified set: {my_set}')