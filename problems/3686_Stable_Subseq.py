'''
Leetcode 3686. Number of Stable Subsequences
Given a list of ints, find # of subsequences where no 3 consecutive numbers having the same parity.

For subsequence problems, consider incremental method.

With each new int from the array:
	if odd:	1. as start of a new odd tail -> becomes 1-odd tail
				=> previous subseqs have nothing OR 1 tail evens OR 2 tail evens
			2. adds to previous subseqs with 1 odd tail -> becomes 2-odd tail
	if even, similar approach
Thus we should keep track of the # of subseqs of 1-odd tail, 2-odd tail, 1-even tail, 2-even tail
For each new item, update each count according to their previous counts.

Even though theoretically same time O(n) without mod during the process
repeatingly mod will help decrease giant int calculations.
Because in python, giant int operation may take O(log(int_value)) time instead of O(1)
even though the log base is huge.

Time O(n), Space O(1)
'''

from typing import List

class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        # space O(1) dp on subseq count of:
        # last odd 1, last odd 2, last even 1, last even 2
        mod = 10**9 + 7
        o1 = o2 = e1 = e2 = 0
        for n in nums:
            if n % 2:
                # new 2-odd increase by prev 1-odd
                o2 = (o2 + o1) % mod
                # new 1-odd increase by all even tails, and 1 for new subseq with only this int
                o1 = (o1 + e1 + e2 + 1) % mod
            else:
                e2 = (e2 + e1) % mod
                e1 = (e1 + o1 + o2 + 1) % mod
        return (o1+o2+e1+e2) % mod