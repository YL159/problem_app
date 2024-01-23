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
        # list with all 1s, delete 1 not 0
        if len(set(nums)) == 1 and nums[0]:
            return len(nums)-1
        # else, deleting 0 is optimum
        # get a list of tuples, (start, end) of 1s in nums
        # padding before applying discrete differentiation filter
        mynums = [0]
        mynums.extend(nums)
        mynums.append(0)
        ones = []
        i = 1
        while i < len(mynums):
            diff = mynums[i] - mynums[i-1]
            if diff > 0:	# positive impulse
                start = i-1
            elif diff < 0:	# negative impulse
                ones.append((start, i-2))
            i += 1
        # record max length of each tuple or if neighbor tuples index diff is 2
        record = 0
        for start, end in ones:
            record = max(record, end-start+1)
        for j in range(len(ones)-1):
            start1, end1 = ones[j]
            start2, end2 = ones[j+1]
            if start2 - end1 == 2:
                record = max(record, end2-start1)
        return record