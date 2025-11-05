'''
Leetcode 1027. Longest Arithmetic Subsequence
Given a list of ints, len >= 2
Find the longest subseq that is an arithmetic sequence.

Method 1, incremental, group difference and update each tail's length
For each new int, it may produce some new difference d with previous ints
	=> that d may be the d of answer subseq
	=> O(n^2) time to collect d from all pair of ints
Now we may group these d by dictionary, {2: {tail1: len1, tail2: len2}, -1: {tail3: len3, tail4: len4}...}
For each new int, upon each d with prev unique int, update the recorded length with this new tail.
Time O(n^2), Space O(n^2), good for small n, int range won't affect performance

Method 2, iterate each possible difference and collection local max length
Since the int range of nums is limited, the arithmetic difference must be within [-D, D], D = max(nums) - min(nums)
	=> for each pair of d and -d, check max length of some subseq with this d
Then get the global max length subseq
Time O(Dn), Space O(n), good for small D and large n
'''

import collections

from typing import List

class Solution:
    # method 1
    def longestArithSeqLength(self, nums: List[int]) -> int:
        diffs = collections.defaultdict(dict)
        # the algo is not idempotent, thus remove duplicated ints
        prev = {nums[0]}
        for i in range(1, len(nums)):
            for x in prev:
                # get the tails of difference group d
                book = diffs[nums[i] - x]
                # either nums[i] extends recorded tail x's length by 1
                # or inherit some longer length if it's already visited
                book[nums[i]] = max(book.get(nums[i], 0), book.get(x, 1) + 1)
            prev.add(nums[i])

        return max([max(book.values()) for book in diffs.values() if book])
