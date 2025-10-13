'''
Leetcode 778. Swim in Rising Water
In a grid of n*n of non-negative heights, at time t the water level is at t units
Any cell height <= t is in water and accessible
A person can swim from top-left to bottom-right cell in no time, but only swim in accessible adjacent cells
Find the min time that the person can reach bottom-right cell

Translation: find a path from top-left to bottom right that max(path_cell) is minimum
And the path's detail is not important

Method 1, sort all cells and check min water level
Imagine the water level is rising up as time increases, the accessible cells for swimmer are increasing
Until the accessible "pond" the swimmer in is reaching the ending cell.
We don't have to simulate the water level rising as is, and check accessibility at each level
since the cells' heights are limited
	=> water at low level -> inaccessible, and when level is high enough -> definitely accessible
    => binary search for this "min high enough" water level
Thus sort all elevations and binary search for min max cell, O(mnlog(mn))
Inner O(mn) BFS validate if a path of this elevation exist from top-left to bottom-right
Time O(mnlog(mn)), Space O(mn)


Method 2, heap all cells and crawl on current smallest
It seems greedily following the smallest neighbor of current cell and "crawl" to the end is viable
	=> easy to make an example that this greedy choice is not globally optimal
Change this local greedy method into more or less global "greedy"
	=> heap the smallest neighbor of visited cells
Thus we only visit the currently smallest next available cell, to make sure the max cell visited is minimized
and record max cell visited so far till visiting end cell
Same Time O(mnlog(mn)), Space O(mn)
'''

from typing import List

import heapq

class Solution:
	# method 1, binary search min water level by checking accessibility
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return grid[0][0]
        
        visited = [[0]*n for _ in range(n)]
        # dfs visit check
        def check(t: int) -> bool:
            if t < grid[0][0] or t < grid[-1][-1]:
                return False
            # reset visited map
            for i in range(n):
                for j in range(n):
                    visited[i][j] = 0
            # bfs check if there is a path from start to end
            end = (n-1, n-1)
            cur = {(0, 0)}
            while cur:
                nex = set()
                for i, j in cur:
                    visited[i][j] = 1
                    for x, y in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
                        if 0 <= x < n and 0 <= y < n and not visited[x][y] and grid[x][y] <= t:
                            nex.add((x, y))
                if end in nex:
                    return True
                cur, nex = nex, set()
            return False
        
        values = set()
        for row in grid:
            values.update(row)
        values = sorted(values)
        l, r = 0, len(values)
        while l < r-1:
            mid = (l+r)//2
            if check(values[mid]):
                r = mid
            else:
                l = mid
        return values[r]



	# method 2, heap accessible cell's neighbors
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return grid[0][0]

        visited = [[0]*n for _ in range(n)]
        hp = [(grid[0][0], 0, 0)]
        visited[0][0] = 1
        res = 0
        while hp:
            h, i, j = heapq.heappop(hp)
            res = max(res, h)
            # when visiting ending cell, heap makes sure only the necessary larger cells were visited if any
            if i == n-1 and j == n-1:
                return res
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < n and 0 <= y < n and not visited[x][y]:
                    visited[x][y] = 1
                    heapq.heappush(hp, (grid[x][y], x, y))