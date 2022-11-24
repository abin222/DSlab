class Graph:
    def __init__(self):

        self.gdict = {}

    def add_Vertex(self,vertex):
        if vertex not in self.gdict.keys():
            self.gdict[vertex] = []
            return True
        return False
    def print_graph(self):
        for vertex in self.gdict:
            print(vertex,":",self.gdict[vertex])

    def add_edge(self,vertex1,vertex2):
        if vertex1 in self.gdict.keys() and vertex2 in self.gdict.keys():
            self.gdict[vertex1].append(vertex2)
            self.gdict[vertex2].append(vertex1)
            return True
        return False

    def add_remove(self,vertex1,vertex2):
        if vertex1 in self.gdict.keys() and vertex2 in self.gdict.keys():
            self.gdict[vertex1].remove(vertex2)
            self.gdict[vertex2].remove(vertex1)
            return True
        return False

    def remove_vertex(self,vertex):
        if vertex in self.gdict.keys():
            for other in self.gdict[vertex]:
                self.gdict[other].remove(vertex)
            del self.gdict[vertex]
            return True
        return False

    def bfs(self,vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:
            deVertex = queue.pop(0)
            print(deVertex)
            for adj in self.gdict[vertex]:
                if adj not in visited:
                    visited.append(adj)
                    queue.append(adj)

    def dfs(self,vertex):
        visited = [vertex]
        stack  = [vertex]
        while stack:
            deVertex = stack.pop()
            print(deVertex)
            for adj in self.gdict[vertex]:
                if adj not in visited:
                    visited.append(adj)
                    stack.append(adj)








g = Graph()
g.add_Vertex("A")
g.add_Vertex("B")
g.add_Vertex("C")
g.add_Vertex("D")
g.add_edge("A","B")
g.add_edge("A","C")
g.add_edge("A","D")
g.add_edge("B","C")
g.add_edge("C","D")
g.print_graph()
g.remove_vertex("D")
print("After removal")
g.print_graph()
print("BFS")
g.bfs("A")
print("DFS")
g.dfs("A")

