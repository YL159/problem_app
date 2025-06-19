'''
Leetcode 2616. Minimize the Maximum Difference of Pairs
From given nums array, choose p pairs of non-overlapping indices to make # pair.
Of all possible choices of p pair numbers, find min(max(abs(pair difference)))

Observation & deduction:
1. The goal is to pair numbers with overall min max_difference
	=> idealy pairing nums[i] with numerically nearest nums[j]
    => sort the array, the closest numbers are also neighbors
    
2. Since nums is sorted, result pair may come from any neighboring pairs
Greedily choosing smallest difference pairs may have overlapping number choices
	=> avoid taking neighboring valid differences, because they share the middle number
    => method 1: use take/not_take dp approach
    OR
    method 2: picking every other valid differences within a valid scope

Since the result space (min max_diff ranging [0, max(diff)]) can be bi-paritioned by the min(max(diff))
We can translate the problem from:
	Selecting p pairs of numbers and record min max_diff, outerloop time O(comb(p, n))
to:
	Fix a max_diff and check if possible to choose >= p pairs from diff, outerloop time O(log(n))
And binary search for this min(max(diff))
Inner loop uses observation 2's deduction, which takes O(n) time

Time O(nlogn), Space O(n)
'''
from typing import List

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0 or len(nums) <= 1:
            return 0
        nums.sort()
        diff = [abs(nums[i+1]-nums[i]) for i in range(len(nums)-1)]

        # check max # of diff to take from diff array if diff <= x
        # method 1, dp on take/not take each valid diff
        def check(x: int) -> int:
            take, take_not = 0, 0
            for d in diff:
                if d > x:
                    take, take_not = 0, max(take, take_not)
                else:
                    take, take_not = take_not + 1, max(take, take_not)
            return max(take, take_not)

        # method 2, [low, high] binary array take every other of consecutive low diff
        def check(x: int) -> int:
            consec, res = 0, 0
            for d in diff:
                if d > x:
                    res += (consec+1) // 2
                    consec = 0
                else:
                    consec += 1
            return res + (consec+1) // 2

		# binary search for the min max_diff_of_p_pairs
        l, r = -1, max(diff)
        while l < r-1:
            mid = (l+r)//2
            if check(mid) >= p:
                r = mid
            else:
                l = mid
        return r
