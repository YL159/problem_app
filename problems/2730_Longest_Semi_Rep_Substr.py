'''
Leetcode 2730. Find the Longest Semi-Repetitive Substring
Semi-repetitive substr:
A substr containing at most 1 adjacent pair of same digit.

Method 1, preprocess neighbor digit same/diff info and check
e.g. 452233 -> 00101, for each neighbor, different -> 0, same -> 1
Find the longest window containing max one 1
Time O(n), Space O(n)

Method 2, upgrade from method 1, without extra space
Directly applying sliding window, but remember position of the last same neighbor
Time O(n), Space O(1)
'''

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        # Method 2, direct sliding window
        if len(s) <= 2:
            return len(s)
        l, r = 0, 1
        last = 0 # the 2nd idx of last encountered rep's idx
        res = 2
        while r < len(s):
            # now r is 2nd idx of current rep
            if s[r] == s[r-1]:
                res = max(res, r - l)
                l, last = last, r
            r += 1
        # wrap up, in case no same neighbor at the end
        res = max(res, r - l)
        return res

