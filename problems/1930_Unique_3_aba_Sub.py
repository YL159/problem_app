'''
Leetcode 1930. Unique Length-3 Palindromic Subsequences
Count all unique length-3 aba-like subsequences of a string

Find the start and end indices of each letter (max 26), start letter will be unique for each range.
Get the set of letters between each pair of [start, end] and count
'''

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # { letter: [start, end] } end=-1 means letter appear only once
        book = {}
        for i, c in enumerate(s):
            if c not in book:
                book[c] = [i, -1]
            else:
                book[c][1] = i
        # get the set of letters between each palindrome starter, O(26*n)
        book1 = {k:set() for k in book}
        for k, [start, end] in book.items():
            if end > 0:
                book1[k] = set(s[start+1:end])

        count = sum([len(v) for v in book1.values()])
        return count