'''
Leetcode 2965. Find Missing and Repeated Values
Given a square matrix of side length n, filled with 1...n^2
But one # is missing and another is repeated
Find the missing and repeated #

This is easy if using set/arr to remember all numbers.
Space O(1) is possible by using math:
repeat - missing = sum(grid) - sum(1...n^2)
repeat^2 - missing^2 = sum(grid[i][j]^2) - sum(1^2, 2^2...n^2^2)
then find repeat and missing respectively.

Here is my space O(1) solution using swap.
Each # should stay in its supposed cell.
	=> For each cell, swap content to content's supposed cell's content, till match
Some # supposed cell has the same #, this # must be repeat
	=> current cell idx is potentially missing
Later any cell's # is the same as repeat, this cell idx is potentially missing
	i.e. this cell idx has supposed # not visited yet, and will be swapped later
    or this cell idx itself is the missing #
'''
from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # for each cell, iteratively swap it with corresponding cell
        # if a #'s corresponding cell has the same #, it is repeating
        # and current cell idx is missing. time O(n^2) space O(1)
        n = len(grid)
        repeat = -1
        missing = -1
        for i in range(n):
            for j in range(n):
                idx = i*n+j+1
                while idx != grid[i][j]:
                    ti = (grid[i][j]-1) // n
                    tj = (grid[i][j]-1) % n
                    # if cur num supposed box has same as cur, must be repeat
                    # and cur box idx is potentially missing
                    if grid[ti][tj] == grid[i][j]:
                        repeat = grid[i][j]
                        missing = idx
                        break
                    # cur supposed box contain the repeated num, idx is potentially missing
                    if grid[ti][tj] == repeat:
                        missing = idx
                    grid[ti][tj], grid[i][j] = grid[i][j], grid[ti][tj]
        return [repeat, missing]