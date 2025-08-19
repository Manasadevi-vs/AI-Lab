def iterative_dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = set()

    while stack:
        current, path = stack.pop()

        if current == goal:
            return path

        if current not in visited:
            visited.add(current)
            for neighbor in reversed(graph.get(current, [])):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

    return None

# 🛠️ Build the graph from user input
def build_graph():
    graph = {}
    num_nodes = int(input("Enter number of nodes: "))
    for _ in range(num_nodes):
        node = input("Enter node name: ")
        neighbors = input(f"Enter neighbors of {node} (comma-separated): ").split(',')
        graph[node] = [n.strip() for n in neighbors if n.strip()]
    return graph

# 🚀 Main execution
if __name__ == "__main__":
    graph = build_graph()
    start = input("Enter start node: ")
    goal = input("Enter goal node: ")

    path = iterative_dfs(graph, start, goal)
    if path:
        print("Path found:", " -> ".join(path))
    else:
        print("No path found from", start, "to", goal)
