'''
Leetcode 1014. Best Sightseeing Pair
Given an array of site arr of sightseeing values
pick 2 different idx sites that maximize (value[i] + value[j] - (j-i))

Method 1:
Rearrange the target criteria = (value[i] - (j-i)) + value[j]
Thus for each later idx j, find the max (value[i] - (j-i))
	=> it is distance downgraded prev value[i], and will downgrade by 1 when j increases
	=> each current j could be this "prev j"
	=> compare (value[i]-(j-i)) and (value[j]-(j-j)) = value[j]
Dynamically update optimum choice (value[i] - (j-i))

Method 2:
Rearrange the target criteria by idx: (value[i] + i) + (value[j] - j)
Thus for each site value, the choice criteria is (value[i] + i), maintain this historical max
And for each j, calculate its corresponding result.

2 different perspectives on criteria formula, similar process.

Time O(n), Space O(1)
'''
from typing import List

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # method 1, visited max will depreciate on the run
        # keep track of the max(visited) - current dist
        # the visited max value will degrade when moving forward.
        # Replace it if a fresh overall larger site is visited
        res, opt = values[0], values[0]
        for v in values[1:]:
            # visited best site's value will degrade as progressing
            opt -= 1
            # update global best pair score
            res = max(res, opt + v)
            # update the best site with current best site
            opt = max(opt, v)
        return res
        
    def maxScoreSightseeingPair(self, values: List[int]) -> int:

        # method 2, score = (v[i] + i) + (v[j] - j), separate i with j
        # thus for each current j, find the visited max (v[i]+i)
        # update the result and maintain the max
        opt = values[0]
        res = 0
        for j in range(1, len(values)):
            res = max(res, opt + values[j] - j)
            opt = max(opt, values[j] + j)
        return res