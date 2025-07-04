'''
Leetcode 1353. Maximum Number of Events That Can Be Attended
Given a list of events with [start, end] day number
Each day can only attend 1 event that has end >= current day
Find max number of events to attend

For each day, we should attend 1 event if there is any available
If multiple events ends at current day, can only attend 1 and discard other same-day ending events
	=> greedily attend the available event that ends earliest
	=> use min heap to find out such event, increment day count, pop invalid events

Time O(nlogn), Space O(n)
'''
import collections, heapq
from typing import List

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        ebook = collections.defaultdict(list)
        max_end = 0
        for a, b in events:
            ebook[a].append(b)
            max_end = max(max_end, b)
        # append a fake event with start > all start
        # accommodate tail events processing
        ebook[max_end + 1] = [1]
        hp = []
        day = 1
        res = 0
        for start in sorted(ebook.keys()):
            # before new start day
            # each day can take a valid event that ends >= day
            while hp and start > day:
                if hp[0] >= day:
                    res += 1
                    day += 1
                heapq.heappop(hp)
            # day < start means no available events to take, shift day to cur start
            if day < start:
                day = start
            # push new event ends to heap for future processing
            for end in ebook[start]:
                heapq.heappush(hp, end)
        return res