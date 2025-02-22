'''
Leetcode 1718. Construct the Lexicographically Largest Valid Sequence
Construct a sequence of # using [1, n] that:
1. 1 used only once, the other # are used twice.
2. distance of two instances of # (idx difference) is #.
Return the lex largest valid seq of #s

DFS on all possible seq starting with largest #. If a path possible, return the result seq.
Each idx has a set of choices, greedily iterate from largest option
'''
from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        # greedy with dfs backtrack
        res = [0]*(2*n-1)
        candidate = set(range(1, n+1))

		# idx: current depth in DFS, used: set of used number in this path
        def backtrack(idx: int, used: set) -> bool:
            while idx < len(res) and res[idx] > 0:
                idx += 1
            if idx == len(res):
                return True
            opts = candidate - used
            while opts:
                nex = max(opts)
                opts.remove(nex)
                used.add(nex)
                # special treatment for 1
                if nex == 1:
                    res[idx] = 1
                    if backtrack(idx+1, used):
                        return True
                    res[idx] = 0
                # treat other opts
                elif idx+nex < len(res) and res[idx + nex] == 0:
                    res[idx] = res[idx+nex] = nex
                    if backtrack(idx+1, used):
                        return True
                    res[idx] = res[idx+nex] = 0
                used.remove(nex)
            return False
        
        backtrack(0, set())
        return res

            