'''
Leetcode 1696. Jump Game VI
Given an array of points nums, starting at idx 0 and each jump can go right at most k steps.
Collect the points at each stop. Find the max total points.

Observation:
Each index is accessible, thus each index has its own max total points.

Thus we can incrementally find optimum results for each index till the last index -> result.
To reach index i and find opt points/score, score[i] = max(score[i-k:i]) + nums[i]

Method 1: use max heap to record visited indices (score[j], j)
For each index i, from heap pop those scores beyond range [i-k, i]
	=> now heap top will be max(score[i-k:i])
Time O(nlogk), Space O(n)

Method 2: use monotonic decreasing deque and score dp array to record currently available max scores
Deque is a list of increasing indices, where their corresponding score is monotonically decreasing
	=> after popping out-of-range indices from left of queue, max score is dp[queue[0]]
Time O(n), Space O(n)
'''
import collections
import heapq
from typing import List
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # incrementally find max score ending at each index, because each index is reachable
        # time O(nlogk)
        hp = []
        for i, n in enumerate(nums):
            while hp and hp[0][1] < i - k:
                heapq.heappop(hp)
            score = 0
            if hp:
                score = -hp[0][0]
            score += n
            if i == len(nums)-1:
                return score
            heapq.heappush(hp, (-score, i))
        

    def maxResult(self, nums: List[int], k: int) -> int:
        # method 2, monotonic decreasing queue
        # monotonic stack to record largest score in score[i-k:i] at queue[0]
        # leftpop queue to remove out-of-range indices
        # time O(n)
        dp = [0] * len(nums)
        q = collections.deque()
        for i, n in enumerate(nums):
            while q and q[0] < i-k:
                q.popleft()
            max_score = 0
            if q:
                max_score = dp[q[0]]
            dp[i] = n + max_score
            while q and dp[i] > dp[q[-1]]:
                q.pop()
            q.append(i)
        return dp[-1]