'''
Leetcode 1268. Search Suggestions System
Output at most 3 sorted word suggestions when typing each letter of searchWord

Use binary search to find the start-stop positions of current input in sorted words array
'''

from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        m, n = len(products), len(searchWord)
        res = [[] for _ in range(n)]
        start, stop = 0, m
        for i in range(n):
            l, r = self.bs(products[start:stop], searchWord[:i+1])
            start, stop = start + l, start + r
            stop1 = min(stop, start+3)
            res[i].extend(products[start:stop1])
        return res
    
    def bs(self, prod: List[str], sub: str) -> tuple:
        n = len(sub)
        c = sub[-1]
        l = bisect_left([len(p) for p in prod], len(sub))
        tmp = [p[n-1] for p in prod[l:]]
        left = bisect_left(tmp, c)
        right = bisect_right(tmp, c)
        return l+left, l+right