def longest_path(graph: list) -> int:
    n = len(graph)
    topo_order = topological_sort(graph, n)
    return calculate_longest_path(graph, topo_order, n)

def topological_sort(graph, n):
    visited = [False] * n
    stack = []

    def dfs(v):
        visited[v] = True
        for neighbor, _ in graph[v]:
            if not visited[neighbor]:
                dfs(neighbor)
        stack.append(v)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
    
    return stack[::-1]

def calculate_longest_path(graph, topo_order, n):
    dist = [-float('inf')] * n
    dist[topo_order[0]] = 0  # Start from the first node in topological order
    
    for u in topo_order:
        if dist[u] != -float('inf'):
            for v, weight in graph[u]:
                if dist[u] + weight > dist[v]:
                    dist[v] = dist[u] + weight
    
    # The longest path would be the maximum value in dist array
    return max(dist)

# Example usage
graph = [
    [(1, 3), (2, 2)],
    [(3, 4)],
    [(3, 1)],
    []
]
print(longest_path(graph))
