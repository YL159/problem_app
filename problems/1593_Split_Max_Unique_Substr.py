'''
Leetcode 1593. Split a String Into the Max Number of Unique Substrings

Idea 1: Greedy on shortest new substr at idx.
	Not working. Because the split of s[i:j] + greedy(s[j:]) is not necessary optimum
Idea 2: DP on tail substr results.
	Not working. Because prefix split affects validity of some optimum tail split
		Even if we save all tail split results and find a valid one for a prefix split,
		it won't add any efficiency in time or space

Use backtrack on current prefix split, check if any tail split is possible, and return max split
This is n-ary tree traversal. Time is of small-o o(n!)

A good pruning is at `if cur in seen or len(s) - j < sub: continue`
	If # of remaining characters in s[j:] < current opt split
	(s[i:] split <= current optimum, including cur = s[i:j]),
		then any tail split won't contribute to an increase of opt split, thus skip
This helps pruning a lot of near-leaf nodes, which account for majority of n-ary tree nodes.
'''
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()

        # try all substr from idx, see if possible to split, record length
        # check max split for s[i:], -1 for impossible
        def backtrack(i: int) -> int:
            if i == len(s):
                return 0

            sub = -1
            for j in range(i+1, len(s)+1):
                cur = s[i:j]
                # leaf pruning
                if cur in seen or len(s) - j < sub:
                    continue
                seen.add(cur)
                tmp = backtrack(j)
                if tmp >= 0:
                    sub = max(sub, tmp + 1)
                seen.remove(cur)
            return sub

        return backtrack(0)