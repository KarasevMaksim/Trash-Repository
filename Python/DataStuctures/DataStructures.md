# Стек LIFO

Стек LIFO - Последний пришел, первый вышел. Реализуется через односвязный список.

## Возможные операции:

- **Добавление элемента**: O(1)
- **Получение элемента**: O(1)
- **Просмотр элемента**: O(1)
- **Получение размера**: O(1)
- **Проверка на пустоту**: O(1)

## Описание реализации:

Класс `Stack` хранит ссылку на последнюю добавленную ноду в `head`, в свою очередь, данная нода хранит ссылку на предыдущую ноду в `link` и так далее. Последняя нода, которая была добавлена самой первой, хранит ссылку на объект `None`.

```python
class NodeForStack:
    '''Класс для представления узла стека.'''
    def __init__(self, data):
        self._data = data
        self._link = None
        
        
class Stack:
    def __init__(self):
        self.__head = None
        self.__count_item = 0
        
    def add_item(self, data):
        new_node = NodeForStack(data)  # Создаем новый узел Node с переданными данными.
        new_node._link = self.__head  # Записываем в ссылку данной ноды, предыдущую ноду из head. Если ее не было, туда запишется объект None.
        self.__head = new_node  # head теперь ссылается на данную ноду.
        self.__count_item += 1  # Обновляем количество созданных объектов Node.
        
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
