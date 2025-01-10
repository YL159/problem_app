'''
Leetcode 2381. Shifting Letters II
Given a letter string s, and a list of (start, end, direction)
	for each tuple, shift each letter in range [start, end] to direction by 1. Wrap around z-a
Find final result of shifted string s

Brutal force is to shift each letter according to each operation.
But only 1 op on each letter, and future operations may cancel prev op.

If we see each shift tuple as differential of the changes, we can accumulate the point of changes before
realizing changes. And then shift each letter to its destination in 1 op.

Thus keep track of the shifting count on those turning points, and make changes later.
'''
from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # shifts are differential +/- ranges, record where to change
        # instead of accumulating each idx's shift (integration)
        changes = [0] * (len(s)+1)
        for start, end, fw in shifts:
            if fw == 0:
                fw = -1
            changes[start] += fw
            changes[end+1] -= fw
        # integrate each idx's shift by applying prefix sum of changes
        a, z = ord('a'), ord('z')
        res = []
        cur = 0
        for i in range(len(s)):
            cur += changes[i]
            cur %= 26
            char = ord(s[i]) + cur
            if char < a:
                char += 26
            elif char > z:
                char -= 26
            res.append(chr(char))
        return ''.join(res)
