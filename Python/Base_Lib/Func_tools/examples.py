from functools import reduce

# функция reduce берет первое значение последовотельности и обрабатывает его
# со второмы, после этого превым значением для обработки становится результат
# этого вычисления и также обрабатывается со следущим элементом
# последовательности
res_reduce = reduce(lambda a, b: a + b, [1, 2, 3, 4, 5])

# =============================================================================
# функция partial используется для переопределения отправки аргументов в
# функуию, таким образом мы переопределям поведении функции как при
# использовании декоратора
from functools import partial, update_wrapper
from typing import Callable

def multiply(a: int, b: int) -> int:
    '''функция перемножает два числа и возвращает результат вычисления'''
    return a * b

double = partial(multiply, 2)

update_wrapper(double, multiply) # копируем докстринг из основной функции
# в parteil

def send_email(name: str, email_address: str, text: str) -> None:
    '''Функция распечатывает данные, которые будут использоваться для отпрвки
    письма по email адрессу'''
    print(f"Имя: {name}")
    print(f"Email: {email_address}")
    print(f"Сообщение: {text}")

# Создание частично примененной функции
send_email_for_senko = partial(
    send_email,
    name='Senko',
    email_address='SenkoSun@gmail.com'
)

# Обновление метаданных функции
update_wrapper(send_email_for_senko, send_email)

if __name__ == '__main__':
    send_email('Holo', 'Wolf@gmail.com', 'Привет, как жизнь!')
    print()
    send_email_for_senko(text='Здравствуйте Senko, '
                              'мне срочно необходимо '
                              'пожимать ваш хвостик')
# =============================================================================


    