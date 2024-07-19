'''
950. Reveal Cards In Increasing Order
Reveal a card, stash a card at the bottom.
Get the original order of the cards which gives increasing order of cards after such revealing operations.

Simulate the indices or using deque to get the final index order, and then reconstruct the original card order.
'''

from typing import List
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # 1. use deque to simulate the process till empty
        # 2. append to the end of deck index to simulate the process
        n = len(deck)
        res = []
        indices = [i for i in range(n)]
        i = 0
        while i < len(indices):
            if i % 2 == 0:
                res.append(indices[i])
            else:
                indices.append(indices[i])
            i += 1
        origin = sorted(zip(res, sorted(deck)))
        return [y for _, y in origin]