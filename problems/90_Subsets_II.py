'''
Leetcode 90. Subsets II
Given a list of ints, may containing repeats
Find all distinct subsets of its elements

Observation:
e.g. [1,2,2], initially empty set []
1: add to existing subsets: [1]
1st 2: add to existing subsets: [1,2], [2], added 2 new subsets
2nd 2: add from ending with 2: [1,2,2], [2,2], still 2 more
    => added subsets are at result tail

Thus we can sort nums
When see a new int:
    safely add it to all existing subsets, as they are all new

When see a repeated int:
    add it only to those ends with this int (avoid repeating)
    and the count of added subset with repeated int is the same

Time O(2^n), Space O(2^n)
'''

from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = [[]]
        nums.sort()
        prev = nums[0]-1 # make sure the 1st number is "different" from previous
        last = 0 # count of subsets added from prev int
        for n in nums:
            # if current n is new int, safely add it to all existing subsets
            # count of addition is current len(res)
            if n != prev:
                last = len(res)
            # if n is repeated int, inherit the last count (tail of current result)

            # range len is evaluated once, len(res) changes won't affect loop condition
            for i in range(len(res)-last, len(res)):
                tmp = res[i].copy()
                tmp.append(n)
                res.append(tmp)
            prev = n
        return res