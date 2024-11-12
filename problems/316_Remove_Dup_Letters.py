'''
Leetcode 316. Remove Duplicate Letters
For a given str of lower case letters, remove duplicated letters
so that each letter appear exactly once, and result str is lexicographically smallest.

For each idx of result, we want to select the smallest letter available.
But global smallest letter may appear after all appearance of some bigger letter, like 'bbbba' => 'ba' not 'ab'

Thus we want to compare each letter's last appearance idx, and choose the smallest idx as right limit,
in order NOT to miss future choices of undecided letters
	=> Use last idx heap to determine the current right limit of str segment of focus

The left limit is the idx of last decided letter => use sorted letter idx list to find idx of decided letter
Among the [left, right] limit, while excluding decided letters, => record decided letters in a set
find the smallest letter, and decide it => greedily decide the left most idx of this letter, its next becomes new left limit

Time O(log26 * (n + logn)) ~ O(n), Space O(n)
'''
import collections, bisect, heapq

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        chars = collections.defaultdict(list)
        for i, c in enumerate(s):
            chars[c].append(i)
        # make a min heap of smallest idx of last appearance of each letter
        c_last = [(chars[c][-1], c) for c in chars]
        heapq.heapify(c_last)
        # have a set of resolved chars
        resolved = set()
        pre = 0
        res = []
        while c_last:
            lim, chara = c_last[0]
            if chara in resolved:
                heapq.heappop(c_last)
                continue
            # choose the smallest char within the allowed window
            choice = min(set(s[pre:lim+1]) - resolved)
            res.append(choice)
            resolved.add(choice)
            idx = bisect.bisect(chars[choice], pre-1)
            pre = chars[choice][idx] + 1
        return ''.join(res)
            
