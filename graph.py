class Graph:
    def __init__(self,A):
        self.A = A
        self.V = len(A)
    def describe_graph(self):
        nodes= self.V
        edges=0
        for i in range(nodes):
            for j in range(len(self.A[i])):
                if self.A[i][j] == 1:
                    edges+=1
        edges //=2
        #print(f"There are {nodes} nodes and {edges} edges in this graph")

    def dfsearch(self, mode="recursive"):
        nodes = self.V
        mark = [0] * nodes
        pre_order = []
        post_order = []
        tree_edges = []
        def _dfs(n):
            mark[n] = 1
            pre_order.append(n)
            for j in range(len(self.A[n])):
                if self.A[n][j] == 1 and mark[j] == 0:
                    #print(f"Performing dfs on node {j}")
                    tree_edges.append((n,j))
                    _dfs(j)
            post_order.append(n)

        def _dfs2(v):
            P = [] # empty stack
            mark[v] = 1
            P.append(v)
            pre_order.append(v)
            while P:
                top = P[-1]
                found_unvisited = False
                for j in range(len(self.A[top])):
                    if self.A[top][j] == 1 and mark[j] == 0:
                        #print(f"marking {j} as visited")
                        mark[j] = 1
                        P.append(j)
                        #print(f"pushed {j} to stack. New Stack: {P}")
                        tree_edges.append((top,j))
                        pre_order.append(j)
                        found_unvisited = True
                        break
                if not found_unvisited:
                    #print(f"Stack: {P}. popping stack")
                    post_order.append(top)
                    P.pop()
                    #print(f"New Stack: {P}")

        for n in range(nodes):
            if mark[n] == 0:
                #print(f"Performing {mode} dfs on node {n}")
                if mode == "recursive":
                    _dfs(n)
                elif mode == "iterative":
                    _dfs2(n)

        return pre_order, post_order, tree_edges
        #print(f"DFS traversal order(pre-order): {pre_order}")
        #print(f"DFS tree edges: {tree_edges}")
        #print(f"Post order: {post_order}")

    def bfsearch(self):
        nodes = len(self.A)
        mark = [0] * nodes
        pre_order = []
        def _bfs(v):
            Q = [] # empty queue
            #print(f"marking {v} as visited")
            mark[v] = 1 # mark node as visited
            Q.append(v)
            #print(f"enqueued {v}. New Queue: {Q}")
            pre_order.append(v)
            while Q:
                u = Q[0]
                Q.pop(0)
                #print(f"popping {u}. Queue is now {Q}")
                for j in range(len(self.A[u])):
                    if self.A[u][j] == 1 and mark[j] == 0:
                        #print(f"marking {j} as visited")
                        mark[j] = 1
                        Q.append(j)
                        #print(f"enqueued {j}. New Queue: {Q}")
                        pre_order.append(j)
        for v in range(nodes):
            if mark[v] == 0:
                #print(f"Performing bfs on node {v}")
                _bfs(v)
        #print(f"BFS traversal order: {pre_order}")

    def art_point(self):
        pre_order, post_order, tree_edges = self.dfsearch()
        print(f"pre-order: {pre_order}\npost-order: {post_order}")
        print(f"tree-edges: {tree_edges}")

        art_points = []
        parent = [-1] * self.V
        pre = [-1] * self.V
        tree_set = set(tree_edges)

        for u,v in tree_edges:
            parent[v] = u

        for i, v in enumerate(pre_order):
            pre[v] = i

        low = pre.copy()

        for v in range(self.V):
            for j in range(self.V):
                if self.A[v][j] == 1:
                    if (v,j) not in tree_set and (j,v) not in tree_set:
                        if pre[j] < pre[v]:
                            print("back edge:", v, "->", j)
                            low[v] = min(low[v],pre[j])

        for v in post_order:
            if parent[v] != -1:
                p = parent[v]
                low[p] = min(low[p], low[v])

        for u, v in tree_edges:
            if parent[u] == -1:  # then u is  root
                continue

            if low[v] >= pre[u]:
                if u not in art_points:
                    art_points.append(u)

        root = pre_order[0]
        children = 0

        for u,v in tree_edges:
            if u == root:
                children += 1

        if children > 1:
            art_points.append(root)

        for v in range(self.V):
            print(v, "parent =", parent[v], "pre =", pre[v], "low =", low[v])

        print(f"\nArticulation points: {art_points}")

    def is_graphic(self,mode="Erdos-Gallai"):
        degrees = []
        for v in range(self.V): # using an adjacency list would reduce the double for loop (lower complexity)
            degree = 0
            for j in range(self.V):
                if self.A[v][j] == 1:
                    degree += 1
            degrees.append(degree)
            print(f"Node {v}: degree {degree}")
        degree_sequence = sorted(degrees, reverse=True)
        ds = degree_sequence.copy()

        def _havel_hakimi(degree_sequence):
            while degree_sequence:
                degree_sequence.sort(reverse=True)
                first = degree_sequence.pop(0)

                if first > len(degree_sequence):
                    return False

                for i in range(first):
                    degree_sequence[i] -= 1
                    if degree_sequence[i] < 0:
                        return False
            return True

        def _erdos_gallai(degree_sequence):
            if sum(degree_sequence )% 2 != 0:
                return False

            for k in range(1, len(degree_sequence) + 1):
                sub_sum1 = sum(degree_sequence[:k])
                sub_sum2 = sum(min(d,k) for d in degree_sequence[k:])
                if sub_sum1 >  k*(k-1) + sub_sum2:
                    return False

            return True

        if mode=="Havel-Hakimi":
            if _havel_hakimi(degree_sequence):
                print(f"Degree sequence {ds} is graphic")
            else:
                print(f"Degree sequence {ds} is NOT graphic")

        if mode == "Erdos-Gallai":
            if _erdos_gallai(degree_sequence):
               print(f"Degree sequence {ds} is graphic")
            else:
                print(f"Degree sequence {ds} is NOT graphic")


g = [
    [0, 1, 1, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 1, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 1, 0],
]
graph = Graph(g)
#graph.describe_graph()
#graph.dfsearch(mode="recursive")
#graph.dfsearch(mode="iterative")
#graph.bfsearch()
#graph.art_point()
graph.is_graphic()
