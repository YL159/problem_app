'''
Leetcode 33. Search in Rotated Sorted Array
A sorted array was rotated at some pivot. Find the idx of target in this array, or -1 if not exist.
Algorithm run in O(logn) time

Method 1, binary search for the pivot point in the array, and bisect on target range
Find the real start of the original sorted array.
Goal is to include the pivot inside each bisect choice:
	if mid < right => [mid, right] is sorted, thus pivot in left => right = mid
		(not mid-1 because mid is possibly the start, we don't want to miss it)
	else mid >= right => mid >= left, because left > right always => pivot in right => left = mid+1
Then we bisect on left and right subarr, report findings.
Time O(log(n)), Space O(1)

Method 2, binary search while considering nums[l], nums[mid], nums[r] relationship
    if nums[l] < nums[mid], nums[l, mid] is sorted, and if target is within range, search inside
        if target is outside, exclude this sorted range by lifting l to mid+1
    else, nums[l] >= nums[mid], mid must be in right half, thus nums[mid] < nums[r] is true
        nums[mid, r] is sorted, search inside
        if target not in side, exclude this sorted range by reduce r to mid-1
Thus to keep target always in [l, r] range.
Time O(log(n)), Space O(1)
'''
from typing import List
import bisect

class Solution:
    # method 1, find pivot point and partial bisect
    def search(self, nums: List[int], target: int) -> int:
        # find start of ascending order
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l+r)//2
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                # nums[mid] <= nums[r] now mid is possible start, include it
                r = mid
        # now l is the start of ascending
        if target > nums[-1]:
            left = bisect.bisect_left(nums, target, 0, l)
            return left if left <= l and nums[left] == target else -1
        right = bisect.bisect_left(nums, target, l, len(nums))
        return right if right < len(nums) and nums[right] == target else -1


    # method 2, direct binary search
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            # [l, mid] is sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        return -1