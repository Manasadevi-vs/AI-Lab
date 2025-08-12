from collections import deque

def bfs_all_edges(graph):
    visited = set()
    res = []

    for node in graph:
        if node not in visited:
            queue = deque([node])
            visited.add(node)
            while queue:
                curr = queue.popleft()
                res.append(curr)
                for neighbor in graph.get(curr, []):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
    return res

E = int(input("Enter number of edges: "))
graph = {}

print("Enter each edge as two space-separated labels (e.g., A B or 1 2):")
for _ in range(E):
    u, v = input().split()
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)  

print("Visited nodes in BFS order:", bfs_all_edges(graph))
