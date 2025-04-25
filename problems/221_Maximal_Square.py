'''
Leetcode 221. Maximal Square
In matrix of 0/1, find the largest square containing only 1. Return # of 1s inside.

1. matrix prefix rectangle sum and find squares, O(n^3)
For each [i,j], find if the sum of a square bottom-right at [i,j], is square of length.
sum(square len a) = pref[i][j] + pref[i-a][j-a] - pref[i-a][j] - pref[i][j-a]

2. DP matrix of m*n, DP[m][n] is the max side len of '1' square bottom-right at [m][n].
To derive DP[m+1][n+1] using prefsum of row and col:
a = DP[m][n]
If mat[i][j]==1 and row_pref[i][j]-row_pref[i][j-a] = a (got 1s to the left of [m+1][n+1])
and col_pref[j][i]-col_pref[j][i-a] = a (got 1s to the top of [m+1][n+1])
Then DP[m+1][n+1] = a+1, else min of prev length.
Time Space O(mn)


3. one step further on the basis of 2
DP[i][j] has one-square of len a, and DP[i+1][j+1] col and row has consecutive 1 more than a
    => DP[i+1][j] and DP[i][j+1] must be >= a
Thus if mat[i+1][j+1] == 1: DP[i+1][j+1] = min(DP[i][j], DP[i][j+1], DP[i+1][j]) + 1.
The smallest square from prev neighbors determines current square size.
Time Space O(mn)
'''
from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        # left-top padding with 0
        dp = [[0]*(n+1) for _ in range(m+1)]
        res = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    res = max(res, dp[i][j])
        return res**2
