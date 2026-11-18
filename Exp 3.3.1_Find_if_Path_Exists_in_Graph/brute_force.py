
def valid_path_brute(n, edges, source, destination):
    # Build adjacency list
    adj = [[] for _ in range(n)]

    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visited = set()

    def dfs(node):
        if node == destination:
            return True

        visited.add(node)

        for neighbor in adj[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True

        return False

    return dfs(source)


# User input
n = int(input("Enter number of nodes: "))
e = int(input("Enter number of edges: "))

edges = []
for i in range(e):
    u, v = map(int, input(f"Enter edge {i + 1} (u v): ").split())
    edges.append([u, v])

source = int(input("Enter source node: "))
destination = int(input("Enter destination node: "))

print(valid_path_brute(n, edges, source, destination))
