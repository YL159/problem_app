'''
Leetcode 1547. Minimum Cost to Cut a Stick
Given a stick of length n, and an int list of cutting positions.
For each cut, the cost is the length of the stick portion to be cut.
Find the best order of the cutting positions, to reach min total cost.

Observation:
1. No matter what the cutting order is, each cut will be executed eventually
    => each cut may be the final cut
    => each final cut's cost is fixed, cost = next_cut - prev_cut
    => prune the decision tree leaves
2. Thus build the solution bottom up. Find min cost for each smallest cut
    => combine and find min cost for each pair of neighboring cut
    => combine for each neighboring 3 cuts, etc

So we build a DP table of cuts, DP[i][j] is the min cost making all cuts[i, j]
    => 0 and n as sentinels should be included
Update each smallest cut, and then each pair of cuts, etc
    => top-left to down-right diagonal update, till top-right corner, i.e. DP[0][-1] is result
And we only update top-right portion of the DP matrix

Time O(n^3), Space O(n^2)

There is an advanced Garsia-Wachs algorithm
which provides time O(nlogn) solution for such neighbor-combine cost problems.
'''

from typing import List

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        # bottom up, table record best result for cut[i, j]
        cuts.sort()
        edges = [0, *cuts, n]

        # print(''.join(f'{x:3}' for x in edges))
        # print()

        m = len(edges)
        dp = [[0] * m for _ in range(m)]
        # kth diagonal, left-top to bottom-right
        for k in range(2, m):
            # find best result for portion:
            # start from ith edge, end at jth edge
            for i in range(m-k):
                best = float('inf')
                j = i+k
                # update dp[i][j] takes O(n) time
                for y in range(i+1, j):
                    best = min(best, dp[i][y] + dp[y][j])
                dp[i][j] = best + edges[j] - edges[i]

        # for row in dp:
        #     print(''.join(f'{x:3}' for x in row))

        return dp[0][-1]


if __name__ == "__main__":
    sol = Solution()
    n = 20
    cuts = [1,14,18,6,17,8,10,4,13,16,7]
    sol.minCost(n, cuts)