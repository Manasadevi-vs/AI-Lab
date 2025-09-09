import heapq

def a_star(graph, start, goal, heuristic):
    open_set = [(heuristic[start], start, [start], 0)]
    visited = set()

    while open_set:
        f_score, current, path, g_score = heapq.heappop(open_set)

        if current == goal:
            return path, g_score

        if current in visited:
            continue
        visited.add(current)

        for neighbor, cost in graph.get(current, {}).items():
            if neighbor in visited:
                continue
            new_g = g_score + cost
            new_f = new_g + heuristic.get(neighbor, float('inf'))
            heapq.heappush(open_set, (new_f, neighbor, path + [neighbor], new_g))

    return None, float('inf')


def get_input():
    graph = {}
    heuristic = {}

    num_nodes = int(input("Enter number of nodes: "))
    print("Enter node names:")
    nodes = [input(f"Node {i+1}: ") for i in range(num_nodes)]

    print("\nEnter edges and costs (format: from to cost). Type 'done' to finish:")
    while True:
        edge = input()
        if edge.lower() == 'done':
            break
        u, v, cost = edge.split()
        cost = float(cost)
        graph.setdefault(u, {})[v] = cost

    print("\nEnter heuristic values for each node:")
    for node in nodes:
        h = float(input(f"Heuristic for {node}: "))
        heuristic[node] = h

    start = input("\nEnter start node: ")
    goal = input("Enter goal node: ")

    return graph, start, goal, heuristic


graph, start, goal, heuristic = get_input()
path, cost = a_star(graph, start, goal, heuristic)

print("\nPath found:", path)
print(" Total cost:", cost)
