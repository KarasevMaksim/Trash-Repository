#python #generator #iterator #iteration #итератор #генератор
# Пример создания функции `Multifilter` с помощью итератора и генератора
### Описание:
Данная функция это расширенная версия обычной встроенной функции `filter`. Здесь при фильтрации мы можем передать в аргумент выбор дополнительного метода, для осуществления дополнительной фильтрации.
***
## Вариант 1 через итератор
```python
class multifilter:  
    def __init__(self, iterable, *funcs, judge=None):  
        self.index = 0  
        self.iterable = iterable  
        self.funcs = funcs  
        self.judge = judge if judge else multifilter.judge_any  
  
    def judge_half(pos, neg):  # (pos >= neg)  
        return pos >= neg  
    def judge_any(pos, neg):  # (pos >= 1)  
        return pos >= 1  
    def judge_all(pos, neg):  # (neg == 0)  
        return neg == 0  
  
    def __logic(self, item):  
        pos = 0  
        neg = 0  
        for func in self.funcs:  
            if func(item):  
                pos += 1  
            else:  
                neg += 1  
        return pos, neg  
  
    def __iter__(self):  
        return self  
  
    def __next__(self):  
        while self.index < len(self.iterable):  
            item = self.iterable[self.index]  
            pos, neg = self.__logic(item)  
            self.index += 1  
            if self.judge(pos, neg):  # Теперь вызываем self.judge  
                return item  
        raise StopIteration  
  
def mul2(x):  
    return x % 2 == 0  
def mul3(x):  
    return x % 3 == 0  
def mul5(x):  
    return x % 5 == 0  
a = [i for i in range(31)]  
print(list(multifilter(a, mul2, mul3, mul5)))  
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
```
***
## Вариант 2 через генератор
```python
class multifilter:  
    def __init__(self, iterable, *funcs, judge=None):  
        self.iterable = iterable  
        self.funcs = funcs  
        # Если judge не передан, используем judge_any по умолчанию  
        self.judge = judge if judge else self.judge_any  
  
    def judge_half(self, pos, neg):  # (pos >= neg)  
        return pos >= neg  
  
    def judge_any(self, pos, neg):  # (pos >= 1)  
        return pos >= 1  
  
    def judge_all(self, pos, neg):  # (neg == 0)  
        return neg == 0  
  
    def __logic(self, item):  
        pos = 0  
        neg = 0  
        for func in self.funcs:  
            if func(item):  
                pos += 1  
            else:  
                neg += 1  
        return pos, neg  
  
    def __iter__(self):  
        for item in self.iterable:  
            pos, neg = self.__logic(item)  
            if self.judge(pos, neg):  # Теперь вызываем self.judge  
                yield item  # Используем yield для возврата элемента
```
***