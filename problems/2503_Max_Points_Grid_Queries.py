'''
Leetcode 2503. Maximum Number of Points From Grid Queries
Give a grid of ints >= 1, for each query q:
	from top-left cell, find max neighboring cells < q

Method 1. brutal force bfs on each query, O(qmn)

Method 2. preprocess grid with min heap, O(mnlog(mn)+qlog(mn)) or O(mnlog(mn)+qlogq+mn)
grid bfs expansion: for each smallest border height, expand visitable cells->points
	binary search query on height array, return corresponding points
	or sort the queries, mn time find all query results

3. sort queries, heap bondary bfs once on grid, O(qlogq+mnlog(mn))
improve from 2, directly find result for each query from small to large in 1 bfs traverse
also need min heap to skip larger cells
'''
from typing import List
import heapq

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        q_list = sorted((q, i) for i, q in enumerate(queries))
        m, n = len(grid), len(grid[0])
        res = [0]*len(queries)
        # min heap of border cells
        border = [(grid[0][0], 0, 0)]
        # (0, 0) already in border heap, mark as 0
        grid[0][0] = 0
        points = 0
        for q, i in q_list:
            while border and border[0][0] < q:
                _, x, y = heapq.heappop(border)
                points += 1
                for a, b in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                    if 0 <= a < m and 0 <= b < n and grid[a][b] != 0:
                        heapq.heappush(border, (grid[a][b], a, b))
                        # mark all visited cells 0, including border cells
                        grid[a][b] = 0
            res[i] = points
        return res