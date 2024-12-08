'''
Стек LIFO - Последний пришел, первый вышел.
Реализуется черз односвязный список.
Возможные операции:
Добавление элемента O(1)
Получение элемента  O(1)
Просмотр элемента   O(1)
Получение размера   O(1)
Проверка на пустоту O(1)

Описание реализации:
Класс Stack хранит ссылку на последнюю добавленную ноду в head, в свою очередь,
данная нода хранит ссылку на пердыдущую ноду в link и так далее. Последняя
нода, которая была добавлена самой первой, хранит ссылку на объект None.
'''


class NodeForStack:
    '''Класс для предостовления узла стека.'''
    def __init__(self, data):
        self._data = data
        self._link = None
        
        
class Stack:
    def __init__(self):
        self.__head = None
        self.__count_item = 0
        
    def add_item(self, data):
        new_node = NodeForStack(data) # Создаем новый узел Node с переданными
        # данными.
        new_node._link = self.__head # Записываем в ссылку данной ноды,
        # предыдущую ноду из head. Если ее небыло, туда запишется объект None.
        self.__head = new_node # head теперь ссылается на данную ноду.
        self.__count_item += 1 # Обновляем количество созданных объектов Node.
        
    def delete(self):
        node = self.__head
        if node:
            self.__head = node._link
            self.__count_item -= 1
            del node
    
    def get_item(self):
        node = self.__head
        if node:
            data = node._data
            self.__head = node._link
            del node
            self.__count_item -= 1
            return data
        else:
            return None
    
    def top_item(self):
        node = self.__head
        if node:
            return node._data
        else:
            return None
    
    def size_stack(self):
        return self.__count_item
    
    def is_empty(self):
        return True if not self.__head else False


'''
Односвязный список Singly linked list
Возможные операции:
Итерирование по елементам            O(n)
Добавление элемента в начало списка  O(1)
Добавление элемента в конец списка   O(n)
Добавление элемента в середину
списка, при условии наличия ссылки   O(1)
Получение элемента из начала списка  O(1)
Получение элемента из конца списка   O(n)
Получение элемента по индексу        O(n)
Получение размера списка             O(1)
Удаление элемента из начала списка   O(1)
Удаление элемента из конца списка    O(n) 
'''
class NodeForSinglyList:
    def __init__(self, data):
        self._data = data
        self._next_link = None
        
        
class SinglyList:
    def __init__(self):
        self.__head = None
        self.__count_items = 0
        

    def insert(self, data, index=None):
        if not index:
            new_node = NodeForSinglyList(data)
            new_node._next_link = self.__head
            self.__head = new_node
        self.__count_items += 1
        
    def insert_after_node(self, node, data):
        new_node = NodeForSinglyList(data)
        new_node._next_link = node._next_link
        node._next_link = new_node
        self.__count_items += 1

        
    def append(self, data):
        new_node = NodeForSinglyList(data)
        head = self.__head
        if head:
            while head._next_link:
                head = head._next_link
            head._next_link = new_node
        else:
            self.__head = new_node
        self.__count_items += 1
            
    
    def __getitem__(self, index):
        # Проверка на пустой список
        if self.__head is None:
            raise IndexError('Список пуст')

        # Обработка положительных индексов
        if index >= 0:
            if index >= self.__count_items:
                raise IndexError('Индекс вне диапазона')
        
            node = self.__head
            for _ in range(index):
                node = node._next_link
            return node._data

        # Обработка отрицательных индексов
        else:
            if abs(index) > self.__count_items:
                raise IndexError('Индекс вне диапазона')

            # Преобразование отрицательного индекса в положительный
            index = self.__count_items + index  # -1 станет (count_items - 1)
            node = self.__head
            for _ in range(index):
                node = node._next_link
            return node._data
        
    def __len__(self):
        pass
    
    def __iter__(self):
        pass
    
    def __next__(self):
        pass
    
    def __del__(self):
        pass


    def __repr__(self):
        if self.__head is None:
            return 'class SinglyList()'
        
        string = ''
        head = self.__head
        while head._next_link:
            data = head._data
            string += str(data) + ', '
            head = head._next_link
        return f'class SinglyList({string + str(head._data)})'
    
    
lst = SinglyList()
lst.insert(4)
lst.insert(5)
lst.append(6)
lst.append(7)
lst.insert(666)
lst.append(777)
print(lst)
print(lst[-6])