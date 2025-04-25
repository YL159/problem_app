'''
Leetcode 2845. Count of Interesting Subarrays
Count interesting Subarrs of given array. Interesting:
A subarr has cnt number of num % modulo = k, and cnt itself is also cnt % modulo = k

e.g.[1,3,2,5,7,10,13], modulo = 3, k = 1

First, convert each nums[i] to 1 if nums[i] % modulo = k, else 0:
	[1,0,0,0,1,1,1]

Thus the problem becomes finding the interesting subarr containing cnt 1s
	=> find the subarr of sum cnt => use prefix sum array for quick subarr sum detect
    [0,1,1,1,1,2,3,4], left padding 0 meaning subarr from idx=0
Since 1/0 array has only 1/0 => prefix sum must grow +1 at a time

Now for some pref p1, we need to find its matching earlier pref p2, that (p1-p2) % modulo = k
We can record starting idx in nums of pref sum of 0,1,2,...
	{0:0, 1:1, 2:5, 3:6, 4:7} Then check each previous p2 and see if valid.
but for p1 = 4, matching p2 is {0, 3}, => {0, 3} is the same in p1=4's eye
	=> {0, 3} are the same because both % modulo = 0

One step further, use dp to record the frequency of pref sums that has same % modulo remains
	[0,1,1,1,1,2,3,4] pref sum array
	[0:2, 1:5, 2:1], % modulo ramain 0 is pref {0, 3}, 2 count; remain 1 is pref {1,1,1,1,4}, 5 count ...
Thus for each new pref p1: (p1-p2) % m = k => p1-p2 = k + x*m => p2%m = p1%m - k (mod m)
it can match any of above prefix sum p2 to get desired subarr.

Time O(n), Space O(modulo)
'''
import collections
from typing import List

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        # dict or array to store remainder: count of prefix sum % m = remainder
        book = collections.defaultdict(int)
        pref = 0
        book[0] = 1
        res = 0
        for n in nums:
            # current prefix sum p1 and its remainder
            pref += n % modulo == k
            cur_rem = pref % modulo
            # find matching previous p2 remainder count, add to result
            res += book[(cur_rem - k) % modulo]
            # increment p1 remainder count
            book[cur_rem] += 1
        return res