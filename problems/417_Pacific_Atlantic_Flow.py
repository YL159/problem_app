'''
Leetcode 417. Pacific Atlantic Water Flow
Given a matrix of heights >= 0, top-left connects pacific, lower-right connects atlantic
Return coordinates of the land that, after raining, water can flow to BOTH oceans.
Water flow to 4-directional platforms with h <= current.

Initialize a record matrix. Each cell records ability to flow to either ocean
	e.g. [1, 0] for [can flow to pacific, can't flow to atlantic]
DFS propagate flow ability from matrix edges. Use early exit to prevent inf loop.
'''
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        self.m, self.n = m, n
        self.heights = heights
        # a cell [1, 0] means flow to pacific but not atlantic.
        self.record = [[[0, 0] for _ in range(n)] for _ in range(m)]

        pacific = [(i, 0) for i in range(m)]
        for j in range(1, n):
            pacific.append((0, j))
        for i, j in pacific:
            self.propagate(i, j, 0)

        atlantic = [(i, n-1) for i in range(m)]
        for j in range(n-1):
            atlantic.append((m-1, j))
        for i, j in atlantic:
            self.propagate(i, j, 1)
        
        # count records of [1, 1]
        res = []
        for i in range(m):
            for j in range(n):
                if self.record[i][j][0] == self.record[i][j][1] == 1:
                    res.append([i, j])
        return res

    # DFS propagate current pos (0 for pacific, 1 for atlantic) to valid neighbors
    def propagate(self, i: int, j: int, pos: int) -> None:
        if self.record[i][j][pos] != 0:
            return
        self.record[i][j][pos] = 1
        candi = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        for x, y in candi:
            if x < 0 or x >= self.m or y < 0 or y >= self.n or self.heights[x][y] < self.heights[i][j]:
                continue
            self.propagate(x, y, pos)
        