'''
Leetcode 1942. The Number of the Smallest Unoccupied Chair
Given enter-leaving time of n people
	each person enter and choose the smallest idx empty chair to sit.
	the person leave at leaving time. Other people entering at the same time can sit the leaving chair if smallest
Find the chair # of target person

We use a heap of chair labels to keep track of the 1st available (smallest) chair for any entering ppl
And flatten the time frame of each pple into [event time, event, ppl] tuples,
	sort the events and process them sequentially
At the same time stamp, process leaving events prior to entering events, push empty chairs into chair heap.
'''
from typing import List
import heapq

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        chairs = [i for i in range(len(times))]
        heapq.heapify(chairs)
        events = []
        sit = {}
        for i, (enter, leave) in enumerate(times):
            events.append((enter, 1, i))
            events.append((leave, -1, i))
        # at time t, leave events are prior to enter events, leaving chairs available
        events.sort()
        for _, e, p in events:
            if e > 0:
                sit[p] = heapq.heappop(chairs)
                if p == targetFriend:
                    return sit[p]
            else:
                heapq.heappush(chairs, sit[p])
        return
