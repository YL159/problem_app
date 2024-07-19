'''
Leetcode 1219. Path with Maximum Gold
Find the max gold of any non-0 path in a grid.

DFS back track on each non-0 cell. But some path may be traversed twice.
'''
from typing import List

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.m, self.n = len(grid), len(grid[0])
        # True is unvisited
        self.marker = [[True for i in range(self.n)] for j in range(self.m)]
        self.res = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 0:
                    self.marker[i][j] = False
                    continue
                self.dfs(i, j, 0)
        # print(self.res)
        return self.res
    
    # dfs backtrack on any non-0 cell for all paths.
    def dfs(self, i: int, j: int, res: int) -> None:
        new_res = res + self.grid[i][j]
        self.marker[i][j] = False
        neighbors = [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]
        filtered = []
        for x, y in neighbors:
            if 0 <= x < self.m and 0 <= y < self.n and self.marker[x][y] and self.grid[x][y] != 0:
                filtered.append((x,y))
        if not filtered:
            self.res = max(self.res, new_res)
        else:
            for x, y in filtered:
                self.dfs(x, y, new_res)
        self.marker[i][j] = True