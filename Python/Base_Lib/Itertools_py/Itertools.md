#itertools #встроенные_библиотеки_python #python #base_lib #lib #библиотеки 
# Встроенная библиотека python `itertools`
## Функции порождающие данные, бесконечные итераторы
### Функция `count`
Функция `count` позволяет возвращает объект итератор, который с каждым использованием увеличивается на единицу.

```python
from itertools import count

'''Бесконечный счетчик'''
count1 = count() # name_args: start, step
```
***
### Функция `cycle`
Функция `cycle` посимвольно возвращает итерируемый объект. В конце не бросает исключение, а начинает заново. Так как сохраняет в себе копию объекта `расходует память`.
```python
from itertools import cycle

x = cycle('Holo')
print(next(x))
# answer: H
```
***
### Функция `repeat`
Функция `repeat` повторяет объект, бесконечно или с ограничением.

```python
from itertools import repeat

rep = repeat('SenkoSun', 5) # args: obj, time: 'количество повторений'
```
***
### Функция `starmap`
Через функцию `starmap`  можно делать дополнительную распаковку в отличии от обычного `map`.
```python
from itertools import starmap

persons = [('Timur', 'Guev'), ('Arthur', 'Kharisov')]

full_names1 = list(starmap(lambda name, surname: f'{name} {surname}', persons))  
full_names2 = list(map(lambda name: f'{name[0]} {name[1]}', persons))
```
***
### Функция `accumulate`
Функция `accumulate` работает аналогично функции `reduce`, за тем исключением, что функция генерирует все промежуточные результаты аккумуляции, а не только итоговый результат. Также функции требуется дополнительная библиотека `operator`, для использования более сложных вычислений. По умолчанию используется оператор сложения.
```python
import operator
from itertools import accumulate

data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]

print(list(accumulate(data))) # [3, 7, 13, 15, 16, 25, 25, 32, 37, 45]
print(list(accumulate(data, operator.mul))) # [3, 12, 72, 144, 144, 1296, 0, 0, 0, 0]
print(list(accumulate(data, max))) # [3, 4, 6, 6, 6, 9, 9, 9, 9, 9]
print(list(accumulate(data, min))) # [3, 3, 3, 2, 1, 1, 0, 0, 0, 0]
```
***
## Фильтрующие функции
### Функция `compress`
Функция `compress` сопоставляет итерируемое значение с другим итерируемым значением.
```python
from itertools import compress

data = 'ABCDEF'
selectors = [True, False, True, False, True, False]

result = compress(data, selectors)
print(list(result)) # ['A', 'C', 'E']
```
***

### Функция `islice`
Функция `islice` позволяет получить срез итерируемого объекта 
```python
from itertools import islice   
   
print(*islice(range(10), None)) # 0 1 2 3 4 5 6 7 8 9  
print(*islice(range(100), 5))   # 0 1 2 3 4 print(*islice(range(100), 5, 10)) # 5 6 7 8 9  
print(*islice(range(100), 0, 100, 10)) # 0 10 20 30 40 50 60 70 80 90
```
***
### Функция `dropwhile`
Функция `dropwhile` начинает возвращать элементы последовательности после того как элемент получит значение False
```python
from itertools import dropwhile   
  
numbers = [1, 1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3]  
new_numbers = list(dropwhile(lambda num: num < 5, numbers))  
print(new_numbers) # [5, 6, 7, 8, 9, 10, 1, 2, 3]
```
***
### Функция `takewhile`
Функция `takewhile` начинает возвращать элементы последовательности до того как будет получено значение False
```python
from itertools import takewhile  
  
new_numbers = list(takewhile(lambda num: num < 5, numbers))  
print(new_numbers) # [1, 1, 2, 3, 4, 4]
```
***
## Функции объединяющие и разделяющие данные
### Функция `chain`
Функция `chain` объединяет в один итератор, все переданные в нее итерируемые последовательности
```python
from itertools import chain  
  
gen_chain = chain([1, 2, 3], ['a', 'b', 'c'], ('Timur', 299, 'Female', 'Dragon Maid'))  
for i in gen_chain:  
    print(i, end=' ') # 1 2 3 a b c Tohru 299 Female Dragon Maid  
    chain_iter2 = chain(enumerate('ABC'))   
print(*chain_iter2) # (0, 'A') (1, 'B') (2, 'C')  
  
# chain.from_iterable Распаковывает вложенные итерируемые объекты  
chain_iter3 = chain.from_iterable(enumerate('ABC'))   
print(*chain_iter3) # 0 A 1 B 2 C
```
  ***
### Функция `zip_longest`
Функция `zip_longest` объединяет элементы в кортежи по самому длинному элементу, к коротким элементам добавляется значение из аргумента
```python
from itertools import zip_longest  
  
print(*zip([1, 2, 3], ['a', 'b', 'c', 'd', 'e']))   
print(*zip_longest([1, 2, 3], ['a', 'b', 'c', 'd', 'e'], fillvalue=None))  
# (1, 'a') (2, 'b') (3, 'c')  
# (1, 'a') (2, 'b') (3, 'c') (None, 'd') (None, 'e')
```
***
### Функция `tee`
Функция tee позволяет создать несколько итераторов на основе одной последовательности. Функция `tee` возвращает кортеж с итераторами.
```python
from itertools import tee  
  
iter1, iter2 = tee(['Senko', 'Holo', 'Vanilla'], 2) # default arg == 2  
print(*iter1, end=' ') # Senko Holo Vanilla  
print(*iter2, end=' ') # Senko Holo Vanilla
```
***
### Функция `pairwise`
Функция `pairwise` создает последовательные перекрывающиеся пары в виде кортежей взятые из итерируемого объекта
```python
from itertools import pairwise  
  
print(*pairwise('ABCDEFG'))  
print(*pairwise([1, 2, 3, 4, 5]))  
# ('A', 'B') ('B', 'C') ('C', 'D') ('D', 'E') ('E', 'F') ('F', 'G')  
# (1, 2) (2, 3) (3, 4) (4, 5)
```
***  
## Функции, группирующие данные
### Функция `groupby`
Функция `groupby` возвращает итератор с кортежами из двух значений
1) Значение характеризующие группу.
2) Итератор с элементами данной группы.
`args: iterable, key: функция вычисляющая значения для группы`
```python
from itertools import groupby  
  
numbers = [1, 1, 1, 7, 7, 7, 7, 15, 7, 7, 7]  
group_iter = groupby(numbers)  
for key, val in group_iter:  
    print(f'{key}: {list(val)}')  
# 1: [1, 1, 1]  
# 7: [7, 7, 7, 7]  
# 15: [15]  
# 7: [7, 7, 7]  
  
# Использование ключа с функцией  
group_iter2 = groupby(numbers, key=lambda num: num < 10)  
for key, val in group_iter2:  
    print(f'{key}: {list(val)}')  
# True: [1, 1, 1, 7, 7, 7, 7]  
# False: [15]  
# True: [7, 7, 7]  
  
# Получить список без повторяющихся элементов  
result = [key for key, group in groupby(numbers)]  
print(result) # [1, 7, 15, 7]  
  
# Получить список с уникальными значениями  
result = [key for key, group in groupby(sorted(numbers))]  
print(result) # [1, 7, 15]
```
***
## Функции для комбинаторных данных
### Функция `permutations`
Функция `permutations` возвращает итератор, который содержит все перестановки из элементов переданного итерируемого объекта. Каждая перестановка заключена в кортеж нужной длины.  
`args: iterable, r - длина возвращаемых кортежей`
```python
from itertools import permutations  
  
numbers = [1, 2, 3]  
letters = 'cba'  
all_num_perm = permutations(numbers)  
all_let_perm = permutations(letters)  
print(list(all_num_perm))  
print(list(all_let_perm))  
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]  
# [('c', 'b', 'a'), ('c', 'a', 'b'), ('b', 'c', 'a'), ('b', 'a', 'c'),  
#  ('a', 'c', 'b'), ('a', 'b', 'c')]
```
***  
### Функция `combinations`
Функция `combinations` возвращает итератор, который содержит все сочетания из элементов переданного итерируемого объекта. Каждое сочетание заключено в кортеж нужной длины.  
`args: iterable, r - длина кортежа`
```python
from itertools import combinations  
  
numbers = [1, 2, 3, 4]  
all_combinations = combinations(numbers, r=2)  
all_combinations2 = combinations(numbers, r=3)  
all_combinations3 = combinations(numbers, r=4)  
print(list(all_combinations))  
print(list(all_combinations2))  
print(list(all_combinations3))  
# [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]  
# [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]  
# [(1, 2, 3, 4)]
```
***
### Функция `combinations_with_replacement`
Функция `combinations_with_replacement` возвращает итератор, который содержит все сочетания из элементов переданного итерируемого объекта с повторами.
`args: iterable, r - длина кортежей`
```python
from itertools import combinations_with_replacement  
  
numbers = [1, 2, 3, 4]  
print(list(combinations_with_replacement(numbers, 1)))  
print(list(combinations_with_replacement(numbers, 2)))  
print(list(combinations_with_replacement(numbers, 3)))  
# [(1,), (2,), (3,), (4,)]  
  
# [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4),  
# (4, 4)]  
  
# [(1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 1, 4), (1, 2, 2), (1, 2, 3), (1, 2, 4),  
#  (1, 3, 3), (1, 3, 4), (1, 4, 4), (2, 2, 2), (2, 2, 3), (2, 2, 4), (2, 3, 3),  
#  (2, 3, 4), (2, 4, 4), (3, 3, 3), (3, 3, 4), (3, 4, 4), (4, 4, 4)]
```
***