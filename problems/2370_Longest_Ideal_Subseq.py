'''
Leetcode 2370. Longest Ideal Subsequence
Find the longest subseq of given string s, that the diff(ascii(neighboring letters in subseq)) <= given k

Record the length of ideal subseq ending at each letter of current s[:t].
Adding s[t] is to update the opt subseq ending at this s[t].
The opt emerges from those subseq ending with letter in range(ascii(s[t])-k, ascii(s[t])+k) letters.

Time O(kn), space O(26) = O(1)
'''

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        # {char: int} record the max length of a subseq ending with char
        book = {}
        res = 0
        a, z = ord('a'), ord('z')
        for c in s:
            record = 0
            value = ord(c)
            # find the max length of previous subseq ending with a letter within range
            for v in range(max(a, value-k), min(z, value+k)+1):
                record = max(book.get(chr(v), 0), record)
            # replace/update the ending letter record
            book[c] = record + 1
            res = max(res, record + 1)
        return res
        