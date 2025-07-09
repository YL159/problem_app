'''
Leetcode 719. Find K-th Smallest Pair Distance
Given nums array, of all the abs(dist(nums[j]-nums[i])), i < j
Find kth smallest distance

Since we look for absolute distance between different (i, j)
we can sort the array and use latter - former nums to unpack abs()

Method 1, brutal force find smallest kth distance
Heap optimize space use
Time O(n^2log(n)), Space O(n)

Method 2, For a potential distance X, check how many pairs with abs(dist) <= X
Binary search for the smallest X that gives k smaller pairs
	=> inner loop accumulate the count for each nums[i]
    => bisect on max idx within X dist of nums[i]
Time O(nlog^2(n)), Space O(1)

Method 3, improve on method 2, accumulate count with 2 pointers
Since the array is sorted, use 2 pointers to find new boundary of X range of nums[i]
Time O(nlog(n)), Space O(1)
'''
import heapq
import bisect
from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # method 1, almost like brutal force
        # Time O(n^2log(n))
        nums.sort()
        # heap on each nums[i]'s next smallest dist
        # heap of tuple (dist to nums[i], i, cur greater idx than i)
        hp = []
        for i in range(len(nums)-1):
            heapq.heappush(hp, (nums[i+1]-nums[i], i, i+1))
        while k > 0:
            d, i, j = heapq.heappop(hp)
            j += 1
            if j < len(nums):
                heapq.heappush(hp, (nums[j]-nums[i], i, j))
            k -= 1
        return d
        
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # method 2, binary search for the dist X that has exactly k dist <= X
        # for each nums[i], bisect for # of nums[j] within X range, nlogn
        # Time O(nlog^2(n))
        nums.sort()
        # l: min absolute impossible dist; r: max absolute possible
        l, r = -1, nums[-1]-nums[0]
        while l < r-1:
            X, count = (l+r)//2, 0
            for i in range(len(nums)-1):
                # find min idx of nums[j] > nums[i]+X
                count += bisect.bisect(nums, nums[i] + X) - i - 1
            if count < k:
                l = X
            else:
                r = X
        return r

    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # method 3
        # smilar to method 2, but inner loop use 2 pointers to count valid pairs
        # time O(nlogn)
        nums.sort()
        l, r = -1, nums[-1]-nums[0]
        while l < r-1:
            X, count = (l+r)//2, 0
            j = 1
            for i in range(len(nums)-1):
                while j < len(nums) and nums[j] - nums[i] <= X:
                    j += 1
                count += j - i - 1
            if count < k:
                l = X
            else:
                r = X
        return r