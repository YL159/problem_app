'''
Leetcode 15. 3Sum
Find unique triplets that sums to 0 in a given nums array.

Method 1, record 2-sum results and match with each nums[i]
Time O(n^2), but need O(n^2) space dict

Method 2, sort and use inner 2-pointer sum. #167
Early exit if there is no hope finding any match for nums[i]
Should NOT remove duplicates
The same time O(n^2) but smaller space O(1)
'''
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue
            # if nums[i] and neighbor 2 nums sums > 0, don't need to check greater nums[i]
            if sum(nums[i:i+3]) > 0:
                break
            # similarly, if nums[i] + nums[-2:] < 0, continue with larger nums[i]
            if i <= len(nums)-3 and nums[i] + sum(nums[-2:]) < 0:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                if nums[l] + nums[r] > -nums[i]:
                    r -= 1
                elif nums[l] + nums[r] < -nums[i]:
                    l += 1
                else:
                    if not res or res[-1][1:] != [nums[l], nums[r]]:
                        res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
        return res