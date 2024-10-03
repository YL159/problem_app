'''
Leetcode 18. 4Sum
Find all 4x tuples in a number list that sums to target.

Build on 2sum. Determine position of (a, b), find (c, d) on rem = target - a - b
Allow each # in nums max 4 times. Sort small list of (c, d) for rem to bisect for valid (c, d)
'''
from typing import List
import collections, bisect

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Idea: loop on 2 sum
        if len(nums) < 4:
            return []
        count = collections.Counter(nums)
        nums = []
        # collect each # repeat only 4 times max
        for k in count:
            rep = min(4, count[k])
            nums.extend([k]*rep)
        
        # 2sum: sorted list of idx tuple (3, 4)
        book = {}
        res = set()
        for a in range(len(nums)-3):
            for b in range(a+1, len(nums)-2):
                rem = target - nums[a] - nums[b]

                if rem not in book:
                    book[rem] = []
                    record = collections.defaultdict(int)
                    # find ALL possible 2sum (c,d) for rem, c starts at a+1 not b+1
                    for c in range(a+1, len(nums)):
                        compli = rem - nums[c]
                        if compli in record:
                            book[rem].append((record[compli], c))
                        record[nums[c]] = c
                    book[rem].sort()
                
                start = bisect.bisect(book[rem], (b+1, 0))
                for c, d in book[rem][start:]:
                    # the tuple won't duplicate because in nums same # are together
                    res.add((nums[a], nums[b], nums[c], nums[d]))
        return res
    