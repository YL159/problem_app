'''
Leetcode 1937. Maximum Number of Points with Cost
Given a matrix of ints, take a # from each row, add to final points
But between neighboring rows, remove abs(column index distance) from points
Find max final points

Method 1, DP on each row cell's best choice, from the above row
For each row, save max possible points if choosing each cell
based on last row's best results
Time O(mn^2), TLE

Method 2, DP on each row cell's best choice, preprocess above row
Similar idea from method 1, but optimize finding best result for each cell
Consider prev_row[0, col], at col + 1, all # will -1
    => prev_row[0, col] max point will STILL be max point of prev_row[0, col], just -1
    => just compare it with the newly added prev_row[col + 1]
    => result will become new best result of prev_row[0, col + 1]
    => left best = max(best[0, col] - 1, prev_row[0, col + 1])
Thus best[0, col] is updated using O(1) time instead of O(n)

Right side best[col, end] is similar, but preprocess each cell from right to left

Time O(mn), Space O(n)
'''

from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        
        cur, nex = points[0], []
        for i in range(1, m):
            right = [0] * (n+1)
            # preprocess prev row right portions' best result for each column
            for j in range(n-1, -1, -1):
                right[j] = max(cur[j], right[j+1] - 1)
            # same idea for left portions' best result on the run
            lbest = 0
            for j in range(n):
                lbest = max(cur[j], lbest - 1)
                nex.append(points[i][j] + max(lbest, right[j]))
            cur, nex = nex, []

        return max(cur)
