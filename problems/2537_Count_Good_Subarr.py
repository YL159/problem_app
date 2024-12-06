'''
Leetcode 2537. Count the Number of Good Subarrays
Given an int arr and int k >= 1, count # of good subarr
A good subarr contains >= k pairs of same numbers. [4,3,5,4,3] has 2 pairs

Method 1
First idea is we want to keep a prefix record of # of pairs for prefix [0, i] as pref[i],
then use 2 pointers to check if a subarr has >= k pairs.
But this requires another record of # of pairs broken for suffix [j, len(nums)] as suffix[j]
Combining above pref & suff arr, we can indeed find # of valid pairs in [j, i] range

Method 2
As hinted in leetcode, the above approach can be simplified as keeping a running count of #:
	Pairs will increase count[nums[r]] for current nums[r]
	Pairs will decrease count[nums[l]] for current nums[l]
Thus check pair ? k to add valid # of subarr to result.
'''
from typing import List
import collections

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        # method 2, running counting
        # 2 pointer find how many pairs between [l, r], count diff >= k
        if len(nums) < 2:
            return 0
        count = collections.defaultdict(int)
        pairs = 0
        res = 0
        pre = 0
        l, r = 0, 0
        while r < len(nums):
            pairs += count[nums[r]]
            count[nums[r]] += 1
            if pairs >= k:
                while pairs >= k:
                    count[nums[l]] -= 1
                    if count[nums[l]]:
                        # reverse pair count
                        pairs -= count[nums[l]]
                    l += 1
                # now excluding nums[l-1] makes pairs < k
                # count only 'fresh' starting ls
                res += (l-pre) * (len(nums)-r)
                pre = l
            r += 1
        return res
