'''
Leetcode 30. Substring with Concatenation of All Words
Given a string s, and list of words of the same length
Find list of start idx in s:
	a substr at idx is a Concat Str of all words in list
Concat Str: each word exactly once, and no other irrelevant chars.

let n = len(words), m = len(words[0])
1. Use sliding window method: A concat str is fixed length of n*m. 
2. Optimize sliding window by offset in range(m): A window shift by m
	<=> each middle token/word of length m remains the same word, except for start/end word
Thus we can use word frequency + hashmap to check valid window on the run

Here used words index encoding, to transform the window validation into following problem:
	check subarr of encoding is a permutation of [0, n-1]
Also using idx rotate mechanism to distinguish same word in words

e.g. s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"], n = m = 4
At offset 0, s => "word good good good best word"
		=> encoding = [0, 1, 1, 1, 2, 3, -1]
        check subarr of length 4 if it's a permutation of [0, 1, 2, 3]
At offset 1, s => "w ordg oodg oodg oodb estw ord", omit offset prefix 'w'
		=> encoding = [-1, -1, -1, -1, -1, -1]
        no subarr between two -1 are of length 4
etc. for offset 2, 3

Time O(m*n), space O(m*n)
'''
from typing import List
import collections

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n, m = len(words), len(words[0])
        if len(s) < n*m:
            return []
        # pos: idx list of a word in words
        # book: current idx of word idx list in pos.
        pos, book = collections.defaultdict(list), {}
        for i, w in enumerate(words):
            pos[w].append(i)
            book[w] = 0
        res = []
        for offset in range(m):
            encode = []
            i = offset
            while i < len(s):
                w = s[i:i+m]
                if w in book:
                    # word idx ROTATE encoding
                    j = book[w] % len(pos[w])
                    encode.append(pos[w][j])
                    book[w] += 1
                else:
                    encode.append(-1)
                i += m
            if not encode or encode[-1] >= 0:
                encode.append(-1)
            res.extend(self.checkPermute(encode, offset, n, m))
        return res

    # check if a subarr of encode contains permute of [0, n-1]
    def checkPermute(self, encode: List[int], offset: int, n: int, m: int) -> List[int]:
        if len(encode) - 1 < n:
            return []
        idx = [i for i in range(len(encode)) if encode[i] == -1]
        res = []
        start = 0
        for end in idx:
            if end - start < n:
                start = end + 1
                continue
            # sliding window on each subarr of length n in range encode[start:end]
            l, r = start, start+n-1
            book = collections.Counter(encode[l:r])
            while r < end:
                book[encode[r]] += 1
                if len(book) == n:
                    res.append(offset + m*l)
                if book[encode[l]] == 1:
                    del book[encode[l]]
                else:
                    book[encode[l]] -= 1
                l += 1
                r += 1
            start = end + 1
        return res
        
