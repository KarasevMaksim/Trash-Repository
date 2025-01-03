#python #recursion #рекурсия #алгоритмы #алгоритмы_на_собеседованиях #json
# Примеры использования рекурсий
### Описание:
Рекурсии используются для различных задач к котором можно применить методологию `разделя и влавствуй`. То есть мы берем одну большую задачи и делим ее на более мелкие подзадачи, пока не сведем их к базовому случаю, когда задача уже решена.
***
# Рекурсивный обход вложенного массива
## Рекурсивная нормализация списка
### Описание:
Рекурсивно проходится по вложенному списку и возвращает все его элементы в виде обычного не вложенного списка.
```python
from typing import Any

mass = [1, [2, [3, 4], 5, [6, 7], 8], 9, [10, [11, ['Senko', 'Holo'], 12], 13, 'Senko', [14, 15], 16], 17]

def list_normalizing(mass: list) -> list[Any]:  
    new_mass = list()  
    def inner_search(mass):  
        if mass:  
            item = mass[0]  
            if not isinstance(item, list):  
                new_mass.append(item)  
            else:  
                inner_search(item)  
            inner_search(mass[1:])  
                  
    inner_search(mass)  
    return new_mass
```
***
## Рекурсивный поиск элемента во вложенном списке
### Описание:
Рекурсивно проходится по вложенному списку и возвращает первый найденный элемент, который был передан в аргумент для поиска.
```python
from typing import Any

mass = [1, [2, [3, 4], 5, [6, 7], 8], 9, [10, [11, ['Senko', 'Holo'], 12], 13, 'Senko', [14, 15], 16], 17]

def list_search_first_elem(mass: list, item: Any) -> True | False:  
    value = False  
    def inner_search(mass):  
        nonlocal value  
        if item in mass:  
            value = True  
            return        for i in mass:  
            if not isinstance(i, list):  
                continue  
            inner_search(i)  
    inner_search(mass)  
    return value

if __name__ == '__main__':  
    print(list_search_first_elem(mass, 15))
```
***
## Рекурсивный просмотор элементов в вложенном списке
### Описание:
Выводит на экран все элементы вложенного списка, с использованием рекурсии и цикла.
`Вариант 1`
```python
from typing import Any

mass = [1, [2, [3, 4], 5, [6, 7], 8], 9, [10, [11, ['Senko', 'Holo'], 12], 13, 'Senko', [14, 15], 16], 17]

def rec_all_list_elem(mass) -> None:  
    for i in mass:  
        if not isinstance(i, list):  
            print(i)  
        else:  
            rec_all_list_elem(i)
```
`Вариант 2`
Возвращает строку собранную из всех элементов вложенного списка, с использованием возвращения значения через обратный стек.
```python
from typing import Any

mass = [1, [2, [3, 4], 5, [6, 7], 8], 9, [10, [11, ['Senko', 'Holo'], 12], 13, 'Senko', [14, 15], 16], 17]

def rec_all_list_elem_str(mass) -> str:  
    if mass:  
        if isinstance(mass[0], list):  
            return rec_all_list_elem_str(mass[0]) + ', ' + rec_all_list_elem_str(mass[1:])  
        else:  
            return str(mass[0]) + ', ' + rec_all_list_elem_str(mass[1:])  
    else:  
        return ''
```
***
# Рекурсивный обход вложенных словарей, json
## Пример вложенных словарей
```python
info = {'name': 'Alyson',    
'surname': 'Hannigan',    
'birthday': {'day': 24, 'month': 'March', 'year': 1974},   
'family': {'parents': {'mother': 'Emilie Posner', 'father': 'Alan Hannigan'}}}  
  
data = {'firstName': 'Тимур', 'lastName': 'Гуев', 'birthDate': {'day': 10, 'month': 'October', 'year': 1993}, 'address':   
    {'streetAddress': 'Часовая 25, кв. 127', 'city':   
        {'region': 'Московская область', 'type': 'город', 'cityName': 'Москва'},  
        'postalCode': '125315'}}  
data2 = {'first_name': 'Alyson', 'last_name': 'Hannigan', 'birthday': {'day': 24, 'month': 'March', 'year': 1974}}  
  
my_dict1 = {'users': {'Arthur': {'grades': [4, 4, 3], 'top_grade': 4}, 'Timur':   
{'grades': [5, 5, 5], 'top_grade': 5}}}  
  
my_dict2 = {'Arthur': {'hobby': 'videogames', 'drink': 'cacao'}, 'Timur': {'hobby':   
'math'}}  
  
my_dict3 = {'Arthur': {'hobby': 'videogames', 'drink': 'cacao'}, 'Timur': {'hobby':   
'math'}}
```
***
## Поиск элемента в вложенном словаре
### Описание:
`Вариант 1`
Возвращает первое найденное значение по переданному ключу в вложенном словаре. Используя рекурсию и циклы.
```python
from typing import Any

def find_first_value_simple(data: dict, key: str) -> Any:  
    if key in data:  
        return data[key]  
    for v in data.values():  
        if isinstance(v, dict):  
            value = find_first_value_simple(v, key)  
            if value is not None:  
                return value
```
`Вариант 2`
Делает тоже самое что и первый вариант, но дополнительно имеет замыкание.
```python
from typing import Any

def find_first_value_closure(data: dict, key: str) -> Any:  
    value = None  
    def inner_find(data: dict):  
        nonlocal value  
        if key in data:  
            value = data[key]  
            return  
        for v in data.values():  
            if isinstance(v, dict):  
                inner_find(v)  
    inner_find(data)   
    return value
```
***
## Поиск всех элементов в вложенном словаре
### Описание:
Рекурсивный поиск всех элементов в вложенном словаре, по заданному в аргументе ключу. Возвращает список со всеми найденными элементами.
```python
from typing import Any

def find_all_values_for_key(data: dict, key: str) -> list[Any]:  
    value = list()  
    def inner_find(data: dict):  
        if key in data:  
            value.append(data[key])  
        for v in data.values():  
            if isinstance(v, dict):  
                inner_find(v)  
    inner_find(data)   
    return value
```
***
# Прочие рекурсивные функции
## Разворот строки
```python
def reverse_name(name: str) -> str:  
    if name:  
        return name[-1] + reverse_name(name[:len(name) - 1])  
    return ''
```
***
## Возведение числа в степень
```python
def my_pow(num, n):  
    if not n == 0:  
        return num * my_pow(num, n-1)  
    return 1
```
***
## Рекурсивная функция с замыканием
```python
def draw_rect(width, hight):  
    def inner(step):  
        if step < hight:  
            print('*' * width)  
            inner(step + 1)  
    inner(0)
```
***
## Факториал числа
```python
def factorial(n):  
    if not n or n == 1:  
        return 1  
    return n * factorial(n - 1)
```
***
## Перевод в двоичную систему счисления
```python
def to_binary(num):  
    if num == 1:  
        return str(1)  
    if num == 0:  
        return str(0)  
    x1 = num // 2  
    x2 = x1 * 2  
    res = num - x2  
    return to_binary(x1) + str(res)
```
***
## Задача про подмножество
### Описание:
Сочетанием из n элементов по k называется подмножество этих n элементов размера k. Два сочетания называются различными, если одно из сочетаний содержит элемент, который не содержит другое. Числом сочетаний из n по k называется количество различных сочетаний из n по k. Обозначим это число за C(n, k).  
Пример:  
Пусть n = 3, т. е. есть три элемента (1, 2, 3). Пусть k = 2. Все различные сочетания из 3 элементов по 2: (1, 2), (1, 3), (2, 3). Различных сочетаний три, поэтому C(3, 2) = 3. Несложно понять, что C(n, 0) = 1, так как из n элементов выбрать 0 можно единственным образом, а именно, ничего не выбрать. Также несложно понять, что если k > n, то C(n, k) = 0, так как невозможно, например, из трех элементов выбрать пять. Для вычисления C(n, k) в других случаях используется следующая рекуррентная формула:  
C(n, k) = C(n - 1, k) + C(n - 1, k - 1).  
Реализуйте программу, которая для заданных n и k вычисляет C(n, k).  
Вашей программе на вход подается строка, содержащая два целых числа n и k (1 ≤ n ≤ 10, 0 ≤ k ≤ 10).  
Ваша программа должна вывести единственное число: C(n, k).
```python
def c(n, k):  
    if n < k:  
        return 0  
    elif k == 0:  
        return 1  
    return c(n-1, k) + c(n-1, k-1)  
  
if __name__ == '__main__':  
    n, k = map(int, input().split())  
    print(c(n, k))
```
***