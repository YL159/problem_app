'''
Leetcode 42. Trapping Rain Water
Given a list of non-negative int wall heights, find the max unit of water they can trap.

Method 1, find each cell's left/right tallest wall
Thus each cell's water must either level with min(left_tall, right_tall), or no water
	=> use prefix max to find each cell's left tallest, and again for suffix max for right tallest
    => traverse function is reusable
Time O(n), Space O(n), logic and implementation is easier


Method 2, 2-pointer seeking tallest wall
Since we care only the prefix/suffix max of a cell, ideally the max is/are in the middle
	=> prefix max will change until this global max, so is suffix max
    => suffix max changing portion won't affect the changing portion of prefix max
	=> use 2 pointer to simulate the traversal, collect water on the way
Time O(n), Space O(1)

Method 3, improve on 2-pointer
Each iteration determines left cell or right cell:
    => cell water determined by current left max and right max
    => if left max is smaller, any future right is taller or smaller doesn't affect cell water
    => if right max is smaller, same for any future left height recorded
Update left/right max height on the way
Time O(n), Space O(1)
'''

from typing import List


class Solution:
    
	# Method 1, find tallest wall from left & right of each cell
	# cell water = min(left, right) - cell, min 0
    def trap(self, height: List[int]) -> int:

        # find each cell's left tallest wall
        def left_tall(arr: List[int]) -> List[int]:
            tall = 0
            res = []
            for n in arr:
                tall = max(tall, n)
                res.append(tall)
            return res
        
        left = left_tall(height)
        right = left_tall(height[::-1])[::-1]
        return sum(min(a, b)-h for a, b, h in zip(left, right, height))
    

	# Method 2, 2 pointer version of seeking tallest mid-point and sweep both sides
    def trap(self, height: List[int]) -> int:
        # from left to right, climb to the highest, take n iteration
        # then from right to left, collect water till said highest, take max n iteration
        n = len(height)
        if n < 2:
            return 0
        stall, cur = 0, 1
        res, tmp = 0, 0
        while cur < n:
            if height[cur] > height[stall]:
                # pour tmp into res only when a taller wall is found
                stall = cur
                res += tmp
                tmp = 0
            else:
                # cache each trap in tmp
                tmp += height[stall] - height[cur]
            cur += 1
        # then start from the end, same thing till the tallest point - "stall"
        cur, rever = n-2, n-1
        while cur > stall:
            if height[cur] > height[rever]:
                rever = cur
            else:
                res += height[rever] - height[cur]
            cur -= 1
        return res
    

    # Method 3, 2 pointer improved, optimal
    def trap(self, height: List[int]) -> int:
        # 2 pointer improved
        # left record current left max, right the same
        left, right = 0, len(height)-1
        lmax = rmax = res = 0
        while left < right:
            lmax = max(lmax, height[left])
            rmax = max(rmax, height[right])
            # min(left max, right max) is current water level
            # for current min(left, right) position
            level = min(lmax, rmax)
            res += level - min(height[left], height[right])
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return res