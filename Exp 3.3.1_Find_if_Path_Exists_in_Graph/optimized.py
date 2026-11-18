
from collections import deque

def valid_path_optimized(n, edges, source, destination):
    # Build adjacency list
    adj = [[] for _ in range(n)]

    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    if source == destination:
        return True

    visited = [False] * n
    queue = deque([source])
    visited[source] = True

    while queue:
        node = queue.popleft()

        for neighbor in adj[node]:
            if neighbor == destination:
                return True

            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return False


# User input
n = int(input("Enter number of nodes: "))
e = int(input("Enter number of edges: "))

edges = []
for i in range(e):
    u, v = map(int, input(f"Enter edge {i + 1} (u v): ").split())
    edges.append([u, v])

source = int(input("Enter source node: "))
destination = int(input("Enter destination node: "))

print(valid_path_optimized(n, edges, source, destination))
