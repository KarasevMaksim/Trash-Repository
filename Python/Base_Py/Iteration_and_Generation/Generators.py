# Генератор простых чисел =====================================================
def primes():
    count = 2
    while True:
        check = all((True if count % i else False for i in range(2, count)))
        if check:
            yield count
        count += 1


x = primes()        
for _ in range(31):
    print(next(x), end=' ')
