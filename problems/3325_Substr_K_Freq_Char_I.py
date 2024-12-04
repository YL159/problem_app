'''
leetcode 3325. Count Substrings With K-Frequency Characters I
Count the # of substr with at least 1 char of freq at least k.
Substr with different start:end count as different.

Similar to 2958, keep letter idx list & running prefix counter
Use current i as distinct end of substr, all start idx:
	before prev k of current c's idx	abcdjdgc, k = 2, at 2nd 'd'
    or before previous 'char >= k' idx. abcdjdgc, k = 2, at 'g'
contributes a valid subarr

Thus at each idx, # of good substr is determined.
Time O(n), space O(n)
'''
import collections

class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        pos = collections.defaultdict(list)
        pref = collections.defaultdict(int)
        res = 0
        start = -1
        for i, c in enumerate(s):
            pos[c].append(i)
            pref[c] += 1
            # if current c freq >= k, update start with c's valid start that eclose c >= k
            if pref[c] >= k:
                start = max(start, pos[c][pref[c] - k])
            # count valid subarr for each idx, either a new start , or inherit prev start
            res += start + 1
        return res
