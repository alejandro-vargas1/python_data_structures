import queue


class Queue:
    def __init__(self):
        self.queue = []
        self.head = 0
        self.tail = 0
    
    def queue_empty(self):
        if len(self.queue) < 1:
            return True
        else: 
            return False
    
    def enqueue(self, value):
        self.queue.append(value)
    
    def dequeue(self):
        if self.queue_empty():
            raise ValueError("It's empty")
        else:
            return self.queue.pop(0)

if __name__=='__main__':
    queue = Queue()
    import pdb; pdb.set_trace()