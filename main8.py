#Задание1

import re
EMAIL = re.compile(r'([a-z0-9_\.]+)@([a-z0-9]+\.[a-z]+)')
def email_parse(email):
    found_info = EMAIL.findall(email)
    if found_info:
        name, addr = found_info[0]
    else:
        raise ValueError(f'wrong email: {email}')
    print(name, addr)

email_parse('someone@geekbrains.ru')
email_parse('someone@geekbrainsru')

#Задание3

from functools import wraps
def type_logger(func):
    @wraps(func)
    def wrapper(*args):
        for arg in args:
            print(f'{func.__name__}({arg}: {type(arg)})', end=', ')
        return func(*args)

    return wrapper


@type_logger
def calc_cube(*args):
    """this shows only with 'from functools import wraps'"""
    return list(map(lambda x: x ** 3, args))


a = calc_cube(5, 3)
print(a)
print(calc_cube.__name__)
print(calc_cube.__doc__)

#Задание4

from functools import wraps


def val_checker(decorator_check_func):
    def _val_checker(func_calc_cube):
        @wraps(func_calc_cube)
        def wrapped(x):
            if decorator_check_func(x):
                return func_calc_cube(x)
            else:
                raise ValueError(x)

        return wrapped
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
print(a)
print(calc_cube.__name__)
print(calc_cube.__doc__)
