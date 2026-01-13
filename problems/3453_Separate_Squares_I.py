'''
Leetcode 3453. Separate Squares I
Given a list of squares (x_bottom_left, y_bl, length), all parallel to x-axis
Find a line y that separates these squares with equal above-below areas.
Overlapped squares can count multiple times.

Observation:
Overlapped areas are counted in full, and its above-below area is solely dependent on relationship with line y
    => x positions don't matter, all squares are independent

Method 1: binary search for this line y, check all squares and see if above-below areas are equal
Time O(nlog(y)), y is range of squares' y coordinates, Space O(1)

Method 2: compress sqaures and line sweep
Since x coordinates don't matter, we use y axis as time line
    => y line sweep each square: 2 events [start, weight] and [end, -weight] using [y, l], [y+l, -l]
Sort "events" by "time", accumulate and find time y so that left & right same weight sum
Time O(nlogn), Space O(n)
'''

import collections

from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        book = collections.defaultdict(int)
        total = 0
        # line sweep on event weights (side length l)
        for x, y, l in squares:
            w = l*l
            book[y] += l
            book[y+l] -= l
            total += l*l

        events = sorted(book.items())
        target = total / 2
        # yi >= 0, thus t can start with 0
        t, weight, i = 0, 0, 0
        while target > 0:
            te, w = events[i]
            grow = weight * (te - t)
            if grow >= target:
                return target / weight + t
            target -= grow
            weight += w
            t = te
            i += 1
