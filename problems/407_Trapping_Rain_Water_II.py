'''
Leetcode 407. Trapping Rain Water II
Given a 2d map of non-negative heights, find total units of water it can trap.


1st thought, reuse #42 trapping rain water 1
For each cell, collect its row's left/right max and col's up/down max
Won't Work! Because whether a cell can hold water is not only determined by its row and col
but also its "swamp" edge wall heights

Thus we should focus on a local "swamp" structure, especially the "shortest board" of the "swamp bucket"
	=> use min heap to find the shortest board of the swamp edges
    => initial "swamp" is the whole map
Then dfs/bfs on each smallest swamp edge cell's unvisited neighbors
	1. new cell height <= current smallest swamp edge h0, it will definitely hold water to h0 level
		because all other swamp edge cells are higher than this h0, the new cell must be inside such a "bucket"
    2. new cell height > h0, push it to min heap
		because it can be an edge cell of this/other swamp
Now all cells are decided, either holding water, or as a swamp edge cell that doesn't hold water

Time O(mnlog(mn)), Space O(mn)
'''

from typing import List

import heapq, collections

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:

        m, n = len(heightMap), len(heightMap[0])
        if m <= 2 or n <= 2:
            return 0
        visited = [[0] * n for _ in range(m)]

        # min heap of swamp edge cells (h, i, j)
        # initially all edge cells of the map
        hp = []
        for i in [0, m-1]:
            for j in range(n):
                visited[i][j] = 1
                hp.append((heightMap[i][j], i, j))
        for j in [0, n-1]:
            for i in range(1, m-1):
                visited[i][j] = 1
                hp.append((heightMap[i][j], i, j))
        heapq.heapify(hp)

        # pop the smallest swamp edge, update the heap with new edges
        # collect water while bfs
        res = 0
        while hp:
            h0, i, j = heapq.heappop(hp)
            que = collections.deque()
            que.append((i, j))
            while que:
                x, y = que.popleft()
                for a, b in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    if 0 <= a < m and 0 <= b < n and not visited[a][b]:
                        visited[a][b] = 1
                        # decide each unvisited cell by height
                        if heightMap[a][b] <= h0:
                            res += h0 - heightMap[a][b]
                            que.append((a, b))
                        else:
                            heapq.heappush(hp, (heightMap[a][b], a, b))
        return res