# Примеры использования и создания итераторов.
## Чтение файлов черз итератор.
Использование функции `iter()` с параметром для `StopIteration` (можно
испльзовать для чтения файла, до определенной строки). Первый аргумент
должен быть вызываемым (функция и.т.п)
```python
# Создаем файл с несколькими строками
with open('example.txt', 'w') as f:
    f.write("Hello\n")
    f.write("World\n")
    f.write("This is a test.\n")
    f.write("Goodbye\n")
# Функция для чтения строк из файла
def read_line():
    return file.readline().strip()
# Открываем файл для чтения
file = open('example.txt')
# Создаем итератор, который будет читать строки до тех пор,
# пока не достигнет пустой строки
iterator = iter(read_line, '')
for line in iterator:
    print(line)
file.close()
```

# Counter iterator
```python
class Counter:
    def __init__(self, low, high):
        self.low = low - 1
        self.high = high
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.low < self.high:
            self.low += 1
            return self.low
        raise StopIteration
    
if __name__ == '__main__':
    counter = Counter(3, 10)
    for i in counter:
        print(i)
```
# fibonacci iterator
```python
class FibonacciIterator:
    def __init__(self):
        self.num1 = -1
        self.num2 = 1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        res = self.num1 + self.num2
        self.num1 = self.num2
        self.num2 = res
        return res
    
if __name__ == '__main__':
    fibonacci = FibonacciIterator() 
    print(next(fibonacci))
    print(next(fibonacci)) 
    print(next(fibonacci)) 
    print(next(fibonacci))
```
