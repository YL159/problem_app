'''
Leetcode 2289. Steps to Make Array Non-decreasing
Given an array of positive numbers, for each step:
	Simultaneously remove any nums[i] if nums[i-1] > nums[i]
Find after how many steps the array will be non-dcreasing (no more numbers to remove)

Consider [5,3,4,4,7,3,6,11,8,5,11] the result array will be:
		 [5,      7,    11,    11] and non-decreasing
	=> nums[j] right neighbors that smaller than nums[j] will be eventually removed
As hint suggests, we can find the removal step for each element, result is max(steps)
For nums[i]:
	smaller than nums[i-1] => removable at step 1
    same as nums[i-1] => +1 on nums[i-1] step
    larger than nums[i-1] => +1 on nums[i-1] step
    => nums[i] step is the max of its previous non-greater element's step + 1
	=> Thus use monotonic decreasing stack to save decided element's steps

Time O(n), Space O(n)
'''
from typing import List

class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        # find the round to delete each element.
        # those in final array is default 0
        rounds = [0] * len(nums)
        # monotonic decreasing stack.
		# stack[0] is definitely the element enters final array
        stack = []
        for i, n in enumerate(nums):
            max_round = 1
            # pop out all elements that <= n, thus n can inherit the largest step
            while stack and nums[stack[-1]] <= n:
                max_round = max(max_round, rounds[stack.pop()]+1)
            if not stack: # n can enter final array
                max_round = 0
            rounds[i] = max_round
            stack.append(i)
        
        return max(rounds)