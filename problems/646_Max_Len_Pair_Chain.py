'''
Leetcode 646. Maximum Length of Pair Chain
Given array of pairs. Chain between pair 1&2 forms if end1 < start2.
Find the longest pair

Method 1:
Greedy choice 1: Sort the array by pair ends.
Maintain a monotonic deque of current chain's ends and their chain #. Update chains if a new pair can be added
Thus the deque contains all longest possible chains from the pair array. Return the longest length.
Time O(nlog(n)), space O(n)

Method 2:
Actually there is greedy choice 2: Just keep the 1st chain pairs and its growth.
Because of the array been sorted by ends, all later chains are definitely smaller than the 1st emerged chain.
Time O(nlog(n)), space O(1)

If the problem instead asks the largest range of such chains, the 2nd greedy choice won't work.
And the following code can easily adapt for this task, by recording each chain's current covering range in their tuples.
'''

from typing import List
import collections

class Solution:
    
    # method 2
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda p: p[1])
        end, chain = float('-inf'), 0
        for a, b in pairs:
            if a > end:
                chain += 1
                end = b
        return chain
    
    # # method 1
    # def findLongestChain(self, pairs: List[List[int]]) -> int:
    #     # greedy choice, the smaller pair_end the longer chain
    #     pairs.sort(key=lambda p: p[1])
    #     # the monotonic deque has (pair_end, chain#) with key=end
    #     deck = collections.deque()
    #     for a, b in pairs:
    #         # populate deck if new pair can be a start
    #         if not deck or deck[0][0] >= a:
    #             deck.append((b, 1))
    #             continue
    #         # bottom chains may connect with new pair as new longer chains
    #         while deck[0][0] < a:
    #             _, chain = deck.popleft()
    #             deck.append((b, chain+1))
    #     return max([p[1] for p in deck])