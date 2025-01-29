'''
Leetcode 2033. Minimum Operations to Make a Uni-Value Grid
Given a grid of numbers, each operation:
	+x or -x on one number in the grid
Find min # of op to make the grid values all equal (uni-value)

Observations:
1. All num % x should be the same, otherwise they will never be equal
2. The grid doesn't matter
3. There may be several possible final value that makes the same op, and one of them must be in current grid
	consider [2,2,6,6], x=1	final value can be 2,3,4,5,6, all of optimal op=8. 3,4,5 are fresh.
	reaching a new mid point require all smaller # uplift, larger # downgrade same x
    thus their end points, i.e. some grid # next to the fresh uni-value is also optimum

Thus we can sort the numbers from grid, count each number's quotient on x
	i.e. # of x inside each number, OR Distance to zero x on residual
	grid number sorted [1,3,3,7,9,13,13,15], x=2 -> [0,1,1,3,4,6,6,7]
Since final uni-value will be one of the grid number, we iterate on each quotient, check if possible
	e.g. set a distance 1, (target uni-value 3)
    [0,1,1,3,4,6,6,7] => [-,0,+,+,+,+,+,+]
	set a distance 3, (target uni-value 7)
    [0,1,1,3,4,6,6,7] => [-,-,-,0,+,+,+,+]
We don't care how many op needed, we care the position in distance arr that makes op min:
	i.e. when switching to the next target distance:
    	smaller dist each should increase m*x, adding m op (the difference between prev target distance to cur target distance)
        larger dist each can relieve m*x, reduce m op
    => 	favor larger distance if # of larger dist is dominant (> sum of 0 and negative distance)
		favor smaller distance if # of smaller dist is dominant (because now smaller dist relieve from increasing too much)
	Thus the counts of dist on both side of target dist matter

The above is indeed equivalent to median of the sorted number arr:
	1. Median's both sides have the same number count <=> neither is domonant
    2. For even length arr, choose either of the middle number as target is acceptable
'''
from typing import List
import collections

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # check each num distance to common remainder with step x
        # lift/push the dist arr so that abs sum is smallest
        # tipping point of positive dist count ~ negative dist count
        m, n = len(grid), len(grid[0])
        rem = grid[0][0] % x
        # count the distance frequency, keys are all non-negative from restriction
        dist = collections.defaultdict(int)
        for i in range(m):
            for j in range(n):
                if grid[i][j] % x != rem:
                    return -1
                dist[grid[i][j] // x] += 1

        darr = sorted(dist.items())
        negative, zero, positive = 0, 0, m*n
        # increasing the target dist, favor untill # of larger dist no longer dominant
        for d, count in darr:
            negative += zero
            zero = count
            positive -= count
            # negative/positive dist are both not dominant, thus sum(abs) can't be reduced
            if negative <= zero + positive and positive <= zero + negative:
                break
        
		# the op count is sum of the diff between target dist and each dist
        res = 0
        for k, count in darr:
            res += count * abs(k-d)
        return res

