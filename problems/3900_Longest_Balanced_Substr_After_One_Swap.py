'''
Leetcode 3900. Longest Balanced Substring After One Swap
Given a string s of only 0 and 1. A substr is balanced if count of 1 = count of 0
Can perform max one swap between any 2 chars of s
Find the longest balanced substr of s

Observation:
If no swap allowed, the same as finding longest balanced 1-0 substr
    => prefix 1_count - 0_count as key, first appearing idx as value
    => check if later such difference reappear, and update recorded length

If swap within substr, count of 0-1 won't change
should swap from outside substr window
  => pre-compute if there are 0/1 before or after some idx

Hash 1-0 count for each idx. for later 1-0 count, check equal or +-2 is in dict
if +-2 show up in dict:
    => check if can swap from behind idx
    => then check if can swap before 1st start idx, or swap before 2nd start idx
    => since there must be equal non-zero count of 1/0 between 1st and 2nd start idx
        we only check max 2 such start idx

Time O(n), Space O(n)
'''
import collections

class Solution:
    def longestBalanced(self, s: str) -> int:
        ones = s.count('1')
        # one_zero[i]: (1 count before/include i, 1 count after i)
        one_zero = [(0, ones)]
        for i in range(len(s)):
            a, b = one_zero[-1]
            if s[i] == '1':
                a += 1
                b -= 1
            one_zero.append((a, b))
        
        book = collections.defaultdict(list)
        book[0] = [-1]
        res = 0
        for i in range(len(s)):
            diff = 2*one_zero[i+1][0]-i-1
            # if no swap, check distance with farthest same 1-0 count idx
            if diff in book:
                res = max(res, i-book[diff][0])
            
            # if swap, check distance with help of one_zero arr
            for d in (diff-2, diff+2):
                if d not in book:
                    continue
                # 1 is two-more than 0 in substr, swap 1 with outer 0 makes them even
                swap_one = d == diff-2
                if res >= i-book[d][0]: # short circuit
                    continue
                
                # 1st check if tail swappable
                tail_1 = one_zero[i+1][1]
                tail_0 = len(s) - i-1 - tail_1
                if swap_one and tail_0 or not swap_one and tail_1:
                    res = max(res, i-book[d][0])
                    continue
                
                # 2nd check head swappable, max iterate first 2 instances
                # if 1st start no available swappable, the 2nd must be
                left = book[d][0]
                head_1 = one_zero[left+1][0]
                head_0 = left+1 - head_1
                if swap_one and head_0 or not swap_one and head_1:
                    res = max(res, i-left)
                elif len(book[d]) == 2:
                    res= max(res, i-book[d][1])
            
            # only the first 2 positions matters
            if len(book[diff]) < 2:
                book[diff].append(i)
        
        return res
