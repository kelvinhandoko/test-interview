# dijkstra algo's
# Time complexity: O(V^2) where V is the number of vertices
# Space complexity: O(V)

import heapq


def dijkstra(graph, source):
    # Create a priority queue
    priority_queue = []
    # Push the source node to the queue with distance 0
    heapq.heappush(priority_queue, (0, source))
    # Initialize distances with infinity
    distances = {node: float('infinity') for node in graph}
    # Distance to the source is 0
    distances[source] = 0

    while priority_queue:
        # Get the node with the smallest distance
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip processing if we found a better path already
        if current_distance > distances[current_node]:
            continue

        # Update the distance for each neighbor
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If a shorter path to the neighbor is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Example graph represented as an adjacency list
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Run Dijkstra's algorithm from source node 'A'
distances = dijkstra(graph, 'A')
print(distances)
