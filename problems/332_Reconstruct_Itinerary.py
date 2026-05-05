'''
Leetcode 332. Reconstruct Itinerary
Given a list of flight tickets, ticket[i] = [from_i, to_i]
The tickets can form a valid itinerary start from "JFK", with each ticket used once.
find an itinerary as a list of city to travel, and of min lexico order.

Observation:
Since the tickets guarangee forming a valid itinerary from "JFK"
according to Eulerian path theorem:
    "JFK" out degree - in degree is either 1 or 0
        if it is 1: another city has 1 more in-degree, and path ends at it
        if 0: all city has equal in/out degree, and path ends at "JFK"

Method 1, BFS find out-in edge of "JFK"
BFS/DFS find if "JFK" has more out-degree than in-degree.
    => first traverse other returnable out-degree by lexico order
    => then traverse the last out-degree
If equal in/out degree, just traverse out-degree by lexico order
Implementation heavy, not recommended.

Method 2, sort tickets and DFS post-order
Further from method 1 without global in/out detection, inspired by solution
Use call stack as DFS stack. But how to maintain traverse status of each city?
    => use neighbor city stack, pop operation changes city connectivity even in different call stack
    => smallest neighbor city at stack top in order to pop first
    => sort tickets in reverse order and collect
Record the city if DFS exhaust all its out-degrees, thus it must be the end of path
Return the path in reverse order

Time O(nlogn), Space O(n)
'''

from typing import List

import collections

class Solution:
    # Method 2, recursive DFS and neighbor stack
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # sort in reverse so small lexico city is at the end of neighbor list
        # i.e. top of neighbor stack
        tickets.sort(reverse=True)
        book = collections.defaultdict(list)
        for a, b in tickets:
            book[a].append(b)
        
        path = []
        # dfs traverse neighbor of start city
        def dfs(start: str) -> None:
            while book[start]:
                # from smallest (stack top)
                # stack pop changes city's neighbor list
                # thus each call stack "knows" city neighbor current visit status
                dfs(book[start].pop())
            # post-order traverse
            # visit start city only when it is the "wrap up" of future visits
            path.append(start)
        
        dfs("JFK")
        # every city in path is a "wrap up"
        # thus reverse the path to get real travel path
        return path[::-1]