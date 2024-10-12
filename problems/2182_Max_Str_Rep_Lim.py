'''
Leetcode 2182. Construct String With Repeat Limit
Rearranging chars in s such that each char repeat in a row less than given limit.
And find lexicographically biggest new str

Use heap to retrieve currently largest char and its remaining count.
If exhaust the count, this char won't come back, and deal with next biggest in line.
Else, repeat this biggest char lim times, and append 1x next char (check if next char is exhausted)
Update their count
'''
import collections, heapq
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        a = ord('a')
        book = collections.Counter(s)
        # make a heap of tuple (-ascii, char, freq)
        hp = [(a-ord(c), c, v) for c, v in book.items()]
        heapq.heapify(hp)
        res = []
        while hp:
            # repeat current biggest char
            n, c, count = heapq.heappop(hp)
            if count <= repeatLimit:
                res.append(c*count)
                continue
            res.append(c*repeatLimit)
            if not hp:
                break
            # biggest char not exhausted, insert 1x 2nd biggest char
            n1, c1, count1 = heapq.heappop(hp)
            res.append(c1)
            if count1 > 1:
                heapq.heappush(hp, (n1, c1, count1-1))
            heapq.heappush(hp, (n, c, count-repeatLimit))

        return ''.join(res)