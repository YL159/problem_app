'''
Leetcode 214. Shortest Palindrome
Given a string, find the shortest palindrome that has the string as suffix.

Start from middle and to the left (because the answer can't be shorter than the string),
For current suffix, check if the remaining prefix's reversion is that suffix's prefix.

Don't think KMP algorithm is useful in reducing time complexity here.
Because for each potential palindrome axis, the text (right part, suffix) and the pattern (left part, prefix)
are different. No pattern is used to match in the middle of some text.
'''

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        limit = len(s) // 2
        for start in range(limit+1, -1, -1):
            # potential prefix repeats suffix
            left = s[:start][::-1]
            # potential prefix share 1 letter with suffix
            left1 = s[:start+1][::-1]
            right = s[start:]
            # check longer prefix first
            if right.startswith(left1):
                return right[1:][::-1] + right
            elif right.startswith(left):
                return right[::-1] + right
        return ''
