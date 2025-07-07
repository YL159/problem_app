'''
Leetcode 115. Distinct Subsequences
Given str s and target str t, find # of all distinct index-wise subsequence of s that equals t

Traverse s from left to right (or reverse)
e.g. s = babgag, t = bag
At 1st 'g': needed by prev 'ba', thus # of 'bag' should increase # of cur 'ba' (cur 1)
At 2nd 'g': needed by 'ba' again, # of 'bag' should increase # of cur 'ba' (cur 3)
	=> if cur char is needed by some unfinished prefix t[,x], promote it's count to t[,x+1]

Thus we can use 2D DP array of (s*t), each row is for s[i], derive from only prev row
Or we use only 1 array of length t, just propagate from right to left to avoid updating shorter prefix before using it
	=> Use incremental count DP array of length t on each char of s
Time O(s*t), Space O(t)
'''
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # left padding 1 char for start match
        # promote[i+1] is the count of prefix t[,i] as subseq in s[, cur_idx]
        promote = [0] * (len(t)+1)
        # all count comes from 1st char match, thus only 1st char match gives unconditional 1 increment
        promote[0] = 1
        for c in s:
            # promote count in reverse to reuse 'promote' arr instead of cur-nex array, or 2D DP
            for i in range(len(t)-1, -1, -1):
                if c == t[i]:
                    promote[i+1] += promote[i]
        return promote[-1]