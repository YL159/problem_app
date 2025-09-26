'''
Leetcode 2197. Replace Non-Coprime Numbers in Array
Repeatedly replace 2 neighboring # in given array with their Least Common Multiple
Return the final array. The result is fixed no matter the order of replacement.

Since the order of replacement won't affect result, try merge numbers in 1 direction.
Suppose merging from right to left, e.g. [2,6,4,9]
	4, 9 are co-prime, leave them as they are.
    6, 4 are non-coprime, replace with LCM 12 = 6 * 4 // 2, GCD(6, 4) = 2
		now 12 , 9 are non-coprime, replace again with LCM 36 = 12 * 9 // 3
Thus we see that future merging may introduce new factors that may appear in previous #
	=> use stack to record the temporary/permanant result #
    => for each new nums[i] try to merge from stack top till co-prime appear, then add to stack

Time O(n), Space O(n)
'''

from typing import List

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        # merge from right to left
        # use stack, whenever merges, start from stack top if any
        stack = [nums[-1]]
        i = len(nums) - 2
        while i >= 0:
            # try to merge current nums[i] with stack tops
            while stack and (g := self.gcd(nums[i], stack[-1])) > 1:
                nums[i] = stack.pop() * nums[i] // g
            # append the possibly updated nums[i]
            stack.append(nums[i])
            i -= 1
        return stack[::-1]
    
    def gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a
