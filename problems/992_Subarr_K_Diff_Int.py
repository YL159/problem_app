'''
Leetcode 992. Subarrays with K Different Integers
Given an array of ints, find # of all subarr that has k distinct ints.

Different from #1358 and #930, here asks exactly k distinct ints (#1358 has only 'abc' letters)
	and ints are different (#930 use pfs, 1s are addable)
If using #930 strategy, isolating each valid 'core' of k distinct ints takes O(n^2) instead of O(n)

Taking sliding window idea of #1358, easy to use O(n) time to find 'at least k distinct ints' subarr count
Thus # of subarr exactly k distinct = # of subarr at least k distinct - # of at least k+1 distinct
Making 2 pass of the nums. Also workable for #930
'''
from typing import List

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # easier to find # of substr has at least k diff ints
        # res = solution(k) - solution(k+1)
        def atLeastK(least: int) -> int:
            book = {}
            i, j = 0, 0
            res = 0
            # if j finishes, march on for potential i
            while len(book) == least or j < len(nums):
                if len(book) < least:
                    book[nums[j]] = book.get(nums[j], 0) + 1
                    j += 1
                else:
                    res += len(nums) - j + 1
                    book[nums[i]] -= 1
                    if book[nums[i]] == 0:
                        del book[nums[i]]
                    i += 1
            return res
        
        return atLeastK(k) - atLeastK(k+1)