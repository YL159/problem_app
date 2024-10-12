'''
Leetcode 1760. Minimum Limit of Balls in a Bag
A list of bags containing different # of balls, and given a max operation #. An operation can split a bag into 2 bags of >= 1 balls.
Find the min of max balls of all bags.

Each operation increase 1 more bag. For a certain max limit n, each bag can be divided into bags of <= n balls.
The increase of bags for each bag is (ceil(balls / n) - 1)
Binary search for this optimum n so that the extra bags is closest under max operations.

Similar to 1011. Capacity To Ship Packages Within D Days
Binary search & check for opt solution, instead of exhaust the partitioning.
'''
from typing import List
import bisect, math

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        nums.sort()
        l, r = 1, nums[-1]
        # distance between extra bags and max allowable extra bags, i.e. max op
        dist = nums[-1]
        # the record mid that achieve current distance
        record = nums[-1]
        # if l == r, also check this mid (l or r)
        while l <= r:
            mid = (l+r)//2
            # binary search for the position in sorted bag list where bag balls > mid
            i = bisect.bisect(nums, mid)
            extra = sum([math.ceil(x/mid)-1 for x in nums[i:]])
            diff = maxOperations - extra
            if diff < 0:
                l = mid + 1
            else:
                if diff <= dist:
                    dist = diff
                    record = mid
                r = mid - 1
        return record