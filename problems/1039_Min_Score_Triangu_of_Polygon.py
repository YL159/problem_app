'''
Leetcode 1039. Minimum Score Triangulation of Polygon
Given a list of n vertices of a convex polygon in clock-wise, each with a positive weight.
The ploygon can be divided into n-2 triangles without intersectiong each other, each using 3 of the vertices.
The weight of a triangle is the product of vertices' weight, and the score of polygon is sum of triangles' weights.
Find the min score of the polygon.

1st thought is using dp on vertices[:k] best results and incrementally adding 1 more vertex for vertices[:k+1] results
But the problem is, the new vertex k may or may not match with neighboring vertices
	=> the other 2 vertices separates existing points into max 3 sections
Thus each vertex addition requires recalculation of many existing tables, not operable or efficient

Solution:
As hint suggests, treat the polygon as a whole.
The polygon is triangulated => there is an edge between each neighboring vertices
	=> each contour edge's perspective is the same as the rest's perspective

e.g. For a polygon of 5 sides, vertices tag (0,1,2,3,4,5), ignore their weights
Use edge(5--0) as base edge, for 3rd vertex k of (1,2,3,4), the polygon is separated into 2 parts:
	small polygon (0,1,...k) and polygon (k,k+1,...5)
    use sub queries to get respective best value of these smaller polygons and find current k's score
    and then find best score among all k
Base edge(5--0) makes sure the smaller polygon (k,k+1,...5) has k <= 5 clock-wise increasing property
	otherwise smaller polygon is (k,k+1,...5,0), a bit harder to represent in code.

Use n*n memo table for min results. Only table's upper right half will be used.
Time O(n^3), each cell of the dp table takes O(n) time to iterate all options of 3rd vertex.
Space O(n^2), filling half of the dp table.
'''

from typing import List

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:

        n = len(values)
        # memo[i][j] is the min res of polygon using vertices[i, j], i>=0, j<=n-1
        memo = [[0] * n for _ in range(n)]
        
		# find the result of small polygon using vertices[i, j], i <= j
        def find(i: int, j: int) -> int:
            if memo[i][j] > 0:
                return memo[i][j]
            if i == j or i + 1 == j:
                return 0
            memo[i][j] = float('inf')
            base = values[j]*values[i]
            for v in range(i+1, j):
                memo[i][j] = min(memo[i][j], find(i, v) + find(v, j) + base*values[v])
            return memo[i][j]
        
        return find(0, n-1)