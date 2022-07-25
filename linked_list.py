class Node:
    def __init__(self,data=None, next=None):
        self.data=data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.nil = Node()
        self.nil.next = self.nil
        self.nil.prev = self.nil
        #self.head = self.nil
    
    def search_data(self,value):
        current = self.head
        while current != None and current.data != value:
            current = current.next
        return current
    
    def search2(self, data):
        x = self.nil.next
        while x != self.nil and x.data != data:
            x = x.next
        return x
    
    def insert(self, value):
        newNode = Node(value)
        newNode.next = self.head
        if self.head != None:
            self.head.prev = newNode
        self.head = newNode
        newNode.prev = None
    
    def insert2(self,data):
        newNode = Node(data)
        newNode.next = self.nil.next
        self.nil.next.prev = newNode
        self.nil.next = newNode
        newNode.prev = self.nil
    
    def delete(self, node):
        if node.prev != None:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next != None:
            node.next.prev = node.prev
    
    def delete2(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del node
    
    def printLL(self):
        current = self.nil.next
        while current != self.nil:
            print(current.data)
            current = current.next
    
    # Function without the self.lil


if __name__=='__main__':
    LL = LinkedList()
    LL.insert2(1)
    LL.insert2(2)
    node = LL.search2(2)
    LL.delete2(node)
    LL.insert2(3)
    LL.printLL()