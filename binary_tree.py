from re import X
from xxlimited import new


class Node:
    def __init__(self):
        self.parent = None
        self.right = None
        self.left = None
        self.data = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def inorder_tree_walk(self, node):
        if node != None:
            self.inorder_tree_walk(node.left)
            print(node.data)
            self.inorder_tree_walk(node.right)
    
    def recursive_tree_search(self, node, key):
        if node != None or key != node.data:
            return node
        if key < node.data:
            return self.recursive_tree_search(node.left, key)
        else:
            return self.recursive_tree_search(node.right, key)
    
    def iterative_tree_search(self, node, key):
        while node != None and key != node.data:
            if key < node.data:
                node = node.left
            else:
                node = node.right
        return node
    
    def minimum(self, node):
        while node.left != None:
            node = node.left
        return node
    
    def maximum(self, node):
        while node.right != None:
            node = node.right
        return node
    
    def tree_successor(self, node):
        if node.right != None:
            return self.minimum(node.right)
        y = node.parent
        while y != None and node == y.right:
            node = y
            y = y.parent
        return y
    
    # Need to write tree predecessor
    def tree_predeccessor(self, node):
        if node.left != None:
            return self.maximum(node.left)
        y = node.parent
        while y != None and node == y.left:
            node = y
            y = y.parent
        return y

    def tree_insert(self, value):
        newNode = Node()
        newNode.data = value
        y = None
        x = self.root
        while x != None:
            y = x
            if newNode.data < x.data:
                x = x.left
            else:
                x = x.right
        newNode.parent = y
        if y == None:
            self.root = newNode
        elif newNode.data < y.data:
            y.left = newNode
        else:
            y.right = newNode
    
    def transplant(self, u, v):
        # v nodo hijo a subir de posicion
        # u nodo padre que va a ser eliminado
        
        if u.parent == None: #En caso de que u sea el nodo raiz
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v != None:
            v.parent = u.parent
    
    def tree_delete(self, z):
        if z.left == None:
            self.transplant(z, z.right)
        elif z.right == None:
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            if y.parent != z:
                self.transplant(y,y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z,y)
            y.left = z.left
            y.left.parent = y
        

if __name__=='__main__':
    tree = BinaryTree()
    import pdb; pdb.set_trace()