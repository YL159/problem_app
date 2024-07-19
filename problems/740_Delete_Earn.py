'''
740. Delete and Earn
Repeatedly earn the number n you delete, but remove all n+1 and n-1. Solve for max earning.

Similar to house robber question. Incrementally maintaining 2 optimum choices:
taking or not taking current number, can be constructed by previous taking or not taking choices
'''

from typing import List
import collections
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        book = collections.Counter(nums)
        res = 0
        take, take_not = 0, 0
        for n in sorted(book.keys()):
            # lone numbers without +1 or -1 showing up can always be taken
            # if n-1 not in book and n+1 not in book:
            #     res += n * book[n]
            #     continue
            # update the optimum value of taking/not taking current number
            # also covers lone number cases
            take, take_not = take_not + n*book[n], max(take, take_not)
            # clean up when reaching the end of continuous numbers like 2,3,4
            if n+1 not in book:
                res += max(take, take_not)
                take, take_not = 0, 0
        return res