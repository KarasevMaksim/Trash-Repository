# Момоизация для функции ======================================================
# Сохранение рузультатов выполненеия функции в cache для уменьшения размер
# стека. Мы возвравщаем результат из кеша, чтобы не вычислять его повторно.
def fib(n):
    cache = {1: 1, 2: 1}
    def fib_rec(n):
        result = cache.get(n)
        if result is None:
            result = fib_rec(n - 2) + fib_rec(n - 1)
            cache[n] = result
        return result
    return fib_rec(n)
    
# Общий декоратор для кеширования функции
import functools

def simple_cached(func):
    cache = dict()
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = args + tuple(kwargs.items())
        result = cache.get(key)
        if result is None:
            result = func(*args, **kwargs)
            cache[key] = result
        else:
            print('Возвращаем значение из кеша')
        return result
    return wrapper

@simple_cached
def sum_ab(a, b):
    return a + b

# if __name__ == '__main__':
#     sum_ab(2, 2)
#     sum_ab(2, 2)
#     sum_ab(2, 2)
#     sum_ab(2, 4)
#     sum_ab(2, 4) # значение из кеша вернется 3 раза
    
# куширование из functools ====================================================    
'''
 Стратегия                Какую запись удаляем          Эти записи чаще других
                                                        используются повторно 
                                                         
First-In, First-Out
 (FIFO)                   самую старую                  новые
 
 Last-In, First-Out
 (LIFO)                   самую недавнюю                старые
 
 Least Recently Used      которая использовалась        недавно прочитанные
 (LRU)                    наиболее давно
                          
 Most Recently Used       которая использовалась        прочитанные первыми
 (MRU)                    последней
 
 Least Frequently         которая использовалась        которые использовались
 Used (LFU)               наиболее редко                часто
'''
from functools import lru_cache

@lru_cache(typed=True, maxsize=128)
def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Отслеживание работы lru_cache
'''
 hits – количество значений, которые lru_cache вернул непосредственно из памяти,
 поскольку они присутствовали в кэше
 misses – количество значений, которые были вычислены, а не взяты из памяти
 maxsize – это размер кэша, который мы определили, передав его декоратору
 currsize – текущий размер кэша
'''

if __name__ == '__main__':
    fibonacci(20)
    print(fibonacci.cache_info())
    fibonacci.cache_clear() # очистка кеша
    