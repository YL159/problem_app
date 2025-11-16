'''
Leetcode 2536. Increment Submatrices by One
A matrix of side length n is initially all 0.
For each query, stating left-top and bottom-right coordinates of a submat:
	increment all cells inside by 1
Return the final matrix

If we just process the queries as is, time complexity is O(q*n^2)

Method 1, line sweep on each row
Consider the queries gives increment of derivative of each row:
	=> collect those increments/decrements at proper positions
Then integrate each row by prefix sum.
Use padding to conform the loop content.
Time O(q*n + n^2)

Method 2, matrix sweep on each submatrix
Upgrade from line sweep to matrix sweep, speed up for query processing
Time O(q + n^2)
'''
from typing import List

class Solution:
    # method 1, update each row(line) sweep
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
    
    # method 2, faster query processing
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        # O(q) processing matrix sweep query
        res = [[0]*(n+1) for _ in range(n+1)]
        for r1, c1, r2, c2 in queries:
            res[r1][c1] += 1
            res[r1][c2+1] -= 1
            res[r2+1][c1] -= 1
            res[r2+1][c2+1] += 1
        # column prefix sum array before processing each row of result
        prev = [0] * (n+1)
        for row in range(n):
            prev[0] += res[row][0]
            res[row][0] = prev[0]
            # row update on the run, in 1 loop
            for col in range(1, n):
                tmp = res[row][col]
                res[row][col] += res[row][col-1] + prev[col]
                prev[col] += tmp
        
        res.pop()
        for row in res:
            row.pop()
        return res