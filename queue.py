'''
Очередь - упорядоченная коллекция элементов,
в которой добавление новых происходит с одного конца, 
а удаление существующих - с другого. 
'''
class Queue:

    def __init__(self):
            self.items = []
            
    def isEmpty(self):
            return self.items == []
            
    def enqueue(self, item):
            self.items.insert(0,item)
            
    def dequeue(self):
            return self.items.pop()
            
    def size(self):
            return len(self.items)
