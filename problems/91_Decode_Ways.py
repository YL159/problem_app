'''
Leetcode 91. Decode Ways
'1' -> 'A' ... '26' -> 'Z'. Given a number string, find how many ways to decode to some letter string

Use DP on current substr [,i]. Current decodes depends only on decodes of [,i-2] and [,i-1]
pre: # of decode for substr [,i-2]. Has to initialize with 1 here
cur: # of decode for substr [,i-1]

Early return on '0' special cases.
Time O(n), space O(1)
'''

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        pre, cur = 1, 1
        i = 1
        while i < len(s):
            two = int(s[i-1:i+1])
            if s[i] == '0':
                if s[i-1] == '0' or two > 26:
                    return 0
                pre, cur = cur, pre
            else:
                tmp = cur
                if 10 <= two <= 26:
                    tmp = cur + pre
                pre, cur = cur, tmp
            i += 1
        return cur