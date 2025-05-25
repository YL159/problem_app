'''
Leetcode 2271. Maximum White Tiles Covered by a Carpet
Given a list of non-overlapping white tile ranges [l_i, r_i], and a carpet length,
find the max white tiles can be covered by the carpet.
Len(tiles) <= 5E4, r_i <= E9, carpet <= E9

Method 1, make a line of E9 length and line sweep on tiles
get the white/non-white config of the whole range
then just sliding fixed window, O(max(r))
also workable for over-lapping tiles
Time O(max(r)), Space O(max(r))

Method 2, sliding window on sorted tiles
same idea as method 1 but traverse tiles instead
since traversing sorted tiles take max time 5E4*log(5E4) = 7.6E5 << E9
Time O(t), Space O(1)
'''
from typing import List

class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        res, count = 0, 0
        r = 0
        # covered tiles of the head range; covered tiles of the tail range
        head, tail = 0, 0
        for l, (left, right) in enumerate(tiles):
            if r == len(tiles):
                break
            end = left + carpetLen - 1
            r = max(l, r)
            # r stop at unfinished new tile range
            while r < len(tiles):
                rl, rr = tiles[r]
                if end >= rr:
                    cur = rr - rl + 1
                    r += 1
                else: # end < rl or end < rr, tiles[r] is unfinished
                    cur = max(0, end - rl + 1)
                count += cur
                tail = cur
                if end < rr:
                    break
            res = max(res, count)
            # remove the head tiles
            # if current range is unfinished, head reset to 0
            if l == r:
                head = 0
            else:
                head = tiles[l][1] - tiles[l][0] + 1
            count -= head
            count -= tail
        return res