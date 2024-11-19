# Генератор простых чисел =====================================================
def primes():
    count = 2
    while True:
        check = all((True if count % i else False for i in range(2, count)))
        if check:
            yield count
        count += 1

# if __name__ == '__main__':
#     x = primes()        
#     for _ in range(31):
#         print(next(x), end=' ')
        
# reverse generator ===========================================================
def reverse_generator(iter_obj):
    index = len(iter_obj) - 1
    while index >= 0:
        yield iter_obj[index]
        index -= 1
        
# if __name__ == '__main__':
#     gen = reverse_generator([1, 2, 3])
#     print(next(gen))
#     print(next(gen))
#     print(next(gen))

# Синтаксическая констркция yield from ========================================
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

# if __name__ == '__main__':
#     for i in gen1():
#         print(i, end=' ') # Good girl This Senko Holo Kawai!

# Рекурсивные генератонры =====================================================
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
