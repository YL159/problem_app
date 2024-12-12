'''
Leetcode 3152. Special Array II
Given an array of ints, a subarray is special if:
	every neighboring pair of # have different parities
For each query in given query list, find if query subarr is special or not.

Consider a neighboring pair have the same parity
it would be the 2nd's 'fault' NOT to have different parity!
	[2,3,4,6,8,9,10]
	t,t,t,f,f,t,t
t for correct, f for fault.
Each number only react to its left neighbor, thus the iterative structure maintained.
The 0-indexed number is always correct!

In order for each query to be fast, we want to make (prefix[end] - prefix[start]) style processing
==> we can use prefix array to store count of abnormalities in nums[0, i]

    [2,3,4,6,8,9,10]
     t,t,t,f,f,t,t
pref:0,0,0,1,2,2,2

If within a query range, abnormality didn't change, it means the subarray in between is special.
Time O(n+q), space O(n)
'''
from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        # make a pref of count of abnormality
        # left padding 0 for idx -1 ref only
        pref = [0]
        prev = (nums[0]-1) % 2
        for n in nums:
            pref.append(pref[-1] + (n % 2 == prev))
            prev = n % 2
        res = []
        # if a, b abnormality count the same => special between [a, b], parity maintained
        for a, b in queries:
            res.append(pref[b+1] - pref[a+1] == 0)
        return res
