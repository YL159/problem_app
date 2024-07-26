'''
Leetcode 1020. Number of Enclaves
In a matrix of 1/0, find the total of lands(1) completely surrounded by sea(0)

Use BFS on any land reaching the edge of matrix, and label them 0
Then sum the matrix to get the total of remaining lands.
'''
from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        candi = set()
        # get 4 edges of the matrix, no -index
        for j in range(n):
            candi.add((0, j))
            candi.add((m-1, j))
        for i in range(m):
            candi.add((i, 0))
            candi.add((i, n-1))
        # Iterative BFS
        while candi:
            nex = set()
            for i, j in candi:
                if grid[i][j] == 0:
                    continue
                grid[i][j] = 0
                # check 4 directional valid candidates for next iteration
                four = {(i-1, j), (i+1, j), (i, j-1), (i, j+1)}
                for x, y in four:
                    if 0 <= x < m and 0 <= y < n and grid[x][y]:
                        nex.add((x, y))
            candi = nex
        # get total lands by sum
        res = 0
        for row in grid:
            res += sum(row)
        return res