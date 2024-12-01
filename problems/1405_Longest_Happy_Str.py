'''
Leetcode 1405. Longest Happy String
Construct a longest string from at most [a, b, c] of letter 'abc', with no sustr of 'aaa', 'bbb', 'ccc'

Similar to CPU task schedule, make a priority queue of available count of each letter.
Greedily append 1-2 of the letter with most count:
	If result empty OR heap top letter different from prev appended letter:
		Append at most 2, and enque if remain any count. Greedy
	If top letter the same as prev appended letter:
		Prev only appended 1 of it, now we can greedily append 1 more without breaking the law.
			Combine them as 2 letters in result for future check
		Prev appended 2 of it, we should get another available letter, greedily append only 1 of it.

Time O(nlog(3)) => O(n)
'''
import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []
        hp = [x for x in zip([-a, -b, -c], 'abc') if x[0] != 0]
        heapq.heapify(hp)
        while hp:
            x, ch = heapq.heappop(hp)
            x = -x
            if not res or ch != res[-1][0]:
                res.append(ch*min(x, 2))
                x -= min(x, 2)
                if x:
                    heapq.heappush(hp, (-x, ch))
                continue
            # now ch the same as last append char
            if len(res[-1]) == 1:
                # append only 1, combine the same chars for future check
                res[-1] = ch*2
                if x > 1:
                    heapq.heappush(hp, (-x+1, ch))
                continue
            # prev append 2 chr, now should change to another char
            if not hp:
                break
            y, ch1 = heapq.heappop(hp)
            y = -y
            res.append(ch1)
            if y > 1:
                heapq.heappush(hp, (-y+1, ch1))
            heapq.heappush(hp, (-x, ch))
        return ''.join(res)
                