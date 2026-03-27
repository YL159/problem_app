'''
Leetcode 59. Spiral Matrix II
Given an int n >= 1, as side length of a square matrix
Fill natural numbers [1, n^2] from left-top cell clock-wise

Observation:
if n = 2k, each circle takes 4(2k-1) numbers, k >= 0
if n = 2k+1, each circle takes 8k numbers, k > 0, k=0, c=1

Method 1, fill each circle (row and col in bulk) and control edges

Method 2, use directional vector and guard condition to intuitively fill
Hint from solution, directional vector can be generated as simple as:
    dx, dy = dy, -dx, representing 90 degree clock-wise rotational matrix
    [ 0, 1] [dx]   [ dy]
    [-1, 0] [dy] = [-dx]

Time O(n^2), Space O(1)
'''

from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # or repeat directional vector
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        res = [[0] * n for _ in range(n)]
        i, j, di = 0, -1, 0
        for num in range(n*n):
            # ii, jj are intended next coordinate
            ii = i + dx[di]
            jj = j + dy[di]
            # if next coordinate is illegal, turn direction
            if not (0 <= ii < n) or not (0 <= jj < n) or res[ii][jj] != 0:
                di = (di + 1) % 4
            # get the correct coordinate and set result
            i += dx[di]
            j += dy[di]
            res[i][j] = num + 1
        return res