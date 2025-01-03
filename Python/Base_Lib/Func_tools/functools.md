#functools #встроенные_библиотеки_python #python #base_lib #lib #библиотеки 
# Встроенная библиотека python `functools`
## Функция `reduce`
Функция `reduce` берет первое значение последовательности и обрабатывает его со вторым. После этого, первым значением для обработки становится результат этого вычисления и также обрабатывается со следующим элементом последовательности
```python
from functools import reduce

array = [1, 2, 3, 4, 5]
resj_reduce = reduce(lambda a, b: a + b, array)
# answer: 15
```
***
## Функция `partial`
Функция `partial` используется для переопределения отправки аргументов в функцию. Таки образом мы переопределяем поведение функции как при использовании декоратора.
```python
from functools import partail, update_wrapper
from typing import Callable

def multiply(a: int, b: int) -> int:
	'''Функция перемножает два числа и возвращает результат вычисления'''
	return a * b

double = partail(multiply, 2)

update_wrapper(double, multiply) # копируем докстринг из основной функции в parteil
```

```python
def send_email(name: str, email_address: str, text: str) -> None:
	'''Функция распечатывает данные, которые будут использоваться для отправки
	письма по email адрессу'''
	print(f"Имя: {name}")  
	print(f"Email: {email_address}")  
	print(f"Сообщение: {text}")

# Создание частично премененной функции
send_email_for_senko = partial(
	send_email,
	name='Senko'
	email_address='SenkoSun@gmail.com'						   
)
# Обновление метаданных функции
update_wrapper(send_email_for_senko, sen_email)

if __name__ == '__main__':
	send_email('Holo', 'Wolf@gmail.com', 'Привет как жизнь!')
	sen_email_for_senko(text='Здравствуй Senko, '
							 'мне срочно необходимо '
							 'пожамкать ваш хвостик')
'''
Answer:
Имя: Holo
Email: Wolf@gmail.com
Сообщение: Привет, как жизнь!

Имя: Senko
Email: SenkoSun@gmail.com
Сообщение: Здравствуйте Senko, мне срочно необходимо пожимать ваш хвостик
'''
```
***