def dfs_all_edges(graph):
    visited = set()
    res = []
    for node in graph:
        if node not in visited:
            stack = [node]
            while stack:
                curr = stack.pop()
                if curr in visited:
                    continue
                visited.add(curr)
                res.append(curr)
                stack.extend(reversed(graph.get(curr, [])))
    return res

V = int(input("Number of vertices: "))
e = int(input("Number of edges: "))
graph = {}
edges = []

print("Enter edges as pairs of integers (e.g., 1 2):")
for i in range(e):
    u, v = map(int, input().split())
    edges.append((u, v))
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)

print("Visited nodes:", dfs_all_edges(graph))
