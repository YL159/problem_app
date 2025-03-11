'''
Leetcode 2536. Increment Submatrices by One
A matrix of side length n is initially all 0.
For each query, stating left-top and bottom-right coordinates of a submat:
	increment all cells inside by 1
Return the final matrix

If we just process the queries as is, time complexity is O(q*n^2)

Consider the queries gives increment of derivative of each row:
	=> collect those increments/decrements at proper positions
Then integrate each row by prefix sum.
Use padding to conform the loop content.
Thus the time complexity is O(q*n + n^2)
'''
from typing import List

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        # translate queries as incre/decre at boarders
        # right/bottom padding for edge consistence
        res = [[0]*(n+1) for _ in range(n+1)]
        for r1, c1, r2, c2 in queries:
            for row in range(r1, r2+1):
                res[row][c1] += 1
                res[row][c2+1] -= 1
        # integrate/prefix sum on each row
        for row in range(n):
            for col in range(1, n):
                res[row][col] += res[row][col-1]
        # drop padding row/col
        res.pop()
        for row in res:
            row.pop()
        return res