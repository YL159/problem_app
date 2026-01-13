'''
Leetcode 2426. Number of Pairs Satisfying Inequality
Given nums1 and nums2 of the same length, and int diff.
Find # of index pairs (i, j), i < j and nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff

Observation:
Rearrange equation: n1[i]-n2[i] <= n1[j]-n2[j] + diff
    => prepare arr = n1-n2, thus arr[j] >= arr[i] - diff

Method 1, loop for all j on each i, takes O(n^2) time

Method 2, modify merge sort: count while merging
Inequality arr[i] <= arr[j] + diff indicates 2-pointer (i, j) fast method if arr is sorted
    => but if sort arr first, the window may contain # with original index smaller than i (window's left edge)
    => for each arr[i] (or arr[j]), we want the search range ALL to the right (or left) of i (or j)
        yet remaining sorted for fast 2-pointer-like counting
This is similar to merge sort process, where both halves are sorted, and separated before merging
    => separated means all the left # are to the left of all the right # in the original order
    => each half is internally decided (pair count resolved), thus only decide pairs between left-right halves

Time O(nlogn), Space O(n) because only 1 branch of split tree exists at any given time
'''

from typing import List

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        arr = [nums1[i]-nums2[i] for i in range(len(nums1))]

        def merge_sort(start: int, end: int) -> tuple:
            if end == start or end - start == 1:
                return 0, arr[start:end]
            mid = (start + end) // 2
            # resolve left and right halves, their respective count are collected
            # now left and right are sorted
            c1, left = merge_sort(start, mid)
            c2, right = merge_sort(mid, end)

            res = []
            i, i1, i2 = 0, 0, 0
            count = 0
            from_right = False

            # consider right half arr[j] >= left half arr[i] - diff
            # all numbers in left are potential arr[i], thus j > i is always true
            # current arr[j] from RIGHT segment should match some prefix of LEFT segment
            while i1 < len(left) or i2 < len(right):
                # deciding current x from left or right
                if i1 == len(left) or i2 < len(right) and right[i2] <= left[i1]:
                    x = right[i2]
                    from_right = True
                    i2 += 1
                else:
                    x = left[i1]
                    from_right = False
                    i1 += 1

                # since LEFT is sorted, some prefix of LEFT is the answer for x
                # since RIGTH is sorted, LEFT's idx i always move to right
                # thus time complexity within loop is minimized.
                if from_right:
                    while i < len(left) and x >= left[i] - diff:
                        i += 1
                    count += i
                
                res.append(x)
            return c1 + c2 + count, res
        
        return merge_sort(0, len(arr))[0]
            