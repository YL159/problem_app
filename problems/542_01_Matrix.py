'''
Leetcode 542. 01 Matrix
Given a matrix of 0/1, find each cell's min distance to some 0

1. Recursive DFS is not working. Each 1 cell derives from 4 neighboring 1 cells' results.
But the matrix is a graph full of cycles, creating dead lock issue (or infinite recursion)

1.1 To avoid cycles, update the matrix in 1 direction, and update again in reversed direction.
e.g. From top-left to bottom-right, and again from bottom-right to top-left
Thus the matrix traversal becomes a tree or DAG, and every neighbor of a cell is considered.

2. DFS propagation is working but (mn)^2 time complexity.
If a cell receives smaller distance, it will propagate new dist to neighboring cells.
Thus each 0 cell will in worst case propagate almost all other 1 cells.

3. Use BFS from 0 cells. Collect updated new cells and work into centers of 1s. Time mn.
'''
from typing import List

# 3. Use BFS and work to the center of 1s
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # BFS from 0s.
        m, n = len(mat), len(mat[0])
        res = [[float('inf')] * n for _ in range(m)]
        level, nex = set(), set()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    res[i][j] = 0
                    level.add((i, j))
        while level:
            for r, c in level:
                for row, col in [(r-1, c), (r, c+1), (r+1, c), (r, c-1)]:
                    if 0 <= row < m and 0 <= col < n and res[row][col] > res[r][c]:
                        nex.add((row, col))
                        res[row][col] = res[r][c] + 1
            level, nex = nex, set()
        return res


# 1. DFS infinite recursion
# class Solution:
#     def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
#         self.m, self.n = len(mat), len(mat[0])
#         self.mat = mat
#         self.res = [[float('inf')] * self.n for _ in range(self.m)]
#         for i in range(self.m):
#             for j in range(self.n):
#                 if self.mat[i][j] == 0:
#                     self.propagate((i, j), 0)
#         return self.res

#     # recursively propagate current cell's new smaller value to neighbors
#     # each cell with 1 will be propagated maximum 4 times
#     def propagate(self, pos: tuple, d: int) -> None:
#         r, c = pos
#         # received distance >= cell record, stop propagate this distance
#         if self.res[r][c] <= d:
#             return
#         # otherwise record this distance, and propagate to neighbors with d+1
#         self.res[r][c] = d
#         neighbors = [(r-1, c), (r, c+1), (r+1, c), (r, c-1)]
#         for p in neighbors:
#             if 0 <= p[0] < self.m and 0 <= p[1] < self.n:
#                 self.propagate(p, d+1)
#         return


# 2. DFS propagate
# class Solution:
#     def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
#         self.m, self.n = len(mat), len(mat[0])
#         self.mat = mat
#         self.res = [[float('inf')] * self.n for _ in range(self.m)]
#         for i in range(self.m):
#             for j in range(self.n):
#                 if self.mat[i][j] == 0:
#                     self.propagate((i, j), 0)
#         return self.res

#     # recursively propagate current cell's new smaller value to neighbors
#     # each cell with 1 will be propagated maximum 4 times
#     def propagate(self, pos: tuple, d: int) -> None:
#         r, c = pos
#         # received distance >= cell record, stop propagate this distance
#         if self.res[r][c] <= d:
#             return
#         dis = d if self.mat[r][c] == 1 else 0
#         # otherwise record this distance, and propagate to neighbors with d+1
#         self.res[r][c] = dis
#         neighbors = [(r-1, c), (r, c+1), (r+1, c), (r, c-1)]
#         for p in neighbors:
#             if 0 <= p[0] < self.m and 0 <= p[1] < self.n and self.mat[p[0]][p[1]] == 1:
#                 self.propagate(p, dis+1)
#         return
