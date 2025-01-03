#closure #python #замыкания
# Примеры создания и использования замыканий
## Возможные применения:
- В основном используется для того, чтобы не использовать метод `Global`
- Отслеживание каких либо ивентов
### Описание:
Замыкания используются для того, чтобы оставить ссылку в памяти на объект внутри
локальной облости в функции. Благодаря этому, после завершения работы функции,
состояние данного объекта сохраняется в памяти и при повторном вызове функции,
объект сохраняет свои данные с прошлых вызывов функции.
***
# Simple closure for counter
### Описание:
Счетчик реализованный в замыкаемой функции.
```python
def counter():
    count = 0
    def inner():
        nonlocal count
        count +=1
        return count
    return inner

count = counter()

if __name__ == '__main__':
    for i in range(10):
        print(count())
```
***
# Closure with arguments
Также можно использовать для создания функций с предустановленными параметрами
```python
def word_creator(word):
    def inner(name):
        return f'{word}: ...{name}'
    return inner

if __name__ == '__main__':
    generate = word_creator('Я очень сильно люблю котиков')
    print(generate('Мое имя Анаями Рей'))
    # Result:
    # Я очень сильно люблю котиков: ...Мое имя Анаями Рей
```
***
# _____closure_____ 
### Описание:
- `f.__closure__` возвращает кортеж ячеек, которые были захвачены внутренней
функцией `inner`. В данном случае это только `arg`, который равен `10`.
- Переменная `name` не захвачена, поскольку она не является аргументом функции
и не используется в `inner`.
```python
def inner_clouser(arg):
    name = 'Holo'
    num = 5
    def inner():
        print(arg)
        print(name)
    return inner

if __name__ == '__main__':
    f = inner_clouser(10) # Создаем замыкание с arg=10
    for value in f.__closure__: # Итерируем по ячейкам замыкания
        # Возвращает только те значения которые были захвачены в inner
        print(value.cell_contents) # Выводим содержимое ячеек замыкания
        # Result
        # 10
        # Holo
```
***
# Closure for ivent
```python
def create_button(lable):
    def on_click():
        print(f'Кнопка "{lable}" нажата')
    return on_click

if __name__ == '__main__':
    button1 = create_button('Сохранить')
    button2 = create_button('Отмена')
    button1()
    button2()
    # Result:
    # Кнопка "Сохранить" нажата
    # Кнопка "Отмена" нажата
```
***
# Closure as class object
### Описание:
Поведение замыкаемой функции как класса.
```python
def func_as_object(a, b):
    def add():
        return a + b
    def sub():
        return a - b
    def mul():
        return a * b
    func_as_object.add = add
    func_as_object.sub = sub
    func_as_object.mul = mul
    return func_as_object

if __name__ == '__main__':
    func = func_as_object(2, 3)
    print(func.add())
    print(func.sub())
    print(func.mul())
    # Result:
    # 5
    # -1
    # 6
```
***