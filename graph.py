import heapq


graph = {
    'S': {'A': 2, 'B': 1},
    'A': {'S': 2, 'C': 3},
    'B': {'S': 1, 'C': 1, 'D': 5},
    'C': {'A': 3, 'B': 1, 'E': 4},
    'D': {'B': 5, 'E': 2},
    'E': {'A': 4, 'D': 2},
}

def main(graph, start, end):
    queue = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = set()
    paths = {node: [] for node in graph}
    paths[start] = [start]
    while queue:
        curr_dist, curr_node = heapq.heappop(queue)
        if curr_node in visited:
            continue
        visited.add(curr_node)
        if curr_node == end:
            return distances[end], paths[end]
        for neighbor, weight in graph[curr_node].items():
            distance = curr_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
                paths[neighbor] = paths[curr_node] + [neighbor]

    return float('inf'), []

start_node = 'S'
end_node = 'E'
print(main(graph, start_node, end_node))


