from typing import List
'''
Leetcode 1493. Longest Subarray of 1's After Deleting One Element
Using discrete differentiation filter with 0 padding to find groups of 1s
Then record the max possible subarray length of candidate neighboring groups

Compared with sliding window counting for 0s in many solutions, this solution is O(n) space
and harder to extend for deleting multiple 0s
'''

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # get a list of tuples, (start, end) of 1s
        # tail padding to wrap last group of 1s
        nums.append(0)
        ones = []
        start = -1
        for i, n in enumerate(nums):
            if n == 0:
                if start >= 0:
                    ones.append((start, i-1))
                    start = -1
            elif start < 0:
                start = i
        
        # if only 1 group, check if any 0 to delete, otherwise have to delete 1
        if len(ones) == 1:
            a, b = ones[0]
            return ones[0][1] - ones[0][0] + (a != 0 or b != len(nums)-2)
        
        # record max length of each tuple or if neighbor tuples index diff is 2
        record = 0
        for j in range(len(ones)-1):
            start1, end1 = ones[j]
            start2, end2 = ones[j+1]
            record = max(record, end1-start1+1, end2-start2+1)
            if start2 - end1 == 2:
                record = max(record, end2-start1)
        return record