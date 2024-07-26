'''
Leetcode 413. Arithmetic Slices
Identify # of arithmetic subarrays in an array. len(subarray) >= 3.

To identify an arithmetic subarray of at least 3 elements, derive the 2nd order difference array:
nums:	1,3,5,7,9,10,8,6
diff:	 2,2,2,2,1,-2,-2
2nd diff: 0,0,0,-1,-3,0

Though total 3 passes, time complexity is still O(n) and loop logic is simpler.

# of zeros indicates # of arithmetic triplets.
And the # of arithmetic subarrays in a grand arithmetic array is:
triplets * (triplets + 1) / 2
or
1 + 2 + ... + triplets
'''

from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
		# 1st order difference
        diff = [nums[i+1] - nums[i] for i in range(len(nums)-1)]
        # 2nd order difference
        consec = [diff[i+1] - diff[i] for i in range(len(diff)-1)]
        res, count = 0, 0
        for n in consec:
            # count 0s and accumulate on result
            if n == 0:
                count += 1
                res += count
            # reset count of 0
            else:
                count = 0
        return res