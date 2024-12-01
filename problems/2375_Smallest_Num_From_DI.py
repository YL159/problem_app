'''
Leetcode 2375. Construct Smallest Number From DI String
Given a string of D/I, indicating target string's neighboring number decreasing/increasing.
Find the smallest result string. Each number 1-9 is used only once.

Result is lexicographically/numerically smallest
	=> max num = len(pattern)
	=> start with smallest possible choices (greedy)
len(pattern) + 1 = len(result)

If we align pattern with result as:
	D I D D I D D D
    2 1 5 4 3 9 8 7 6
	  *     *       *
idx with * are our 'current' smallest choices AFTER considering precedding group of Ds
Thus we look ahead for the length of each D group, and preprocess these groups

Time O(n), space O(n), n <= 9
'''
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        cur = 1
        ds = 0
        res = []
        i = 0
        while i < len(pattern):
            # I always append current smallest, consider last length of Ds as well
            if pattern[i] == 'I':
                res.append(cur)
                cur += ds + 1
                ds = 0
                i += 1
            # for D groups, check group length and start with min num > cur
            else:
                while i < len(pattern) and pattern[i] == 'D':
                    ds += 1
                    i += 1
                for j in range(ds):
                    res.append(cur + ds - j)
        res.append(cur)
        return ''.join(str(x) for x in res)
