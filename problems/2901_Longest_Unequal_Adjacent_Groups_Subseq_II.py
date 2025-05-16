'''
Leetcode 2901. Longest Unequal Adjacent Groups Subsequence II
Given a list of words and a list of group numbers, group[i] is the group number of words[i].
Find any one of the longest subseq of words that for each neighboring words in the subseq:
	1. Corresponsing group # are different
	2. Hamming distance (count of different letter at each index) is 1
	3. Length are the same

Group words by length, search result in each subseq: Satisfy criteria 3
Within each list of same-length words, use DP list to record the longest word chain ending at that word
	and related information of the word chain
Thus for each new word, it needs to compare with all previous words and match:
	criteria 1 & 2
	but also chain with only the longest previous chains, to maintain the DP condition
    if multiple longest previous chains, any one will do
		because any later word that would chain current word will continue grow on this longest chain

Time O(n^2*m) for each list, n = len(tlist), m = len(word)
'''
from typing import List
import collections

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        # find the longest target subseq from same-length word list
        def getSubseq(tlist: List[tuple]) -> List[str]:
            # each word record (word, group, longest subseq, predecessor)
            dp = [(*tlist[0], 1, 0)]
            longest, end = 1, 0
            for i in range(1, len(tlist)):
                length, predi = 1, i
                word, group = tlist[i]
                # dp on all prev words as end, for each new word
                for j in range(i):
                    w, g, l, pre = dp[j]
                    if g != group and sum(a != b for a, b in zip(w, word)) == 1 and l + 1 > length:
                        length = l + 1
                        predi = j
                if length > longest:
                    longest, end = length, i
                dp.append((word, group, length, predi))
            # construct word list from the longest subseq, ending at idx "end"
            # use predicessor till it points to itself
            w, _, _, pre = dp[end]
            seq = [w]
            while pre != end:
                end = pre
                w, _, _, pre = dp[end]
                seq.append(w)
            return seq[::-1]
        
        # group same-length words in a list ordered by index
        book = collections.defaultdict(list)
        for i in range(len(words)):
            book[len(words[i])].append((words[i], groups[i]))
        # process each list from same-length word collection
        res = []
        for v in book.values():
            tmp = getSubseq(v)
            if len(tmp) > len(res):
                res = tmp
        return res
