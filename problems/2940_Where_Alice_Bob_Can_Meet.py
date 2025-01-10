'''
Leetcode 2940. Find Building Where Alice and Bob Can Meet
Given a list of building heights > 0, Alice at building idx a, Bob at b.
They want to meet at some building. If anyone go to some building idx t:
	t > current idx AND heights[t] > heights[cur idx]
i.e. they should meet at some higher building to their right or at someone's building.
For each query, Alice at q[0], Bob at q[1], find min idx of their meeting building.
If no building options, give -1

We can observe that if their idx are the same OR larger idx has higher building:
	return the larger idx directly
For larger idx with same or smaller building, we want to find the right nearest building higher than both.
=> suggests building increasing monotonic stack for each query
=> precompute stack for each idx, taking O(n^2). Each query O(log(n)) for binary search.

As hint suggests, we can work out the stack from right to left, while serving the 'correct' queries.
Sort the queries by larger height idx, O(qlog(q)).
Examine each query while maintaining the stack to the proper state for query. O(qlog(n))
	thus avoid O(n^2) stack construction for each idx

Time O(q(log(q)+log(n))), space O(q+n)
'''
from typing import List
import collections, bisect

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = len(queries)
        # backward decreasing monotonic stack, forward increasing monotonic stack
        q = collections.deque()
        work_idx = len(heights) - 1
        res = [0] * n
        # work with sorted queries while building mon stack
        qs = []
        for i, (a, b) in enumerate(queries):
            if a > b:
                a, b = b, a
            qs.append((a, b, i))
        qs.sort(key=lambda qr: qr[1], reverse=True)
        
        for a, b, i in qs:
            if a == b or heights[b] > heights[a]:
                res[i] = b
                continue
            # now a < b and h[b] <= h[a], find t > b and h[t] > h[a]
            # maintain mon stack till b+1 position
            while work_idx > b:
                while q and heights[work_idx] >= q[0][0]:
                    q.popleft()
                q.appendleft((heights[work_idx], work_idx))
                work_idx -= 1
            t = bisect.bisect(q, (heights[a], n))
            if t == len(q):
                res[i] = -1
            else:
                res[i] = q[t][1]
        return res