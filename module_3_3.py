def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(b=25)
print_params(c=[1, 2, 3])
# Да, вызовы print_params(b = 25) и print_params(c = [1,2,3]) работают.

values_list = [1, 'str', False]
values_dict = {'a': 1, 'b': 'Пока', 'c': [5, 6, 7]}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [5, None]
print_params(*values_list_2, 42)
# Вызов print_params(*values_list_2, 42) работает.
