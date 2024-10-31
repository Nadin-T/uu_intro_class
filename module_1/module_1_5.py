immutable_var = 1, 'a', True,  1.25
print(immutable_var)
# immutable_var[0] = 4 Error: 'tuple' object does not support item assignment

mutable_list = [1, 'a', True,  1.25]
mutable_list.append(123)
mutable_list.extend('hello')
mutable_list.remove(1)
print(mutable_list)