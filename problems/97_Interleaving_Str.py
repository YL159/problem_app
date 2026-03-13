'''
Leetcode 97. Interleaving String
Given string s1, s2, check if they can interleaving into string s3.
Interleaving keeps letter order from each string.

Method 1, s1-s2 matrix DP
Use a matrix of n*m to transfer interleaving state: s1[:i] and s2[:j] into s3[:i+j]
    to new state: s1[i] match s3[i+j] and dp[i-1][j] permits, or s2[j] match s3[i+j] and dp[i][j-1] permits

Method 2, BFS and pruning
Let current level as all possible tuple (x, y) that s1[,x] and s2[,y] forms s3[,x+y]
Next level grows from current possibilities, check if any tuple can grow for s3[,x+y+1]
    => each existing tuple may generate 2 new tuple
    => use set to keep unique new tuples, avoid repeated exploring same tuples

Time O(mn), Space O(mn)
'''

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Method 2, BFS and pruning
        n, m, l = len(s1), len(s2), len(s3)
        if m + n != l:
            return False
        # (x, y) front x of s1 and front y of s2 can interleaf front x+y of s3
        level = {(0, 0)}
        z = 0
        while level and z < l:
            _level = set()
            for x, y in level:
                # if s1[x] match s3[z], grow from x's posibility
                if x < n and s3[z] == s1[x]:
                    _level.add((x+1, y))
                # same for s2[y]
                if y < m and s3[z] == s2[y]:
                    _level.add((x, y+1))
            if _level:
                z += 1
            level = _level

        return z == l