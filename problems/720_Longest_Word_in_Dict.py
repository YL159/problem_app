'''
Leetcode 720. Longest Word in Dictionary
Find the longest word in a given word list, that all of its prefix is also in list
Return the smallest lex word if multiple valid longest words found

Method 1:
Use Trie to store each word. Then check for valid longest in the trie.
Here add (-1: word idx) entry for each word. 'eat' -> {e: {a: {t: {-1: idx}}}}
	thus any prefix that doesn't have -1 key in its next level, is not present in word list
	e.g. a single word 'eat' without 'e' and 'ea' (no -1 in 'e' dict) will stop its subtrie traversal
Then traverse the trie for valid path (each level has -1 key)
Time O(n), space O(sum(word length))

Method 2:
Sort the word list, BFS check each word length from 1 to max len.
	current pref that don't have any children, die out
	next pref that can't grow from current pref won't be next candidate
Time O(nlog(n)), space O(sum(word length))
'''
from typing import List

class Solution:
    def longestWord(self, words: List[str]) -> str:
        # Trie solution
        # padding '' as -1 key for book itself
        words.append('')
        book = {-1: -1}
        for i, word in enumerate(words):
            cur = book
            for c in word:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            # \0 end for current word, referring word idx
            cur[-1] = i
        
        res = ''
        cur = [book]
        # iterative BFS
        while cur:
            nex = []
            for bk in cur:
                for k in bk:
                    if k == -1 or -1 not in bk[k]:
                        continue
                    nex.append(bk[k])
            if not nex:
                res = min(words[boo[-1]] for boo in cur)
            cur = nex
        return res
