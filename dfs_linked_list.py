class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Graph:
    def __init__(self):
        self.graph = {}  

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = None
        if v not in self.graph:
            self.graph[v] = None

        node_u = Node(v)
        node_u.next = self.graph[u]
        self.graph[u] = node_u

        node_v = Node(u)
        node_v.next = self.graph[v]
        self.graph[v] = node_v

    def dfs(self, start):
        visited = set()
        result = []

        def dfs_util(u):
            visited.add(u)
            result.append(u)
            temp = self.graph.get(u)
            while temp:
                if temp.val not in visited:
                    dfs_util(temp.val)
                temp = temp.next

        if start in self.graph:
            dfs_util(start)
        return result

E = int(input("Enter number of edges: "))
g = Graph()

print("Enter edges (any labels, e.g., A B or 1 2):")
for _ in range(E):
    u, v = input().split()
    g.add_edge(u, v)

start_node = input("Enter starting node for DFS: ")
print("DFS traversal:", g.dfs(start_node))
