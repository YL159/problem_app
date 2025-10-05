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
'''

from typing import List


class Solution:
    
	# method 1, find tallest wall from left & right of each cell
	# cell water = min(left, right) - cell, min 0
    def trap(self, height: List[int]) -> int:

        # find each cell's left tallest wall
        def left_tall(arr: List[int]) -> List[int]:
            tall = 0
            res = []
            for n in arr:
                res.append(tall)
                tall = max(tall, n)
            return res
        
        left = left_tall(height)
        right = left_tall(height[::-1])[::-1]
        return sum(max(min(a, b)-h, 0) for a, b, h in zip(left, right, height))
    

	# method 2, 2 pointer version of seeking tallest mid-point and sweep both sides
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