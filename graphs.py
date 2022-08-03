from collections import deque

class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None
        # BFS fields
        #self.color = "WHITE"
        #self.d = 2147483647
        #self.predecessor = None

class VerctorBFS:
    def __init__(self):
        self.vertex = None
        self.color = "WHITE"
        self.d = 2147483647
        self.predecessor = None

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V
        self.bfs_fields = None
    
    def verify_adj_list(self, graph_source, key):
        node = self.graph[graph_source]
        while node:
            if node.vertex == key:
                return False
            node = node.next
        return True
    
    def add_edge(self, src, dest):
        can_create = self.verify_adj_list(src, dest)
        if can_create:
            node = AdjNode(dest)
            node.next = self.graph[src]
            self.graph[src] = node

        can_create = self.verify_adj_list(dest, src)
        if can_create:
            node = AdjNode(src)
            node.next = self.graph[dest]
            self.graph[dest] = node
    
    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i)),
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex)),
                temp = temp.next
            print(" \n")
    
    def bfs(self, graph_source):
        bfs_fields = []
        for i in self.graph:
            node = VerctorBFS()
            bfs_fields.append(node)
        bfs_fields[graph_source].vertex = graph_source
        bfs_fields[graph_source].color = "GRAY"
        bfs_fields[graph_source].d = 0
        bfs_fields[graph_source].predecessor = None
        queue = deque()
        queue.append(bfs_fields[graph_source])
        while queue:
            u1 = queue.popleft()
            v1 = self.graph[u1.vertex]
            while v1:
                if bfs_fields[v1.vertex].color == "WHITE":
                    #import pdb; pdb.set_trace()
                    bfs_fields[v1.vertex].color = "GRAY"
                    bfs_fields[v1.vertex].d = bfs_fields[u1.vertex].d + 1
                    bfs_fields[v1.vertex].predecessor = u1
                    queue.append(v1)
                v1 = v1.next
            bfs_fields[u1.vertex].color = "BLACK"
        self.bfs_fields = bfs_fields
        
        


if __name__=='__main__':
    V = 7
    graph = Graph(V)

    #graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(2, 4)
    graph.add_edge(4, 5)
    graph.add_edge(5, 6)

    graph.print_graph()

    graph.bfs(1)
    import pdb; pdb.set_trace()