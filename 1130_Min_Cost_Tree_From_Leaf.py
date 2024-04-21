'''
1130. Minimum Cost Tree From Leaf Values
Given an in-order traversal list of leaf node values, for all the trees from it, get the min sum of non-leaf nodes

Here is a memo brutal solution of all possible trees.
Extracted max matrix out from the main dp loop to reduce main loop time complexity from O(n^4) to O(n^3)

A better O(n) solution is to greedily use min leaf first, and larger leaf near tree top to make non-leaf nodes as small as possible
'''

from typing import List

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        # 1. Greedy + monotonic stack can achieve O(n)
        # 2. Memo 'brutal' force here O(n^3)
        n = len(arr)
        # create max matrix of arr, O(n^2). Using max() will be O(n^3)
        # mx[i][j] is the max of arr[i:j+1], i <= j
        mx=[[0]*n for _ in range(n)]
        for i in range(n):
            # monotonic stack
            max_stack = []
            prev = arr[i]-1
            for j in range(i, n):
                if arr[j] > prev:
                    max_stack.append((j, arr[j]))
                    prev = arr[j]
            # accommodate stack indexing
            max_stack.append((n-1, max_stack[-1][1]))
            index = 1
            for j in range(i, n):
                if j >= max_stack[index][0]:
                    index += 1
                mx[i][j] = max_stack[index-1][1]

        # make a 2d matrix dp. dp[i][j] is the optimum of arr[i:j+1]
        # dp[i][j] is min of partition i~(i+1:j) ... (i:j-1)~j. i <= j
        dp=[[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = arr[i]
        for i in range(n-1):
            dp[i][i+1] = dp[i][i]*dp[i+1][i+1]
        for j in range(2, n):
            for i in range(n-j):
                cur_min = float('inf')
                for k in range(i, i+j):
                    left = 0 if k == i else dp[i][k]
                    right = 0 if k+1 == i+j else dp[k+1][i+j]
                    cur = left + right + mx[i][k] * mx[k+1][i+j]
                    cur_min = min(cur_min, cur)
                dp[i][i+j] = cur_min

        return dp[0][n-1]