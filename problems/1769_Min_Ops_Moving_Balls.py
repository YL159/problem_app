'''
Leetcode 1769. Minimum Number of Operations to Move All Balls to Each Box
Incrementally calculate current moves based on previous moves.
O(n) time, O(1) space
'''
from typing import List
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0]
        # initialize left, middle, right count of 1s
        m = int(boxes[0])
        l, r = 0, sum([int(i) for i in boxes]) - m
        for i, n in enumerate(boxes):
            if n == '1':
                ans[0] += i
        # loop again and modify from the starting value
        # the step should be precise as follows
        cur = ans[0]
        for n in boxes[1:]:
            cur -= r
            l += m
            m = n == '1'
            r -= m
            cur += l
            ans.append(cur)
        return ans