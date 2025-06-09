'''
Leetcode 386. Lexicographical Numbers
Return an array of integers in range [1, n] in lexicographical order.
Use O(n) time and O(1) space

Lexico order, 10, 11... 19 < 2 < 20, 21... and also 10 < 100, 101... < 11 < 110, 111... < 12
Thus for each current number, we should repeatedly check if appending 0s (mult 10) is within range
before printing its successor integer:
	if within range, recursively deal with appending 0 and 1,2,...
	else print its integer successor
If not considering recursive call stack and return array as extra space, space complexity O(1)
Time O(n), Space O(logn) call stack depth is the dfs tree's height
'''
from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        # recursive dfs
        def dfs(tens: int) -> None:
            for i in range(10):
                cur = tens + i
                if cur <= n:
                    res.append(cur)
                    dfs(cur * 10)

		# initial loop shouldn't start with 0
        # dfs(0*10) is dfs(0), infinite recursion
        for i in range(1, 10):
            if i <= n:
                res.append(i)
                dfs(i * 10)
        return res