from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        # init a dict of s, including chars in p
        ref = Counter(p)
        frame = { c:0 for c in set.union(set(s), set(p)) }
        for k in s[:len(p)]:
            frame[k] += 1

        res = []
        # check for initial case, a bit repetitive but avoid an if-clause in main loop
        tmp = True
        for k in ref:
            tmp = tmp and ref[k] == frame[k]
        if tmp:
            res.append(0)

        for i in range(1, len(s) - len(p) + 1):
            # update the frame dict by edge char changes
            frame[s[i-1]] -= 1
            frame[s[i-1+len(p)]] += 1
            # check for a match
            tmp = True
            for k in ref:
                tmp = tmp and ref[k] == frame.get(k, -1)
            if tmp:
                res.append(i)
        return res