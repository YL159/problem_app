'''
Leetcode 1314. Matrix Block Sum

Use prefix sum matrix to reduce complexity from O(mnk^2) to O(mn)
Prefix sum of rows of matrix only reduce to O(mnk)
'''

from typing import List

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        pref = [[0]*m for _ in range(n)]
        # O(mn) calculate prefix sum matrix
        for i in range(n):
            for j in range(m):
                left = pref[i][j-1] if j > 0 else 0
                up = pref[i-1][j] if i > 0 else 0
                lu = pref[i-1][j-1] if i > 0 and j > 0 else 0
                pref[i][j] = left + up - lu + mat[i][j]
        # O(mn) get the result matrix
        res = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                down = min(i+k, n-1)
                right = min(j+k, m-1)
                left = pref[down][j-k-1] if j > k else 0
                up = pref[i-k-1][right] if i > k else 0
                lu = pref[i-k-1][j-k-1] if i > k and j > k else 0
                rd = pref[down][right]
                res[i][j] = rd - left - up + lu
        return res