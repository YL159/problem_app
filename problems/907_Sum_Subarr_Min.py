'''
Leetcode 907. Sum of Subarray Minimums
Get the sum of every min(subarr) of given arr

# method 1
similar to 84. Largest Rectangle in Histogram
ask how far to left/right can a number be min of the range
	=> maintain increasing mon stack for idx range [0, i]
	=> decreasing mon stack(que) for [i, len(arr)) => reverse increasing mon stack from -1
idx i is at 'top' of both stack, easy find left/right dominant range.
But if multiple same min in stack, assign them (subarr that cover all of them) to either left or right
to avoid duplicated addition of them.
Time O(n), space O(n)

# method 2 by solutions section
DP on sum(min) of all subarr ending at idx i: DP[i] = result of arr[0, i]
Also keeps increasing mon stack from left.
At each i, new subarr can start from:
	on/before stack[-1] position, which in total has sum(min) of DP[j]
    after stack[-1] position, which has min of idx i
Time O(n) but 1 pass, space O(n)
'''
from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # check each # and maintain increasing mon stack from left
        left = self.increMonStack(arr, True)
        # reverse check each # for right decr mon stack
        right = self.increMonStack(arr[::-1], False)[::-1]
        # combine left & right for result
        res = 0
        mod = 10**9 + 7
        for i in range(len(left)):
            res += left[i] * right[i] * arr[i] % mod
            res %= mod
        return res
        
    def increMonStack(self, ar: List[int], assign: bool) -> List[int]:
        # -1 position holder to avoid if/else in for loop
        res, stack = [], [-1]
        for i, n in enumerate(ar):
            # if multiple same ar number, assign subarr containing all of them to only 1 side
            # to avoid dup count
            if assign:
                while stack[-1] >= 0 and ar[stack[-1]] >= n:
                    stack.pop()
            else:
                while stack[-1] >= 0 and ar[stack[-1]] > n:
                    stack.pop()
            l = i - stack[-1]
            stack.append(i)
            res.append(l)
        return res

# # method 2 from solutions
# class Solution:
#     def sumSubarrayMins(self, arr: List[int]) -> int:
#         stack = []
#         dp = [0]*(len(arr)) #dp[i] is the sum of all subarray that ending with i-th element

#         for i in range(len(arr)):
#             while stack and arr[stack[-1]] > arr[i]:
#                 stack.pop()
#             j = stack[-1] if stack else -1
#             # subarr starting left of j has sum(min) of dp[j]
#             dp[i] = dp[j]+(i-j)*arr[i]

#             stack.append(i)
        
#         return sum(dp) % (10**9+7)