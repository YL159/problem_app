'''
Leetcode 2981. Find Longest Special Substring That Occurs Thrice I
Special substr: a substr containing only 1 kind of char
Given string s, find the longest special substr that appears at least 3 times.

Since we only look for special substr, we can separate the given s into single-letter segments:
	aabcccrrba => aa, b, ccc, rr, b, a
Then aggregate them according to the letter, count their frequency:
	a: (aa, 1), (a, 1); b: (b, 2); c: (ccc, 1); r: (rr, 1)
	=> a: [(2, 1), (1, 2)]; b: [(1, 2)]; c: [(3, 1)]; r: [(2, 1)]
Process each char and find the global longest special substr length:
	starts from char's longest special substr, check overall occurrence. Reduce length by 1 each iteration.
	if found a length occur >= 3, record this length

Time O(n), space O(sqrt(n))
Preprocessing string s takes O(n).
For each letter, 26x, sort the substr frequency list is at worst O(sqrt(n)log(sqrt(n))),
	O(26*sqrt(n)log(sqrt(n))) = O(sqrt(n)log(n)) = O(n)
'''
import collections

class Solution:
    def maximumLength(self, s: str) -> int:
        # separate s into segments of different letters, aggregate them for checking
        book = collections.defaultdict(list)
        pre = 0
        for i, c in enumerate(s):
            if c == s[pre]:
                continue
            book[s[pre]].append(i-pre)
            pre = i
        book[s[pre]].append(len(s)-pre)
        # for each letter, check its longest substr that occur thrice
        res = -1
        for c in book:
            segments = [(k, v) for k, v in collections.Counter(book[c]).items()]
            segments.sort(reverse=True)
            length = segments[0][0]
            if length <= res:
                continue
            while length > 0:
                occur = 0
                found = False
                for l, t in segments:
                    if l >= length:
                        occur += (l - length + 1) * t
                        if occur >= 3:
                            res = max(res, length)
                            found = True
                    else:
                        break
                if found:
                    break
                length -= 1
        return res