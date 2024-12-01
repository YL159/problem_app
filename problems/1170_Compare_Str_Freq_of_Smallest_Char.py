'''
Leetcode 1170. Compare Strings by Frequency of the Smallest Character
Given a word list, f(word) = freq(min char of word)
For each query str, find # of words that f(word) > f(query)

Each word & query str can be precomputed into an int =>
	Find # of int in word list, that w_int > q_int
Thus we get the result int list of words list,
	-> Count & sort distinct int
	-> Suffix sum array from the sorted distinct int as idx key
Thus each query <=> bisect for idx of larter list int -> get suffix sum from the idx

Time O((n+q)log(n)), space O(n+q)
'''
from typing import List
import bisect

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        # pre-compute words' f results
        book = {}
        for w in words:
            f = self.func(w)
            book[f] = book.get(f, 0) + 1

        # sort result keys & make suffix sum for quick query check
        f_res = sorted(book.keys())
        suff = [0] * (len(f_res) + 1)
        for i in range(len(f_res)-1, -1, -1):
            suff[i] = suff[i+1] + book[f_res[i]]
        
        # each query use O(log(n) + 1) -> O(log(n)) time
        res = []
        for q in queries:
            target = self.func(q)
            idx = bisect.bisect(f_res, target)
            res.append(suff[idx])
        return res

    def func(self, word: str):
        t = 0
        lex = 'z'
        for c in word:
            if c < lex:
                t = 1
                lex = c
            elif c == lex:
                t += 1
        return t
        