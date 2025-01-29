'''
Leetcode 32. Longest Valid Parentheses
Given a string of only '(' and ')', find the length of longest well-formed parentheses subarr.

Still use stack to match ( and ). But here we need length of valid substr:
	Save idx instead of '(' chars in stack.
    Also keeps unmatched/excessive ')' idx to distinguish valid () starting at different position.
'''
import collections

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        # record the current length of valid () starting at key+1 idx.
        record = collections.defaultdict(int)
        res = 0
        for i, c in enumerate(s):
            # append ( idx, or any ) that can't match
            if c == '(' or stack[-1] == -1 or s[stack[-1]] == ')':
                stack.append(i)
                continue
			# if there is a match, add the length to recorded length
            # thus parallel ()s will return to the same prev idx, each length is added
            # different valid () will be marked by different prev idx.
            cur = i - stack.pop() + 1
            record[stack[-1]] += cur
            res = max(res, record[stack[-1]])
        return res
