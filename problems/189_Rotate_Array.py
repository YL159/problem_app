from typing import List
'''
189. Rotate Array
For method 3, jump & put each number to its target place in nums
requires O(1) space & O(n) time
If k & len(nums) are coprime, 1 such jump sequence will do
If not coprime, then #GCD such jumps starting from [0...GCD-1] will do
'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0:
            return
        # # 1. O(n) space, slice and put it back
        # tmp = nums[len(nums)-k:]
        # nums[k-len(nums):] = nums[:len(nums)-k]
        # nums[:k] = tmp
        # return

        # 2. deque rotate method

        # 3. O(1) space
        # outer GCD loop to make every num jump
        a, b = len(nums), k
        rem = 1
        while rem:
            rem = a % b
            a, b = b, rem
        # now a is gcd of len(nums) & k
        for i in range(a):
            nex = (i + k) % len(nums)
            tmp1 = nums[i]
            while nex != i:
                tmp2 = nums[nex]
                nums[nex] = tmp1
                nex = (nex + k) % len(nums)
                tmp1 = tmp2
            nums[i] = tmp1
        return
            
