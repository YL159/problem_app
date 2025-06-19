'''
Leetcode 1838. Frequency of the Most Frequent Element
Given a list of ints. One operation: bump up a number by 1
Find the most frequently appeared elements after max k such operations.

Each distinct number can be the target for other smaller numbers to bump up to.
For distinct nums[i], greedily bump up closest and smaller numbers to match it, then even smaller ones
	=> Sort the distinct numbers. For each target, sequentially bump up its left numbers

Sorting takes O(nlogn) time, but if naively traverse each smaller numbers to the left, it would take O(n^2) time
	=> Use 2-pointer sliding window to maintain a window where bump ups <= k
    => Bump up all previously included numbers to the current target, operations may exceed k
    => Greedily exclude some smallest numbers, in order to maximize the reduction of excessive bump ups
Thus achieving O(n) window traversal

Time O(nlogn), Space O(n)
Sorting nums without counting frequencies is the same.
'''
import collections
import math
from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # use 2-pointer sliding window or deque
        book = collections.Counter(nums)
        arr = sorted(list(item) for item in book.items())
        i, j = 0, 0
        up, freq = 0, 0
        res = 0
        prev = arr[0][0]
        while j < len(arr):
            cur, n = arr[j]
            # let all numbers (= previous number) in window bump up to current target
            up += freq * (cur - prev)
            freq += n
            # exclude smallest numbers untill bump up <= k
            while up > k:
                small, m = arr[i]
                diff = cur - small
                remove = min(m, math.ceil((up - k) / diff))
                freq -= remove
                up -= remove * diff
                if remove == m:
                    i += 1
                else:
                    arr[i][1] -= remove
            res = max(res, freq)
            prev = cur
            j += 1
        return res
