'''
Leetcode 72. Edit Distance
Given 2 words, find min # of op to make them equal.
Op: insert, delete, replace

Idea is to utilize as many common chars in words as possible, relate to 1143 Longest Common Subsequence problem
We also use a word DP matrix made of column as word2, row as word1.
The shortest distance betwen word1[:i] and word2[:j] come from DP of word1[:i-1~i], word2[:j-1~j]

If the last chars are the same:
	abbc -> abbc d, eef -> eef d. Then DP(eefd->abbcd) = DP(eef->abbc)
Else:
	abbc -> abbc t, eef -> eef g. Then DP(eefg->abbct) = min of:
		DP(eef->abbct) + 1 (delete g from eefg, because eef match the whole of abbct)
		DP(eefg->abbc) + 1 (insert t to eefg, because eefg is already matched with abbc)
		DP(eef->abbc) + 1 (replace g with t, because eef matches abbc)
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # col is for word2, row is for word1
        m, n = len(word1), len(word2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        # left-up padding both words with ''
        for j in range(1, n+1):
            dp[0][j] = dp[0][j-1] + 1
        for i in range(1, m+1):
            dp[i][0] = dp[i-1][0] + 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                # last char the same, then inherit distance from left-up dp
                if word2[j-1] == word1[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                # not the same, increment from smallest distance between top/left/left-top
                # top dist + 1 insert, left dist + 1 delet, left-top + 1 replace
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        return dp[-1][-1]