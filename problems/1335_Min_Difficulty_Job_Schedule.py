'''
Leetcode 1335. Minimum Difficulty of a Job Schedule
Partition a job list into exactly d non-empty parts/days.
Difficulty of each day is max(difficulty(jobs of a day)).
Find min total difficulty of all d days.

Similar to #813 largest sum of avg, find min difficulty of:
	1st job allocated into 1 day -> all job allocated into 1 day
	=> 2 jobs allocated into 2 days -> all jobs into 2 days
	=>...
	=> d jobs allocated into d days -> n jobs into d days
This time use DP array instead of table, since k day DP array depends only on k-1 day DP array
Time O(dn^2), Space O(n)
'''

from typing import List

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if d > len(jobDifficulty):
            return -1
        # 2d-DP. but since d+1 day schedule depends only on d day schedule
        # use cur/nex dp array is enough

        # base case: partition job[0,i] into k=0 day
        # min schedule dfc of partition job[0,i] into k days
        cur = []
        m = 0
        for job in jobDifficulty:
            m = max(m, job)
            cur.append(m)
        
        # min schedule dfc of partition job[0,i] into k+1 days
        # cur/nex without -1 terms needs careful idx management
        nex = []
        k = 1 # actually day 2
        n = len(jobDifficulty)
        while k < d:
            # update nex dp array based on cur dp
            # i is jobDifficulty idx
            for i in range(k, n):
                opt, m = float('inf'), 0
                # j is jobDifficulty idx idx
                for j in range(i, k-1, -1):
                    # suffix max from job[i] to job[j]
                    m = max(m, jobDifficulty[j])
                    # new optimum come from:
					# taking opt of (assigning job[0,j) into k-1 days and assign job[j,i] to day k)
                    opt = min(opt, cur[j-n-1] + m)
                nex.append(opt)
            cur, nex = nex, []
            k += 1
        
        return cur[-1]