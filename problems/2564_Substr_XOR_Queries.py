'''
Leetcode 2564. Substring XOR Queries
Given string of only 0 & 1s, for each query [first, second]:
find the min range of string's substr that represents val, and val xor first = second.
If multiple options, give smallest range idx.

Preprocess the queries:
	val xor first xor first = second xor first = val
Thus either 1: process val into binary str, match with s for 1st match, time O(q*n^2)
			2: preprocess s for all possible substr and their equivalent vals, time O(q + n^2)

Considering constraint: first and second < 10^9 => len(binStr(val)) <= 30
2nd method takes actually O(q + n*30) time
'''
from typing import List

class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        # get all possible val from substr of s takes O(n*30) at most
        n = len(s)
        book = {}
        for i in range(n):
            if s[i] == '0':
                if 0 not in book:
                    book[0] = [i, i]
                continue
            v = 0
            for j in range(i, min(n, i+30)):
                v *= 2
                v += s[j] == '1'
                if v not in book:
                    book[v] = [i, j]
        # time O(q)
        res = []
        for a, b in queries:
            val = a ^ b
            res.append(book.get(val, [-1, -1]))
        return res
    