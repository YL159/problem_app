'''
Leetcode 611. Valid Triangle Number
Given a list of non-negative ints, find # of triplets as side lengths that form a valid triangle.


Basic idea is to fix 2 sides, and find all 3rd side.

Brutal force traversing the array takes O(n^3) time.
Because for 3rd side the int is completely random and thus unpredictable.

Since fixing 2 side takes at least O(n^2) time, we can sort the array at O(nlogn) cost
and use it's increasing property when locating 3rd sides.

Method 1, sort and find 3rd side without going back
Outer 2 loops for fixing 2 sides, and the 3rd side starts from rightneighbor of each 2nd side
	=> 3rd side index k never decrease, because 1st and 2nd sides are always increasing.
    => It stops at the length that can't make triangle with fixed 2 sides, or the end of array
    => 2nd and 3rd side together traverse the nums[i+1:] part twice
    => j-loop and k-loop together costs O(n) time

Method 2, sort and fix 3rd side, make 1st and 2nd side meet in the middle
On the other hand, fix 3rd side from largest to smallest
Then find each matching 1st side and 2nd side, while 1st <= 2nd
	=> number in between are possible 2nd sides that can also match with such 1st side
1st and 2nd side traversal together also costs O(n) time

Time O(n^2), Space O(1)
'''

from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        # method 1
        nums.sort()
        n = len(nums)
        k = 0
        res = 0
        for i in range(n-2):
            if nums[i] == 0:
                continue
            k = i+2
            # j loop and k loop together takes O(n) time
            for j in range(i+1, n-1):
                two = nums[i] + nums[j]
                while k < n and two > nums[k]:
                    k += 1
                res += k - j - 1
        return res
