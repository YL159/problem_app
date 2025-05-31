'''
Leetcode 1269. Number of Ways to Stay in the Same Place After Some Steps
Given an array of fixed length arrLen, a pointer starting at index 0
For each step, the pointer can move to left 1 slot, stay or right 1 slot.
	pointer can't move out of the array at any time
Find the number of ways to stay at index 0 after exactly k steps.

Reduce problem dimension by growing k from 0 to k steps.
At k+1 steps, slot i's new number of ways only come from k step's:
	i-1 slot ways, i slot ways, i+1 slot ways
	over boundary slots has default 0 ways
Thus build from 0 steps to target steps in DP.
Time O(steps*min(steps, arrLen)), Space O(min(steps, arrLen))
'''
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        # dp on final positions after each k steps, till n steps
        row, row1 = [1], []
        k = 0
        while k < steps:
            for i in range(min(len(row)+1, arrLen)):
        		# at k+1 step, result in arr[i] comes from k steps' arr[i-1], arr[i], arr[i+1]
                tmp = (row[i-1] if i > 0 else 0) + \
                        (row[i] if i < len(row) else 0) + \
                        (row[i+1] if i < len(row)-1 else 0)
                row1.append(tmp)
            row, row1 = row1, []
            k += 1
        return row[0] % (10**9+7)