import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))
        
        
        
class LoggableList(list, Loggable):
    def append(self, value):
        list.append(self, value)
        self.log(value)
        
        
        
x = LoggableList()
x.append(10)
print(x)