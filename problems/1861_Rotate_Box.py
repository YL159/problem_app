'''
Leetcode 1861. Rotating the Box
Find box new configuration when rotate 90 degree clockwise.

Use zip to transpose the matrix.
'''
from typing import List

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        for i in range(m):
            count = 0
            for j in range(n):
                if box[i][j] == '#':
                    count += 1
                    box[i][j] = '.'
                elif box[i][j] == '*' and count:
                    for k in range (1, count+1):
                        box[i][j-k] = '#'
                    count = 0
            if count:
                for k in range (1, count+1):
                    box[i][-k] = '#'
        return [row[::-1] for row in zip(*box)]