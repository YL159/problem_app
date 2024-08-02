'''
Leetcode 1143. Longest Common Subsequence
Find the longest common subseq between 2 strings.

New lcs is built on existing lcs of smaller prefix substrings.
Make a DP matrix of lcs that keeps the lcs of text1[:i] and text2[:j].
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # DP on text1[:i] and text2[:j] prefix
        m, n = len(text1), len(text2)
        lcs = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                # Can also use matrix left-up padding by 0 to avoid edge test
                left = lcs[i][j-1] if j > 0 else 0
                up = lcs[i-1][j] if i > 0 else 0
                lu = lcs[i-1][j-1] if i > 0 and j > 0 else 0
                # if current end chars match, it definitely adds 1 to lcs of t1[:i) and t2[:j)
                if text1[i] == text2[j]:
                    lcs[i][j] = lu + 1
                # if end chars don't match, result is max between:
                # lcs of t1[:i] and t2[:j)
                # lcs of t1[:i) and t2[:j]
                else:
                    lcs[i][j] = max(left, up)
        return lcs[-1][-1]
