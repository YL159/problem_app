'''
Leetcode 2826. Sorting Three Groups
Given an int array of only 1,2,3s, remove min # of ints to make the array non-decreasing.

To make minimum removal <=> find max length of subseq that is non-decreasing
	=> #300 longest increasing subseq

The O(nlogn) solution of #300
Maintaining a sorted element list. For each array int, binary search for its insertion point:
	if largest, append to list => new length is reachable by some subseq ending with cur int
    else replace the list element => maintaining sorted property while keeping existing length

Here we only have 1,2,3 ints, thus binary search for new item's position in the sorted temp list can be simplified:
	remember 1,2,3 end positions instead of bisect, thus inner loop O(1) time find new item's supposed position
Since 3's end position indicates the length of the sorted list
	=> make the list "imaginary" by only maintaining those 3 end postions

Time O(N), Space O(1)
'''

from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
		# last index of 1, 2, 3 in the imaginary length recording array
        i, j, k = -1, -1, -1
        for n in nums:
            if n == 3:
                k += 1
            elif n == 2:
                j += 1
                if j > k:
                    k = j
            else:
                i += 1
                if i > j:
                    j = i
                if j > k:
                    k = j
        return len(nums) - k - 1

