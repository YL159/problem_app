'''
Leetcode 2779. Maximum Beauty of an Array After Applying Operation
For each # in the given array we can make at most 1 op. In 1 op:
	change the ith # to any number in [nums[i]-k, nums[i]+k]
Find the max length of a subseq of the same number, in result arr.

1st thought, the final 'same number' sequence is not necessarily from existing numbers:
	[7,7,7,5,5]; k=1, the choice of # for max len subseq is 6
Thus we want to see all the possibilities for each #, and see which gets the most 'vote'
=> Keep a vote dict for all possible choices for all #, count their votes.
=> The largest vote is the max len of target subseq
Time O(n*k), space O(n*k)

2nd method, as hint says, since subseq require no order of its original #,
we can sort the array in ascending order. Thus for each #:
	find max idx/number that can cope with starter # to form a 'same # seq'
	=> find max j that nums[j] - nums[i] <= 2*k
	=> record max j-i, till j = len(nums)
Time O(nlog(n)), space O(1) if using given nums and sort in-place

Favor 1st than 2nd when k < log(n), otherwise favor 2nd for better time complexity
'''
from typing import List
import bisect

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # # method 1: for each nums[i], give 1 vote to each # in range [nums[i]-k, nums[i]+k]
        # # find the most votes => max len of same # subseq. O(n*k)
        # votes = collections.defaultdict(int)
        # for n in nums:
        #     for x in range(n-k, n+k+1):
        #         votes[x] += 1
        # return max(votes.values())

		# method 2: sort the array, from smallest, find max j that nums[j] - nums[i] <= 2*k
        # O(nlog(n))
        nums.sort()
        res = 0
        i = 0
        j = bisect.bisect(nums, nums[i]+2*k) - 1
        res = j-i+1
        while j < len(nums):
            if nums[j] - nums[i] > 2*k:
                res = max(res, j-i)
                i += 1
            j += 1
        res = max(res, j-i)
        return res