#cache #python #кеш #кеширование #memo #мемоизация
# Кеширование в Python
## Мемоизация для функций
### Описание:
Сохранение результатов выполнения функции в cache для уменьшения размера стека. Мы возвращаем результат из кеша, чтобы не вычислять его повторно.
```python
def fib(n):
	cache = {1: 1, 2: 1}
	def fib_rec(n):
		result = cache.get(n)
		if result is None:
			result = fib_rec(n - 2) + fib_rec(n - 1)
			cache[n] = result
		return result
	return fib_rec(n)
```
***
## Общий шаблон своего декоратора для кеширования функций
```python
import functools

def simple_cached(func):
	cache = dict()
	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		key = args + tuple(kwargs.items())
		result = cache.get(key)
		if result is None:
			result= func(*args, **kwargs)
			cache[key] = result
		else:
			print('Возвращаем значение из кеша!')
		return result
	return wrapper

@simple_cached
def sum_ab(a, b):
	return a + b

if __name__ == '__main__':
	sum_ab(2, 2)
	sum_ab(2, 2)
	sum_ab(2, 2)
	sum_ab(2, 4)
	sum_ab(2, 4)
	# Значение из кеша вернется 3 раза
```
***
## Различные методы реализации кеширования

| Стратегия                        | Какую запись удаляем                     | Эти записи чаще других <br>используются повторно |
| -------------------------------- | ---------------------------------------- | ------------------------------------------------ |
| First-In, First-Out  <br> (FIFO) | Самую старую                             | Новые                                            |
| Last-In, First-Out  <br>(LIFO)   | Самую недавнюю                           | Старые                                           |
| Least Recently Used <br>(LRU)    | Которая использовалась<br>наиболее давно | Недавно прочитанные                              |
| Most Recently Used<br>(MRU)      | Которая использовалась<br>последней      | Прочитанные первыми                              |
| Least Frequently Used<br>(LFU)   | Которая использовалась<br>наиболее редко | Которые использовались<br>част                   |
***
## Кеширование из модуля `functools`
### Описание:
В модуле `functools` есть декоратор для кеширования посредством метода `LRU`. 
```python
form functools import lru_cache

@lru_cache(typed=True, maxsize=128)
def fibonacci(n):
	if n <= 2:
		return 1
	else:
		return fibonacci(n - 1) + fibonacci(n - 2)
```
Отслеживание работы `lru_cache`
`hits` - количество значений, которые `lru_cache` вернул непосредственно из памяти, поскольку они присутствовали в кеше.
`misses` - количество значений, которые были вычислены, а не взяты из памяти.
`maxsize` - это размер кеша, который мы определили, передав его декоратору.
`currsize` - текущий размер кеша.
```python
if __name__ == '__main__':
	fibonacci(20)
	print(fibonacci.cache_info())
	fibonacci.cache_clear() # очистка кеша
```
***