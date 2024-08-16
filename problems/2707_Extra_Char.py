'''
Leetcode 2707. Extra Characters in a String
Partition a given string with words in dictionary, find the minimum extra chars of all such partitions.

Precalculate dict of lists of the same ending letter from words in dictionary
Use DP array to record s[0:i] prefix's min extra chars.
DP[i+1] = DP[-1] + 1 if s[0:i+1] has no suffix match in dictionary
		= min(DP[i-len(w)] for all suffix matching w)
'''
from typing import List
import collections

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        short = float('inf')
        book = collections.defaultdict(list)
        # construct a dict {last letter of word: [list of such words]}
        for w in dictionary:
            short = min(short, len(w))
            book[w[-1]].append(w)
        # DP on extra char in s[:i].
        # Check if s[i-len(w):i] match w, extra char will be the same as dp[i-len(w)]
        dp = [i for i in range(short)]
        for i in range(short, len(s)+1):
            res = dp[i-1] + 1
            for w in book[s[i-1]]:
                if len(w) <= i and w == s[i-len(w):i]:
                    res = min(res, dp[i-len(w)])
            dp.append(res)

        return dp[-1]