'''
Leetcode 873. Length of Longest Fibonacci Subsequence
Given an increasing arr, find the length of longest Fibonacci-like suubseq. Length >= 3

Time complexity is at least o(n^2)
	Because each pair in arr could be a potential (x0, x1) for a fib-like seq
Instead of matching prev 2 terms of current term
	we preprocess the arr and check valid (x0, x1) that	has x0+x1 in the arr
    and then iterate each valid x0 as start using DFS to record longest fib-seq
To avoid repeatedly checking a subseq of some evaluated fib-seq, we should remove every x1 from x0's candidate list
	e.g. [3, 4, ...] is a valid subseq of [1, 3, 4, ...], and all later subseqs are definitely shorter
    thus remove 4 from set of x1 of 3 as x0, remove 7 from set of x1 of 4 as x0, ...
    DFS subtree pruning

Time complexity O(n^2), space complexity O(n^2)
'''
from typing import List
import collections

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        self.nums = set(arr)
        # x0: [x1 ... ] valid (x0, x1i) that has x0+x1i in arr
        self.record = collections.defaultdict(set)
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                if arr[i] + arr[j] in self.nums:
                    self.record[arr[i]].add(arr[j])
        res = 0
        for i in range(len(arr)-1):
            if arr[i] not in self.record or not self.record[arr[i]]:
                continue
            res = max(res, self.DFS(arr[i]))
        return res

    def DFS(self, start: int) -> int:
        max_len = 0
        for nex in self.record[start]:
            cur = start
            count = 3
            while nex in self.record and cur + nex in self.record[nex]:
                count += 1
                cur, nex = nex, cur + nex
                # avoid future start (2,3) cus it's part of 1,2,3,5...
                self.record[cur].remove(nex)
            max_len = max(max_len, count)
        return max_len
        