'''
Leetcode 395. Longest Substring with At Least K Repeating Characters
Find the length of title substr.

If all chars has freq >= k: whole string is valid
Some chars freq < k: avoid those chars' idx
	=> candidates must be inside these remaining segments
	=> char freq changes within these maximal candidate subarr
	=> same problem with smaller scale
Thus use divide & conquer to deal with the problem and smaller samel problems.
'''
import collections

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # divide and conquer. pivot on those idx of letter count < k
        # each subarr is the same problem with smaller scale
        if len(s) < k:
            return 0
        book = collections.defaultdict(list)
        for i, char in enumerate(s):
            book[char].append(i)
        # positions of invalid chars
        pos = []
        for v in book.values():
            if len(v) < k:
                pos.extend(v)
        if not pos:
            return len(s)
        pos.append(len(s))
        pos.sort()
        res = 0
        start = 0
        for end in pos:
            # divide and conquer on each potential subarr
            tmp = self.longestSubstring(s[start:end], k)
            res = max(res, tmp)
            start = end + 1
        return res
