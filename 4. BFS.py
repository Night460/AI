graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['D', 'E'],
    'C': [],
    'D': ['G', 'H'],
    'E': [],
    'G': [],
    'H': []
}

visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        current_node = queue.pop(0)
        print(current_node, end=" ")

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

print("Breadth First Search:")
bfs(visited, graph, 'S')