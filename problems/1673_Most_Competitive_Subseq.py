'''
Leetcode 1673. Find the Most Competitive Subsequence
Given num array, find subseq of length k that is most competitive
Competitive: similar to lexicographically smallest, but string[i] comparison -> num[i] comparison

method 1
res[0]: find smallest within nums[:len(nums)-k+1], 
res[1]: find smallest within nums[idx(res[0])+1:len(nums)-k+2]
time O(kn)

method 2
Inherit the idea that res[j] can only come from nums[j:len(nums)-k+j]
Use monotonic increasing stack, but pop only untill the idx that cur nums[i] can take over
[3,5,2,1,6], k=3, res=[2,1,6].
 0,1,2,3,4
res[0] digit can only come from at least nums[:-2]
res[1] can only come from at least nums[:-1]
when stack=[2(2)], new item is 3(1), we can't pop 2 cus idx=3 reaches nums[:-1] range
it can replace at most till stack[1], not replacing stack[0] even nums[3] (1) < nums[stack[-1]] (2)
'''
from typing import List

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
		# 'lexico'graphically smallest subseq
        stack = []
        for i, n in enumerate(nums):
            if stack:
                # current n can only show up in stack later than idx=allow
                allow = k - min((len(nums)-i), k)
                while len(stack) > allow and n < nums[stack[-1]]:
                    stack.pop()
            if len(stack) < k:
                stack.append(i)
        return [nums[i] for i in stack]