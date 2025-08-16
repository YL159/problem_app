'''
Leetcode 808. Soup Servings
A B soup base both have initially n ml soup. In each step randomly choose 1 of 4 operations:
	take 100 ml A and 0 ml B; 75 ml A and 25 ml B
	50 ml A and 50 ml B; 25 ml A and 75 ml B
	to mix, until one or both soups are empty. If less than desired amount, pour all of remaining soup.
Find the probability of A empties earlier than B plus half probability of A & B empties simultaneously.
Accurate under 10^-5 difference than real value

Observation:
1. On average, A is likely pour out more than B in each operations
	=> A will likely depletes earlier than B when n is large
2. A B states are fixed, (n, n), (n-100, n), (n-75, n-25) ... thus result probability depends on 4 prior states' probability
	=> bottom up tabulation to avoid repeated state result calculation
	=> top down using cache is also ok
This is an upgraded fibonacci number problem, with 2D-DP

Since the states are varied by 25 ml difference, we can treat each <= 25 ml as a serving
Method 1, top down recursion
Method 2, bottom up tabulation
Time O(n^2), Space O(n^2)
'''

from functools import lru_cache
import math

class Solution:
    def soupServings(self, n: int) -> float:
        # Method 1
        # top-down recursion has many repeated calculation
        @lru_cache
        def recur(a: int, b: int) -> tuple:
            if a <= 0:
                if b > 0:
                    return (1, 0)
                else:
                    return (0, 1)
            if b <= 0:
                return (0, 0)
            x1, y1 = recur(a-100, b)
            x2, y2 = recur(a-75, b-25)
            x3, y3 = recur(a-50, b-50)
            x4, y4 = recur(a-25, b-75)
            return (0.25*(x1+x2+x3+x4), 0.25*(y1+y2+y3+y4))

        if n >= 4300:
            return 1.
        x, y = recur(n, n)
        return x+y/2
        

    def soupServings(self, n: int) -> float:
		# Method 2
        # bottom-up 2D-DP to remember calculated A-B config
        # experiment on n shows when n >= 4300 the difference between real value and 1 is less than 10^-5
        if n >= 4300:
            return 1.
        lim = 1-10**-5
        serving = math.ceil(n/25) + 1
        dp = [[0]*serving for _ in range(serving)]
        # half probability of a=b=0, 1 * 0.5
        # this 0.5 will carry on for all states that choose to ends at a=b=0
        dp[0][0] = 0.5
        for b in range(1, serving):
            dp[0][b] = 1
        for a in range(1, serving):
            for b in range(1, serving):
                # current state depends on previous 4 states
                dp[a][b] = 0.25 * (dp[max(a-4, 0)][b] + \
                    dp[max(a-3, 0)][b-1] + \
                    dp[max(a-2, 0)][max(b-2, 0)] + \
                    dp[a-1][max(b-3, 0)])
            if dp[a][a] >= lim:
                return 1.
        return dp[-1][-1]
