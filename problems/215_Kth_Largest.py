'''
Leetcode 215. Kth Largest Element in an Array
Find kth largest.

Method 1. sort & access kth, O(nlogn)

Method 2. maintain k-length list storing largest, O(kn)

Method 3. import heapq, heapq.nlargest(k, list), O(nlogk)

Method 4. k selection sort, expected O(n)
here is in-place k selection sort method
using nums[-1] as pivot, assuming nums are randomly distributed
'''
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = nums[-1]
        # smaller, equal, larger portion idx, 1 ahead of them
        i, e, j = 0, len(nums)-2, len(nums)-1
        while i <= e:
            if nums[i] < pivot:
                i += 1
                continue
            if nums[i] > pivot:
                nums[j], nums[i] = nums[i], nums[j]
                j -= 1
            nums[i], nums[e] = nums[e], nums[i]
            e -= 1
        # larger portion contains >= k elements, search inside
        if len(nums) - j - 1 >= k:
            return self.findKthLargest(nums[j+1:], k)
        # larger < k but larger + equal >= k, kth must be in equal portion
        if len(nums) - i >= k:
            return pivot
        # small >= k, search in small portion
        return self.findKthLargest(nums[:i], k-len(nums)+i)