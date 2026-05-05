'''
Leetcode 1871. Jump Game VII
Given a binary str, start from str[0] = '0':
    jump right in (i + minJump, i + maxJump) range
    jump to only '0' block
Find if possible to jump to str[-1]

Similar to staircase jump problem, dp on each step's reachable true/false

Method 1, double loop on each block and jump range
time O(n*jump_dist), not efficient enough

Method 2, sliding window update edge status
use prefix sum or tracking reachable T count to optimize inner loop
Also use deque to only keep window's reachability

Time O(n), Space O(jump_dist)
'''

import collections

class Solution:

    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # Method 2, dp + sliding window + deque
        if s[-1] == '1':
            return False
        reach = collections.deque([False] * (minJump-1))
        reach.appendleft(True)
        t = 1
        for j in range(minJump, len(s)):
            # update latest block reachability
            if s[j] == '0':
                reach.append(t > 0)
            else:
                reach.append(False)
            # then update window True count
            t += reach[-minJump]
            if j >= maxJump:
                t -= reach[-maxJump-1]
                reach.popleft()
        return reach[-1]
