class Graph:
    def __init__(self,A):
        self.A = A
        self.V = len(A)
    def describe_graph(self):
        nodes= len(self.A)
        edges=0
        for i in range(nodes):
            for j in range(len(self.A[i])):
                if self.A[i][j] == 1:
                    edges+=1
        print(f"There are {nodes} nodes and {edges} edges in this graph")

    def dfsearch(self):
        nodes = len(self.A)
        mark = [0] * nodes
        visited_order = []
        def _dfs(n):
            mark[n] = 1
            visited_order.append(n)
            for j in range(len(self.A[n])):
                if self.A[n][j] == 1 and mark[j] == 0:
                    _dfs(j)

        for n in range(nodes):
            if mark[n] == 0:
                _dfs(n)

        print(f"DFS traversal order: {visited_order}")




g = [[0,0,1,0],[0,1,0,1],[1,0,0,1],[0,1,1,0]]
graph = Graph(g)
graph.describe_graph()
graph.dfsearch()
