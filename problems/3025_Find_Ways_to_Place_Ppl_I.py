'''
Leetcode 3025. Find the Number of Ways to Place People I
Given a list of point coordinates on a 2D plane, find the number of point pairs where:
	1 point is top left, the other is bottom right and form a rectangle
	within/on the edge of the rectangle, there is no other points
    rectangle with 0 area is ok, either vertical or horizontal

Intuitively, there are n^2 pairs of points to check, time complexity is at least O(n^2)
Brutal force checking if any other points show on a given rectangle, takes O(n) time

But if we group the points by their x coordinates, raise the criteria of accepting future points
possibly we can skip many future groups of points
e.g. if a=(1, 5) now pairs with b=(2, 2), a future point from group x=3 is p=(3, 1)
	p is at bottom right of a, but its y=1 <= yb=2, thus if p is bottom right, the rectangle will definitely include b
    => future p should have 2 < yp <= 5, and this lower bound 2 will always increase
		=> say for next group x=6, we can at least skip yp <= 2
    => choose only 1 point from each group to match a.
    	If >= 2 points from a group, one point must be on the edge of the other rectangle
Thus we should sort the points by x then by y, and group them by x

Then when traversing each point of some x, we should traverse from larger y to smaller y,
and make the next smaller y as initial lower bound of future p
With this O(1) time verification of each b, we make sure the selected b for each a will form a valid rectangle.

"for i..." and "for t..." loops for all points as top-left point, O(n)
	"for j..." loops for all next groups of points as potential bottom-right point, O(k), k is # of x groups
		bisect find the only point that may match (x, y), O(log(n/k)), n/k is average group size
Worst case Time O(n^2) when k=n/e, Space O(n)
'''

from typing import List
import collections, bisect

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort()
        # for each point, find the 1st point with greater x and smallest y
        # filter next points that has non-smaller x and larger y
        book = collections.defaultdict(list)
        for x, y in points:
            book[x].append(y)
        xs = list(book.keys())
        res, n = 0, len(xs)
        for i in range(n):
            x = xs[i]
            res += len(book[x]) - 1
            # traverse from top to bottom points of fixed x
            for t in range(len(book[x])-1, -1, -1):
                y = book[x][t]
                # next b limit is the next smaller y of this x
                b = book[x][t-1] if t > 0 else float('-inf')
                for j in range(i+1, n):
                    a = xs[j]
                    # find max b <= y for (a, b) points fixing a
                    idx = bisect.bisect(book[a], y) - 1
                    if idx < 0:
                        continue
                    # raise bar b till y
                    if b < book[a][idx] <= y:
                        res += 1
                        b = book[a][idx]
        return res