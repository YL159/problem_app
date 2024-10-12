'''
Leetcode 2799. Count Complete Subarrays in an Array
A complete subarr contains all distinct # of this arr. Count such subarr in given arr

Use sliding window on a tight complete subarr. Tight => head of complete subarr appears only once.
Current complete subarr became not tight => include another same head # from right
If not tight, left + 1 and repeat.

As long as left/head is different, we can add:
Distinct complete subarrs with this head = count of right remaining # + 1
'''
from typing import List

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total = len(set(nums))
        count = 0
        # contain current number freq inside the [l:r] range
        book = {}
        l, r = 0, 0
        # initialize book as complete subarr
        while len(book) < total:
            if nums[r] in book:
                book[nums[r]] += 1
            else:
                book[nums[r]] = 1
            r += 1
            
        while r <= len(nums):
            count += len(nums) - r + 1
            # current nums[l] show only once, increase r to try find 1 more nums[l]
            if book[nums[l]] == 1:
                while book[nums[l]] == 1 and r < len(nums):
                    book[nums[r]] += 1
                    r += 1
            # after searching, nums[l] still show once
            # meaning can't increase l for any more complete subarr
            if book[nums[l]] == 1:
                break
            else:
                # head freq >= 2 means safely increase l
                book[nums[l]] -= 1
                l += 1
        return count