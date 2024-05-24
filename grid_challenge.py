from typing import List


def gridChallenge(grid: List[str]):
    new_grid = [list(char) for char in grid]
    for i in range(len(new_grid)):
        new_grid[i].sort()
    for i in range(len(new_grid) - 1):
        for j in range(len(new_grid[i])):
            if new_grid[i][j] > new_grid[i + 1][j]:
                return "NO"
    return "YES"


print(gridChallenge(['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']))

# create NO case
print(gridChallenge(['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywua']))

# create NO case on column
print(gridChallenge(['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuz']))
