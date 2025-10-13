'''
Leetcode 3186. Maximum Total Damage With Spell Casting
Given an array of int spell powers/damange, find the max total damage casting some spells:
	Each spell can be casted only once
	Once a spell power of x is casted, spell power of [x-2, x-1, x+1, x+2] can't be casted

Observation: all spells of the same power x can be casted right away, for max total damage
Decision of casting a spell possibly affects previous and later choices of spells
	=> thinking of take/not take DP solution for each unique spell power
But DP requires no after effect of each choice
	=> sort the unique spell powers so that
    	[x+1, x+2] after effect is mirrored as [x'-2, x'-1] previous effect for a later x'
    => DP state transition form is maintained

Time O(nlogn), Space O(n)
'''

from typing import List

import collections

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        ps = collections.Counter(power)
        ks = sorted(ps.keys())
        dp = [0] * len(ks)
        for i in range(len(ks)):
            # take current spell, 3 cases
            take = ks[i] * ps[ks[i]]
            if i >= 1 and ks[i-1] < ks[i] - 2:
                take += dp[i-1]
            elif i >= 2 and ks[i-2] < ks[i] - 2:
                take += dp[i-2]
            elif i >= 3: # prev 3rd spell must be < cur - 2
                take += dp[i-3]
            # not take current spell, dp[i-1]
            dp[i] = max(dp[i-1], take)
        return dp[-1]
