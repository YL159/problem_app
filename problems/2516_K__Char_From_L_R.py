'''
Leetcode 2516. Take K of Each Character From Left and Right
Given a string of only 'abc', and int k, find min operations to take k of each char.
1 operation: take 1 char from leftmost/rightmost of the string

Idea is sliding window, but evaluates the letter count of prefix/suffix of the window.
Initially find the suffix to take to just fulfill k of each char.
Move left pointer to the right, and move right pointer to the right as well,
	while maintaining the pref + suff to always meet k of each char
		compare the pref + suff length with global optimum

Time O(n), space O(1) because only 'abc' letters
'''
import collections

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        i, j = 0, len(s)-1
        book = collections.defaultdict(int)
        # find the largest idx j that [j:] meets 'all k' criteria
        while j >= 0:
            book[s[j]] += 1
            if all(book[x] >= k for x in 'abc'):
                break
            j -= 1
        if j == -1:
            return -1
        res = len(s) - j
        # sliding window, move left pointer i to the right
        while i < len(s):
            book[s[i]] += 1
            # move j to the right, but always maintain book[x] >= k for all x
            while j < len(s) and book[s[j]] > k:
                book[s[j]] -= 1
                j += 1
            res = min(res, len(s) - j + i + 1)
            if j == len(s):
                break
            i += 1
        return res