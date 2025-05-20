'''
Leetcode 1089. Duplicate Zeros
Insert one additional 0 after each 0 in arr in place.
Discard any element in result that exceeds arr length.

Method 1: Queuing all insertion elements using deque, work from left.
Time O(n), Space O(n)

Method 2: Count elements that can enter final arr, work from right.
Each original element -> 1 or 2 new element
	=> overwriting from right won't affect remaining element's new seats in final arr.
Time O(n), Space O(1)
'''
from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # # method 1, deque
        # dq = collections.deque()
        # for i, n in enumerate(arr):
        #     if n == 0:
        #         dq.append(0)
        #         dq.append(0)
        #     else:
        #         dq.append(n)
        #     if dq:
        #         arr[i] = dq.popleft()
        
        # method 2, O(1) space.
        # check which idx to stop, and replace from stop idx to start to avoid queing
        total, n = 0, len(arr)
        for i, x in enumerate(arr):
            total += 1 if x != 0 else 2
            if total >= n:
                break
        j = n-1
        # total > n, then the last element to include must be 0
        if total > n:
            arr[j] = 0
            j -= 1
            i -= 1
        # j >= i is always true
        while i >= 0:
            if arr[i] == 0:
                arr[j] = 0
                j -= 1
            arr[j] = arr[i]
            i -= 1
            j -= 1
        
