'''
Leetcode 3664. Two-Letter Card Game
Given a deck of cards, each displays 2 lowercase english letter, and a given letter x
Find max # of card pairs to take so that:
	Each card is removed once taken
    Both cards in a pair have letter x, and differ exactly 1 position

Observation: there are xc, xx, cx cases, c != x
	xc/cx can pair with itself as long as c differs
	xx can pair with any of xc or cx, but can't pair with itself
Strategy: pair xc/cx within themselves as many as possible
	=> got some pairs and leftover singles
then each xx can pair with any of those singles for a new pair
and if more xx, relax some previous xc/cx pairs for xx, at a cost of 2 xx breaking each xc/cx pair

Time O(n), Space O(n)
'''

from typing import List

import collections

class Solution:
    def score(self, cards: List[str], x: str) -> int:
        xc = collections.defaultdict(int)
        cx = collections.defaultdict(int)
        xx = 0
        # count xc's c types and cx's c types, and xx #
        for card in cards:
            if card[0] == x and card[1] == x:
                xx += 1
            elif card[0] == x:
                xc[card[1]] += 1
            elif card[1] == x:
                cx[card[0]] += 1
        
        # find (max internal pairs of cx or xc, remaining singles)
        def pair(book: dict) -> tuple:
            pairs = 0
            rem = (0, '')
            record = collections.defaultdict(int)
            # greedily pair each letter with next letter, switch rem with any that left
            for t in book.items():
                t = (t[1], t[0])
                if not rem[0]:
                    rem = t
                    continue
                if rem < t:
                    rem, t = t, rem
                pairs += t[0]
                record[t[1]] += t[0]
                record[rem[1]] += t[0]
                rem = (rem[0]-t[0], rem[1])
            # the remaining singles may still join some existing pairs for more pairs
            # e.g. remaining 3 xa can pair with any x_ that _ != a at a cost of 2 each
            other = pairs - record[rem[1]]
            add = min(other, rem[0]//2)
            return pairs + add, rem[0] - add*2
        
		# process xc and cx types
        xc_p, xc_r = pair(xc)
        cx_p, cx_r = pair(cx)
        # res is initial # of pairs, rem is remaining xc/cx singles
        res = xc_p + cx_p
        rem = xc_r + cx_r
        if not xx:
            return res
        # xx pair with rem singles first
        if rem >= xx:
            return res + xx
        xx -= rem
        # leftover xx join existing pairs at a cost of 2 each
        xp = xx // 2
        return res + rem + min(res, xp)