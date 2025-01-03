#decorator #python #декоратор
# Примеры создания и работы с декораторами
## Возможные применение декораторов:
- Кеширование
- Логирование
- Проверки доступа
- Проверка типов
### Описание:
Декораторы используются для изменения поведения, модификации функции, без непосредственного ее изменения. Функция обертывается декоратором, тем самым расширяется ее функционал.
***
# Шаблон стандартного декоратора
```python
def decorator(func): 
    @functools.wraps(func) 
    def wrapper(*args, **kwargs): 
        # Что-то выполняется до вызова декорируемой функции 
        value = func(*args, **kwargs) 
        # декорируется возвращаемое значение функции 
        # или что-то выполняется после вызова декорируемой функции 
        return value 
    return wrapper
```
***
# example 1 simple_decorator
```python
def simple_decorator(func):
    print('im cat! =^^=')
    return func

def meow():
    print('Meow :3')

if __name__ == '__main__':
    meow = simple_decorator(meow)
    meow()
```
***
# example2 new_print
### Описание:
Изменяет поведение стандартной функции `Print()`. Копирует `имя функции` и ее `doc string`
без использования библиотеки `functools`.
```python
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

if __name__ == '__main__':
    print = new_print(print)
    print(print.__name__)
    print(print.__doc__)
    print(111, 'qwe', 333, sep='xxx')
    # Restlt:
    # WRAPPER
    # PRINT(VALUE, ..., SEP=' ', END='\N', FILE=SYS.STDOUT, FLUSH=FALSE)

    # PRINTS THE VALUES TO A STREAM, OR TO SYS.STDOUT BY DEFAULT.
    # OPTIONAL KEYWORD ARGUMENTS:
    # FILE:  A FILE-LIKE OBJECT (STREAM); DEFAULTS TO THE CURRENT SYS.STDOUT.
    # SEP:   STRING INSERTED BETWEEN VALUES, DEFAULT A SPACE.
    # END:   STRING APPENDED AFTER THE LAST VALUE, DEFAULT A NEWLINE.
    # FLUSH: WHETHER TO FORCIBLY FLUSH THE STREAM.
    # 111XXXQWEXXX333
```
***
# example 3 Counter call func
### Описание:
Печатает в консоль имя вызываемой функции и сколько раз она вызывалась.
```python
import functools

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

if __name__ == '__main__':
    add_smile = counter(add_smile)
    print(add_smile('im a cat!'))
    print(add_smile('im a cat!'))
    print(add_smile('im a cat!'))
    # Result:
    # Call add_smile: 1
    # im a cat! :3
    # Call add_smile: 2
    # im a cat! :3
    # Call add_smile: 3
    # im a cat! :3
```
***
# example 4 Decorator with parametrs
```python
import functools

def add_two_smile(smile1='=^^=', smile2=':3'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = f'{smile1} {func(*args, **kwargs)} {smile2}'
            return res
        return wrapper
    return decorator

def get_text(text):
    return text

 if __name__ == '__main__':
    wrapper = add_two_smile(smile2='OwO')
    get_text = wrapper(get_text)
    print(get_text('Im a Neco!'))
    # or
    get_text = add_two_smile(
        smile1='OwO',
        smile2='UwU'
    )(get_text)
    print(get_text('Im a Neco!'))
    # Result:
    # =^^= Im a Neco! OwO
```
  ***  
# example 5 Repit Func
### Описание:
Повторяет вызов декорируемой функции n-раз.
```python
import time
import functools
import requests

def repit_requests(iteration, time_wait=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, iteration + 1):
                status_code, response = func(*args, *kwargs)
                print('Func run iteration:', i, 'code:', status_code)
                if status_code == 200:
                    return response
                else:
                    time.sleep(time_wait)
            raise Exception('Bad request!')
        return wrapper
    return decorator

@repit_requests(5)
def test_request(url):
    response = requests.get(url)
    return response.status_code, response.text

if __name__ == '__main__':
    answer = test_request('https://habr.com/ru/news/750366682/')
    print(answer)
```
***
# Decorator with params and not params
```python
def decorator_params(arg1, arg2):
    def real_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return real_decorator

def init_decorator(func=None, *, arg1=None, arg2=None):
    # Декоратор прослойка для инициализации типа вызова декоратора
    # Декоратор будет вызван как декоратор с параметром или без
    if func is None:
        # Вызов декоратора с параметрами
        return decorator_params(arg1, arg2)
    else:
        # Вызов как обычного декоратора
        return decorator_params(arg1, arg2)(func)

@init_decorator
def func_example():
    print('666')

@init_decorator(arg1=1, arg2=2)
def fucn_example2():
    print(555)

if __name__ == '__main__':
    func_example()
    func_example2()
```
***
# Type Hint for decorators
from `typing` import `Callable`, `TypeVar`, `ParamSpec`

- любые входящие аргументы, любой результат
`Callable[..., Any]`

- функция вида `func(a: int, b: float)`
`Callable[[int, float], Any]`

- функция вида `func(a: int, b: float) -> int`
`Callable[[int, float], int]`
```python
import functools
from typing import Callable, TypeVar, ParamSpec


T = TypeVar("T")

def func(a: T) -> T:
    pass
# int -> int, str -> str, float -> float

F_Spec = ParamSpec("F_Spec")
F_Return = TypeVar("F_Return")

def decorator(
    func: Callable[
        F_Spec,  # функция с произвольными входными аргументами
        F_Return
    ]
) -> Callable[
    F_Spec,      # функция с теми же входными аргументами
    F_Return
]:
    @functools.wraps(func)
    def wrapper(
        *args: F_Spec.args,      # эти аргументы
        **kwargs: F_Spec.kwargs  # эти аргументы
    ) -> F_Return:
        return func(*args, **kwargs)
    return wrapper
```
***