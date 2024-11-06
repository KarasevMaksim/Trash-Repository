import time

class Loggable:
    def log(self, msg):
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
        
        
        
x = LoggableList()
x.append(10)
print(x)