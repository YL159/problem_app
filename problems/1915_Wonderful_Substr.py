'''
Leetcode 1915. Number of Wonderful Substrings
Given a string of only a-j, find # of substr has at most 1 letter appear odd times.
Same substr at different idx are different.

For any substr, we can use prefix str for memoed check.
Thus each prefix gives count of each letter, to compare with later prefix's letter count.
If compare 1 by 1 of earlier prefix, inner loop takes O(n) time.
If compare only the oddity of each letter, and consider max 1 idx oddity difference
	Use oddity bit repr of all letters a-j and dict, to efficiently check if target bit repr was seen
	Inner loop time O(10) -> O(1)

Time O(n), space O(n)
'''
import collections

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        # use 2sum idea to remember a seen prefix check of odd letters
        book = collections.defaultdict(int)
        a = ord('a')
        # count oddity of j-a. 1-odd, 0-even
        odds = 0b0
        res = 0
        book[0] = 1 # '' is wonderful as well, act as pref[0] = 0
        for c in word:
            odds ^= 1 << ord(c) - a
            res += book[odds]
            book[odds] += 1
            for i in range(10):
                code = odds ^ 1 << i
                res += book.get(code, 0)
        return res