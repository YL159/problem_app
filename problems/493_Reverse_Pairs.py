'''
Leetcode 493. Reverse Pairs
Given an int array, count # of reverse pairs:
Pair index (i, j), i < j and nums[i] > 2 * nums[j]

Method 1, direct approach
For each j, find prev idx i that satisfy nums[i] inequality.
Since nums is unordered, each nums[j] requires O(n) time search. Total O(n^2)

If sort nums in descending order first, with index info
For each j, nums' prefix that satisfy inequality will monotonically increasing
But still need to filter for those i < j. Total again O(n^2)

Method 2, modified merge sort
The problem requires order in both index and values.
Consider partially ordered structure in merge sort:
    left portion has all idx < right portion
    total linear time finding inequality range for each right nums[j], since left is sorted
And then merge sort as usual.
Time O(nlogn), Space O(nlogn)
'''

from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # consider merge sort
        # indices are apart yet partially sorted while merging
        self.count = 0
        self.merge_sort(nums)
        return self.count

    def merge_sort(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return arr
        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])
        
        i = 0
        # this nested loop runs O(len(arr)) time
        for n in right:
            target = n * 2
            while i < len(left) and left[i] <= target:
                i += 1
            self.count += len(left) - i
        
        return self.merge(left, right)
    
    def merge(self, left: List[int], right: List[int]) -> List[int]:
        res = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        if i == len(left):
            res.extend(right[j:])
        else:
            res.extend(left[i:])
        return res
        


