'''
Leetcode 377. Combination Sum IV
Find # of all permutation of # in nums that sums to target

Build a reference hashtable of {target: # of permutations} from small to big targets
Binary search for the subarray where each is no greater than current target
'''

from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        book = {0: 1}
        for n in range(target+1):
            index = self.bs(nums, n)
            if n not in book:
                book[n] = 0
            for x in nums[:index+1]:
                if n-x in book:
                    book[n] += book[n-x]
        return book[target]

    def bs(self, ns: List[int], t: int) -> int:
        # binary search for the position in ns where # <= t target
        l, r = 0, len(ns)-1
        m = (l+r)//2
        while l < r:
            if ns[m] > t:
                r = m-1
            elif ns[m] == t:
                l = m
                break
            else:
                l = m+1
            m = (l+r)//2
        return min(l, m)
