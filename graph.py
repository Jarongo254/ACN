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

    def dfsearch(self, mode="recursive"):
        nodes = len(self.A)
        mark = [0] * nodes
        visited_order = []
        def _dfs(n):
            mark[n] = 1
            visited_order.append(n)
            for j in range(len(self.A[n])):
                if self.A[n][j] == 1 and mark[j] == 0:
                    print(f"Performing dfs on node {j}")
                    _dfs(j)

        def _dfs2(v):
            P = [] # empty stack
            mark[v] = 1
            P.append(v)
            visited_order.append(v)
            while P:
                top = P[-1]
                found_unvisited = False
                for j in range(len(self.A[top])):
                    if self.A[top][j] == 1 and mark[j] == 0:
                        print(f"marking {j} as visited")
                        mark[j] = 1
                        P.append(j)
                        print(f"pushed {j} to stack. New Stack: {P}")
                        visited_order.append(j)
                        found_unvisited = True
                if not found_unvisited:
                    print(f"Stack: {P}. popping stack")
                    P.pop()
                    print(f"New Stack: {P}")

        for n in range(nodes):
            if mark[n] == 0:
                print(f"Performing {mode} dfs on node {n}")
                if mode == "recursive":
                    _dfs(n)
                elif mode == "iterative":
                    _dfs2(n)


        print(f"DFS traversal order: {visited_order}")




g = [[0,0,1,0],[0,1,0,1],[1,0,0,1],[0,1,1,0]]
graph = Graph(g)
graph.describe_graph()
graph.dfsearch(mode="recursive")
graph.dfsearch(mode="iterative")
