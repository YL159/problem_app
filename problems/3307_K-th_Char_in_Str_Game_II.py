'''
Leetcode 3307. Find the K-th Character in String Game II
Starting with 'a', for each operations[i]:
	0: append a copy of str after str
	1: append a letter-shifted str after str
Find kth char in final str after all operations.

len(operations) < 100, k <= 10^14, final str length >= k
100 op gives 2^100 ~ 10^30 length word, but k <= 10^14
thus k <= 10^14 < 2^50 << 2^100, we can only consider operation 49th or less

Similar to #3304. Find the K-th Character in String Game I, but may copy current str directly.
Observation:
	1. After each operation, str length is doubled
	2. All letters in current str trace back to initial 'a', thus "revert" the trace of kth letter
=> current kth letter comes from (k-2^t)th letter, where 2^t is the largest 2-power < k
	and record whether this operations is 1/0: shift/no shift
Repeat until k = 1, thus infer the original letter from 'a' and accumulated shifting operations

Time O(log(k)), Space O(1)
'''
from typing import List

class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        change = 0
        # the index of final operation that definitely covers k
        idx = min(49, len(operations)-1)
        # the 2-power close to k
        p2 = 1 << idx
        while k > 1:
            # kth letter comes from 1st half's counter part, record operation
            if p2 < k:
                k -= p2
                change += operations[idx]
            p2 >>= 1
            idx -= 1
        return chr(ord('a') + change % 26)
