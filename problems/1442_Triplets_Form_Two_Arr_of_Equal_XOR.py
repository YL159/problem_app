'''
Leetcode 1442. Count Triplets That Can Form Two Arrays of Equal XOR
Given array of ints, find # of triplet idx i < j <= k so that:
	a := XOR(arr[i,j-1]) == b := XOR(arr[j,k])

a = b <=> a xor b = 0 <=> xor(arr[i,k]) = 0
Thus find all the subarrs of XOR reduce to 0 <=> prefix XOR(arr[,i-1]) = prefix XOR(arr[,k])
	because x xor 0 = x
Within arr[i,k], any non-empty 2-partition will suffice => arr[i,k] has at least 2 elements.
Since arr[i] > 0 => no consecutive same pref in pref arr, which guarantee k-i >= 2
Then use 2-sum "seen before" dictionary to get all seen-before prefix, and count unique partitions.
'''
from typing import List
import collections

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        pref = 0
        seen = collections.defaultdict(list)
        seen[0] = [-1]
        res = 0
        for i, n in enumerate(arr):
            pref ^= n
            if pref in seen:
                # between i and each prev seen pref value
                # there are i-idx-1 ways to get the triplets
                for idx in seen[pref]:
                    res += i - idx - 1
            seen[pref].append(i)
        return res
