'''
Leetcode 827. Making A Large Island
Given a n*n grid of 0-1. 0 is water cell, and 1 is land cell.
Change at most one water into land, find the area of largest island there can be.

BFS on each island, assign labels to each island
for each water cell, find max connectable islands (max 4 different isles) total area
Time O(n^2)
'''
from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # cell visit state. -1: unvisited, other: island label
        visit = [[-1]*n for _ in range(n)]
        # islands' area list. idx is island label
        islands = []

        # BFS on an island cell, return island area
        def islandBFS(x: int, y: int) -> int:
            # early exit on calculated results
            if not grid[x][y]:
                return 0
            stat = visit[x][y]
            if stat >= 0:
                return islands[stat]
            # BFS on a new island cell
            label = len(islands)
            isle = set()
            cur, nex = {(x, y)}, set()
            area = 0
            while cur:
                area += len(cur)
                isle |= cur
                for a, b in cur:
                    visit[a][b] = label
                    for j, k in [(a+1, b), (a-1, b), (a, b+1), (a, b-1)]:
                        if 0 <= j < n and 0 <= k < n and grid[j][k] and (j, k) not in isle:
                            nex.add((j, k))
                cur, nex = nex, set()
            islands.append(area)
            return area
        
        res = 0
        for i in range(n):
            for j in range(n):
                # BFS on a land cell
                if grid[i][j]:
                    res = max(res, islandBFS(i, j))
                    continue
                isle_label = set()
                tmp = 1
                # collect water cell's 4 neighbor's land labels, add their areas
                for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if 0 <= x < n and 0 <= y < n:
                        if grid[x][y]:
                            islandBFS(x, y)
                        if visit[x][y] >= 0:
                            isle_label.add(visit[x][y])
                if isle_label:
                    tmp += sum(islands[t] for t in isle_label)
                res = max(res, tmp)
        return res