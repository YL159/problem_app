'''
Leetcode 983. Minimum Cost For Tickets
Find the min total cost of ticket purchasing strategies, to cover all dates to travel

Incremental:
	for each new date:
		keep all the candidates that covers the new date
		select the min cost of those strategies where pass is over (selection tree trimming)
			if some passes are over, add all 3 cost options to buy a new pass
'''

from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # for each new date, keeps all those previous costs that cover today
        # those can't cover today, keep only the min cost (buy new ticket anyways)
        avail = [(costs[0], days[0]), (costs[1], days[0]+6), (costs[2], days[0]+29)]
        for day in days[1:]:
            _avail, over = [], []
            cur_min = 0
            # filter for over-pass & in-pass scenarios
            for cost, till in avail:
                if till < day:
                    over.append(cost)
                else:
                    _avail.append((cost, till))
            if over:
                cur_min = min(over)
                _avail.append((cur_min + costs[0], day))
                _avail.append((cur_min + costs[1], day + 6))
                _avail.append((cur_min + costs[2], day + 29))
            avail = _avail
        return min([c for c, _ in avail])
    