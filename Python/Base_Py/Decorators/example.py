import functools

'''
Возможные применение декораторов:
Кеширование, Логирование, Проверки доступа,
'''

# example 1 simple_decorator ==================================================
def simple_decorator(func):
    print('im cat! =^^=')
    return func

def meow():
    print('Meow :3')

# if __name__ == '__main__':
#     meow = simple_decorator(meow)
#     meow()

# Шаблон дефолтного декоратора ================================================

def decorator(func): 
    @functools.wraps(func) 
    def wrapper(*args, **kwargs): 
        # Что-то выполняется до вызова декорируемой функции 
        value = func(*args, **kwargs) 
        # декорируется возвращаемое значение функции 
        # или что-то выполняется после вызова декорируемой функции 
        return value 
    return wrapper


# example3 new_print ==========================================================

def new_print(func):
    def wrapper(*args, **kwargs):
        args = (i.upper() if isinstance(i, str) else i for i in args)
        kwargs = {
            k: v.upper() if isinstance(v, str) else v for k, v in kwargs.items()
        }
        func(*args, **kwargs)
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
    return wrapper

# if __name__ == '__main__':
#     print = new_print(print)
#     print(print.__name__)
#     print(print.__doc__)
#     print(111, 'qwe', 333, sep='xxx')


# example 4 Counter call func =================================================

def counter(func):
    count = 0
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'Call {func.__name__}: {count}')
        return func(*args, **kwargs)
    return wrapper

def add_smile(text):
    return f'{text} :3'

# if __name__ == '__main__':
#     add_smile = counter(add_smile)
#     print(add_smile('im a cat!'))
#     print(add_smile('im a cat!'))
#     print(add_smile('im a cat!'))
