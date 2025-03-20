'''
Leetcode 995. Minimum Number of K Consecutive Bit Flips
Given a binary arr and int k>=1. 1 flip on arr is flipping consecutive k elements 1->0 and 0->1
Find min flips to make arr all 1

Super set of #3191. Minimum Operations to Make Binary Array Elements Equal to One I
where k=3. Easy O(nk) solution becomes O(n), acceptable.

Method 1. Sliding window flipping k elements when 1st is 0
Time O(kn) is O(n^2)

Method 2. Sliding window line sweep
Instead of updating each number in range k
record flip increment/decrement like line sweep, differential of flip range:
	record current prefix sum of flips, and mark window end flip-1
time O(n)

'''
from typing import List

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        change = [0] * (len(nums)+1) # right padding 1
        # curFlip is the prefix sum of flips considering change array
        # i.e. help to calculate flips of current nums[i]
        flips, curFlip = 0, 0
        for i in range(len(nums)-k+1):
            curFlip += change[i]
            if (curFlip + nums[i]) % 2 == 0:
                flips += 1
                curFlip += 1
                change[i+k] -= 1
        
        for j in range(len(nums)-k+1, len(nums)):
            curFlip += change[j]
            if (curFlip + nums[j]) % 2 == 0:
                return -1
        return flips