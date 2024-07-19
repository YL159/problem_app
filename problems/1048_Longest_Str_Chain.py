'''
Leetcode 1048. Longest String Chain
Find longest string chain where each is a predecessor of its next.

Reduce from longest words, check if any predecessor exists in next layer.
Record the length of the chain a word can form.
'''
from typing import List
import collections

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # create dict. len(word):set(same length words)
        book = collections.defaultdict(set)
        for word in words:
            book[len(word)].add(word)
        
        res = 1
        length = max(book.keys())
        # word as predecessor:longest length, starts with default 1
        cur = {x:1 for x in book[length]}
        while length > min(book.keys()):
            if length-1 not in book:
                length -= 1
                continue
            nex = {x:1 for x in book[length-1]}
            # check current layer word has any predecessor in nex layer, update length
            for word in book[length]:
                for i in range(len(word)):
                    predecessor = f'{word[:i]}{word[i+1:]}'
                    if predecessor in book[length-1]:
                        nex[predecessor] = max(nex[predecessor], cur[word]+1)
            res = max(res, max(nex.values()))
            length -= 1
            cur = nex
        return res