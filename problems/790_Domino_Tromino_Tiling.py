'''
Leetcode 790. Domino and Tromino Tiling
Find ways to fully tile a 2*n board with domino and tromino tiles

DP on full tilings and lack-1 on last column tilings.
New full tiling derives from previous full tiling and lack-1 tiling.
And also update lack-1 tiling from previous full tiling and lack-1 tiling.

Essentially 2 intertwined recurrence sequence.
'''
class Solution:
    def numTilings(self, n: int) -> int:
        # dp_full[i] is ways of full tiling for 2*n board
        dp_full = [0, 1, 2, 5]
        # dp_1[i] is ways of lack-1 in last col tiling for 2*n board
        dp_1 = [0, 0, 2, 4]
        for i in range(4, n+1):
            # full tiling: full[i-1] add verti domino, full[i-2] add 2 horiz domino
            # and lack-1 tiling[i-1] add tromino
            dp_full.append(dp_full[i-1] + dp_full[i-2] + dp_1[i-1])
            # lack-1 tiling: lack-1[i-1] add domino, full[i-2] add 1x tromino 2 ways
            dp_1.append(dp_1[i-1] + dp_full[i-2]*2)
        return dp_full[n] % (10**9 + 7)
