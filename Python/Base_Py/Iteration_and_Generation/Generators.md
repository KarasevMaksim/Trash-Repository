# Примеры создания и использования генераторов
# Генератор простых чисел
```python
def primes():
    count = 2
    while True:
        check = all((True if count % i else False for i in range(2, count)))
        if check:
            yield count
        count += 1

if __name__ == '__main__':
    x = primes()        
    for _ in range(31):
        print(next(x), end=' ')
```
        
# reverse generator
```python
def reverse_generator(iter_obj):
    index = len(iter_obj) - 1
    while index >= 0:
        yield iter_obj[index]
        index -= 1
        
if __name__ == '__main__':
    gen = reverse_generator([1, 2, 3])
    print(next(gen))
    print(next(gen))
    print(next(gen))
```
# Синтаксическая констркция yield from
```python
def get_data():
    for num in range(5):
        yield num
    for char in 'ABC':
        yield char
# можно заменить на yield from <iterable>:
def get_data():
    yield from range(5)
    yield from 'ABC'

def gen2():
    yield 'Senko'
    yield 'Holo'

def gen1():
    yield 'Good girl'
    yield 'This'
    yield from gen2()
    yield 'Kawai!'

if __name__ == '__main__':
    for i in gen1():
        print(i, end=' ') # Good girl This Senko Holo Kawai!
```

# Рекурсивные генератонры
```python
def numbers(start):
    yield start
    yield from numbers(start + 1) # бесконечный рекурсивный генератор
    
mass = [[1, 2], [[3]], [[4], 5]]

# Получаем все значения вложенного списка
def get_item_from_list_gen(mass):
    if mass:
        item = mass[0]
        if isinstance(item, list):
            # Рекурсивно обрабатываем вложенные списки
            yield from get_item_from_list_gen(item)
        else:
            # Возвращаем элемент, если это не список
            yield item
        # Рекурсивно продолжаем обход оставшихся элементов
        yield from get_item_from_list_gen(mass[1:])

if __name__ == '__main__':
    gen = get_item_from_list_gen(mass)
    print(next(gen))
    print(next(gen))
```
# Generators for read file
```python
import os

def update_gen() -> str:
    for line in file_lines:
        yield f'=^^= {line} UwU'

os.chdir('.\\Python\\Base_Py\\Iteration_and_Generation')
with open('file.txt', encoding='utf-8') as file:
    file_lines = (line.strip() for line in file)
    gen = update_gen()
    
    print(next(gen))
    print(next(gen))
```
    
# Прочие примеры
```python
from typing import NamedTuple, TypeVar, Iterator


class Person(NamedTuple):
    Name: str
    Country: str
    Gender: str
    Rodilsy: int
    Umir: int
    
T = TypeVar('T', bound=Person)

persons: list = [Person('E. M. Ashe', 'American', 'male', 1867, 1941),
           Person('Goran Aslin', 'Swedish', 'male', 1980, 0),
           Person('Erik Gunnar Asplund', 'Swedish', 'male', 1885, 1940),
           Person('Genevieve Asse', 'French', 'female', 1949, 0),
           Person('Irene Adler', 'Swedish', 'female', 2005, 0),
           Person('Sergio Asti', 'Italian', 'male', 1926, 0),
           Person('Olof Backman', 'Swedish', 'male', 1999, 0),
           Person('Alyson Hannigan', 'Swedish', 'female', 1940, 1987),
           Person('Dana Atchley', 'American', 'female', 1941, 2000),
           Person('Monika Andersson', 'Swedish', 'female', 1957, 0),
           Person('Shura_Stone', 'Russian', 'male', 2000, 0),
           Person('Jon Bale', 'Swedish', 'male', 1950, 0)]

def filter_gen_country(person: list[T]) -> Iterator[T]:
    '''Выдает значния, которые соответствуют условию'''
    for i in person:
        if i.Country == 'Swedish' and not i.Umir:
            yield i
            
def filter_youngest(person: Iterator[T]) -> str:
    result = max(person, key=lambda x: x.Rodilsy)
    return result.Name
        
if __name__ == '__main__':
    print(filter_youngest(filter_gen_country(persons)))
```
```python
def unique(iterable):
    '''Выдает уникальные значения из итерируемой последовательности'''
    dublikate = set()
    for i in iterable:
        if not i in dublikate:
            dublikate.add(i)
            yield i
            
if __name__ == '__main__':
    iterator = iter('111222333') 
    uniques = unique(iterator) 
    print(next(uniques)) 
    print(next(uniques)) 
    print(next(uniques))
```
```python
numbers = [1,2,3,4,5]

def around(iterable):
    iterable = iter(iterable)
    x = None
    y = None
    z = None
    for i in iterable:
        if not x and not y and not z:
            y = i
            z = next(iterable)
            yield (x, y, z)
        else:
            x = y
            y = z
            z = i
            yield (x, y, z)
    else:
        x = y
        y = i
        z = None
        yield (x, y, z)

if __name__ == '__main__':
    print(*around(numbers)) 
    print(*around('hey'))
```            