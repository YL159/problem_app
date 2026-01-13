'''
Leetcode 46. Permutations
Given a list of unique ints, get all permutations of them.

Method 1, incremental and insert
For each new #, it can insert into all positions of each previous permutations
    => creating new permutations
Time O(n!), sum(n*n!), Space O(n!)

Method 2, exchange and permute suffix
Inspired by discussion
We can fix the prefix and permute the suffix. Permuting a range means exchange all possible pairs.
Thus fix nums[0], permute the suffix, RETURN # to original position, and exchange nums[0] with nums[1]
    => untill nums[0] has exchanged with all other #
Permuting the suffix uses the same routine.
Time O(n!), Space O(n!)
'''

from typing import List

class Solution:

    # method 1, incremental and insert
    def permute(self, nums: List[int]) -> List[List[int]]:
        cur, nex = [[nums[0]]], []
        # add each new # to current permutations
        for i in range(1, len(nums)):
            length = len(cur)
            # to each permutation
            for p in range(length):
                # each permutation's all positions
                for pos in range(len(cur[p])+1):
                    x = cur[p][:]
                    x.insert(pos, nums[i])
                    nex.append(x)
            cur, nex = nex, []
        
        return cur


    # method 2, exchange and permute suffix
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        # permute the suffix of current nums[i:]
        def perm_suf(i: int) -> None:
            # no suffix to permute, copy to result
            if i == len(nums):
                res.append(nums[:])
            
            # exchange nums[i] with each # including self, and permute the suffix
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                perm_suf(i+1)
                nums[i], nums[j] = nums[j], nums[i]

        perm_suf(0)
        return res