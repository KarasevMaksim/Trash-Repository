#python #ООП #mixin
# Реализация Mixin паттерна
## List Mixin
### Описание:
Создаем новый класс с расширенными возможностями стандартного класса `List`.
```python
import time


class Loggable:
	def log(slef, msg):
		print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
	def append(self, value):
		list.append(self, value)
		# or super().append(value)
		# or super(LoggableList, self).append(value)
		self.log(value)
		# or super().log(value)
		# or super(Loggable, self).log(value)
		# or Loggable.log(self, value)

if __name__ == '__main__':
	x = LoggableList()
	x.append(10)
	print(x)
```
***