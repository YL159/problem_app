'''
Leetcode 403. Frog Jump
Given the positions of stones in ascending order in a linear river
	A frog starts at 1st stone, initially jump 1 unit
	Each later jump can be (k-1, k, k+1) units, where k is the last jump unit
	Frog can only jump to forward
Find if the frog can reach the last stone.

Basically we want to know all the possible jump units reaching ith stone
thus to determine the next stones to reach
	=> for each previous jump unit, its 3x jump options can be added to some valid future stones
    => keep a set of jump units of each stone
Then use incremental method to update each stone's jump unit set
Check if the last stone has any thing in its set.

Complexity analysis:
The maximal reachable jump unit count happens when each jump can reach some stone:
	stones = [0,1,2,3,4,5,6,...]
Keeping 1 unit jump can always reach any stone
Consider stone 1, keeping max jumps (always choose k+1) -> 3 -> 6 -> 10 -> 15 ...
	=> 10, 11, 12, 13, 14 all have [1,2,3,4] prev jump units, 15 has [1,2,3,4,5]
Thus the growth of the prev jump unit set for each stone is of O(n^0.5)
	=> Time O(n*n^0.5) = O(n^1.5)
    => Space O(sigma[(k*(k+1)/2)]) and k*(k+1)/2 ~ n => O(n^2)
Time O(n^1.5), Space O(n^2)
'''

from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        pos = set(stones)
        book = {k: set() for k in stones}
        book[1] = {1}
        for i in range(1, len(stones)):
            for unit in book[stones[i]]:
                for jump in [unit-1, unit, unit+1]:
                    if jump > 0 and stones[i] + jump in pos:
                        book[stones[i]+jump].add(jump)
        return len(book[stones[-1]]) > 0