'''
Leetcode 33. Search in Rotated Sorted Array
A sorted array was rotated at some pivot. Find the idx of target in this array, or -1 if not exist.
Algorithm run in O(logn) time

Binary search to find the pivot point in the array, the real start of the original sorted array.
Goal is to include the pivot inside each bisect choice:
	if mid < right => [mid, right] is sorted, thus pivot in left => right = mid
		(not mid-1 because mid is possibly the start, we don't want to miss it)
	else mid >= right => mid >= left, because left > right always => pivot in right => left = mid+1

Then we bisect on left and right subarr, report findings.
'''
from typing import List
import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find start of ascending order
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l+r)//2
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid
        # now l is the start of ascending
        left = self.check(nums, target, 0, l)
        right = self.check(nums, target, l, len(nums))
        return max(left, right)

    def check(self, ns: List[int], t: int, start: int, end: int) -> int:
        idx = bisect.bisect(ns, t, lo=start, hi=end)
        if idx == 0 or ns[idx-1] != t:
            return -1
        return idx - 1
