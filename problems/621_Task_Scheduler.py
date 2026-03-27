'''
Leetcode 621. Task Scheduler
Given a list of tasks represented by cap letters, and int n.
Each task executes within 1 second.
Each type of tasks with cool down time at least n seconds
Find min total time to execute all tasks

Observations:
1. The most frequent tasks determine the back bone of final schedule
2. Need to find a way to represent cool down
    => use timed queue to buffer cool down tasks

Method 1, use max heap + queue find next available task
Get the most frequent task from max heap and asign for current time block
Then append it to a queue (queue order represents available time order) waiting for next heap call
Time O(nlog26) ~ O(n), Space O(n)

Method 2, plan the most frequent tasks ahead
Arrange the most frequent task as head of each (n+1) block
    => fill the empty blocks with other less frequent tasks
    => the last (n+1) row may not be fully filled, and only the same most frequent tasks can reach
What if there are many tasks with the same max frequency?
    => each (n+1) row can expand larger, all these tasks will fill in and no space needed for each row
    => time is length of tasks
Find max of two arrangement, because there may be idle blocks.
Time O(n), Space O(n)
'''

from typing import List

import collections, heapq

class Solution:
    # Method 1, heap + que find next available task
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # max heap for current most frequent tasks
        # que the cool down tasks and its next available time
        book = collections.Counter(tasks)
        hp = [-v for v in book.values()]
        # max heap of task freq
        heapq.heapify(hp)
        # que of (-freq, next_avail_time)
        que = collections.deque()

        t = 0
        while hp or que:
            while que and que[0][1] <= t:
                heapq.heappush(hp, que.popleft()[0])
            if hp:
                freq = heapq.heappop(hp) + 1
                if freq != 0:
                    que.append((freq, t+n+1))
            t += 1
        return t
    

    # Method 2, deterministic greedy planning
    def leastInterval(self, tasks: List[str], n: int) -> int:
        book = collections.Counter(tasks)
        maxi = max(book.values())
        maxi_count = collections.Counter(book.values())[maxi]
        return max((maxi-1)*(n+1)+maxi_count, len(tasks))
