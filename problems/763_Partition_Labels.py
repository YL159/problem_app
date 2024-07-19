'''
Leetcode 763. Partition Labels
Partition string into max # of groups that each letter only appear in 1 group
Find the smallest window that enclosure all appearances of the letters inside
'''

from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # find the first & last position of each letter, in letter appearing order
        book = {}
        for i, letter in enumerate(s):
            if letter not in book:
                book[letter] = [i, i]
            else:
                book[letter][1] = i
        res = []
        data = list(book.values())
        start, stop = data[0]
        for start1, stop1 in data:
            if stop >= start1:
                stop = max(stop1, stop)
            else:
                res.append(stop - start + 1)
                start, stop = start1, stop1
        res.append(stop - start + 1)
        return res