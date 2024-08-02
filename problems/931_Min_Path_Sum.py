'''
Leetcode 931. Minimum Falling Path Sum
Given a matrix of ints, from top row to bottom row, find the path that has min sum.

Refer to Seam Carving algorithm. The value of each cell is the 'Energy' of the pixel,
magnitude of change vectors in x-y directions

Make a DP matrix, each row contains min sum path of the matrix till this row.
And use this row to find min sums for next row

Additionally, to find the min sum path:
Trace from the min value of the last row, and upstream for its min parent (upper, upper left/right) each row.
Because the min of current row must come from the min value of its 3 parents, adding the same matrix cell value.

Using numpy or torch matrix manipulations, like matrix rolling, can avoid edge check.
'''
from typing import List 

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # Core of Seam Carving algorithm
        n = len(matrix)
        cal = [[0] * n for _ in range(n)]
        cal[0] = matrix[0].copy()
        for i in range(1, n):
            # collecting min path sums at row i, used for next row
            for j in range(n):
                left = cal[i-1][j-1] if j > 0 else float('inf')
                right = cal[i-1][j+1] if j < n-1 else float('inf')
                cal[i][j] = matrix[i][j] + min(left, right, cal[i-1][j])
        return min(cal[-1])