'''
Leetcode 1247. Minimum Swaps to Make Strings Equal
Given 2 equal length string of only 'x' and 'y'
1 operation: swap a char from str1 with some char from str2
Find min # of operations to make them equal, otherwise return -1

As example suggests,
	case 1, 'xx' 'yy' takes 1 op, so as 'yy' 'xx'
	case 2, 'xy' 'yx' takes 2 op, so as 'yx' 'xy'
Thus we can align strings head to toe. Clearly we don't want to disturb already matched indices.
	xxyyxy
	xxxxyx
	xy pair: 1. yx pair: 3
Resolve the mismatch according to base cases. Collect mismatched xy pairs and yx pairs accross 2 strings.
Within xy pairs, each 2 instance can use case 1 solution, using 1 op. So as within yx pairs
If any remaining xy/yx pairs, actually remaining at most 1 for each
	if both remains 1 pair, use case 2 solution, add 2 operations
	otherwise it's not solvable, return -1
'''
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        # each pair of x-y can use 1 step to eliminate, so is y-x
        # remaining x-y and y-x should be both 0 or 1. if 1, taking 2 steps
        xy, yx = 0, 0
        for c1, c2 in zip(s1, s2):
            if c1 == c2:
                continue
            if c1 == 'x':
                xy += 1
            else:
                yx += 1
        res = xy // 2 + yx // 2
        xy %= 2
        yx %= 2
        if xy != yx:
            return -1
        res += 2 * xy
        return res
