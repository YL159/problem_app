'''
Leetcode 221. Maximal Square
In matrix of 0/1, find the largest square containing only 1. Return # of 1s inside.

1. matrix prefix rectangle sum and find squares, O(n^3)
For each [i,j], find if the sum of a square bottom-right at [i,j], is square of length.
sum(square len a) = pref[i][j] + pref[i-a][j-a] - pref[i-a][j] - pref[i][j-a]

2. DP matrix of m*n, DP[m][n] is the max side len of '1' square bottom-right at [m][n].
To derive DP[m+1][n+1] using prefsum of row and col. O(n^2):
a = DP[m][n]
If mat[i][j]==1 and row_pref[i][j]-row_pref[i][j-a] = a (got 1s to the left of [m+1][n+1])
and col_pref[j][i]-col_pref[j][i-a] = a (got 1s to the top of [m+1][n+1])
Then DP[m+1][n+1] = a+1, else min of prev length.

Below is 1 step further on the basis of 2

3. Same DP matrix, if mat[i][j]==1:
deriving DP[i][j] = min(DP[i-1][j-1], DP[i-1][j], DP[i][j-1]) + 1. O(n^2)
The smallest square from prev neighbors determines current square size.
'''
from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        res = 0
        # has to be from left to right, top to bottom
        for i in range(m):
            for j in range(n):
                up = dp[i-1][j] if i >= 1 else 0
                left = dp[i][j-1] if j >= 1 else 0
                leup = dp[i-1][j-1] if i >= 1 and j >= 1 else 0
                if matrix[i][j] == '1':
                    dp[i][j] = min(up, left, leup) + 1
                    res = max(res, dp[i][j])
        return res**2
