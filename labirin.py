from collections import deque
import time


class Solution:
    def __init__(self, n, labirin):
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        self.visited = {(0, 0)}
        self.queue = deque([(0, 0)])
        self.n = n
        self.labirin = labirin

    def isSafe(self, x, y, ):
        return 0 <= x < self.n and 0 <= y < self.n and self.labirin[x][y] == 0

    def bfs(self):
        while self.queue:
            x, y = self.queue.popleft()
            if x == self.n - 1 and y == self.n - 1:
                return "aman"
            for dx, dy in self.directions:
                nx, ny = x + dx, y + dy
                if self.isSafe(nx, ny) and (nx, ny) not in self.visited:
                    self.visited.add((nx, ny))
                    self.queue.append((nx, ny))
        return "tidak aman"


# Timing the BFS function
start_time = time.time()
# craete not safe labirin
solution = Solution(3, [[0, 1, 0],
                        [1, 1, 0],
                        [1, 1, 0]])

result = solution.bfs()
elapsed_time = time.time() - start_time

print(result)  # Expected result: "aman" if the labyrinth is navigable
print(f"Execution time: {elapsed_time:.6f} seconds")
