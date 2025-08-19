def depth_limited_search(graph, start, goal, limit):
    def recursive_dls(node, depth):
        if depth > limit:
            return None
        if node == goal:
            return [node]
        for neighbor in graph.get(node, []):
            path = recursive_dls(neighbor, depth + 1)
            if path:
                return [node] + path
        return None

    return recursive_dls(start, 0)


def get_graph_input():
    graph = {}
    num_nodes = int(input("Enter number of nodes: "))
    for _ in range(num_nodes):
        node = input("Enter node name: ")
        neighbors = input(f"Enter neighbors of {node} (comma-separated): ").split(',')
        graph[node] = [n.strip() for n in neighbors if n.strip()]
    return graph


if __name__ == "__main__":
    graph = get_graph_input()
    start = input("Enter start node: ")
    goal = input("Enter goal node: ")
    limit = int(input("Enter depth limit: "))

    path = depth_limited_search(graph, start, goal, limit)
    if path:
        print(" Path found:", " -> ".join(path))
    else:
        print(" No path found within the depth limit.")
