'''
Codility problem: Mininum Number of Glasses

Given a series of empty glasses with capacity of 1,2,3,..., N,
Find the minimum number of glasses needed to fill a total volume of K
    if not possible, return -1
Each glass can be used at most once, and either empty or full.

Method 1: Dictionary DP
Maintain a dict of {possible volume: min count of glasses}
Update the dict with each new glass capacity till N
Get target K from dict, if not exist, return -1
Time O(N^3) or O(NK) since viable K ~ O(N^2), Space O(N^2)

Method 2: Greedy choice
Since glasses are "continuous", we can always find a glass with capacity <= K
After subtracting biggest possible glass capacity from K
    => the remaining choices of glasses are again "continuous" with smaller max capacity
    => iterate the process until K is reduced to 0
Thus the min count of glasses is guaranteed. No side effect of greedy choice.
Time O(N), Space O(1)

DP is universal solution for 0-1 knapsack type problems
    => random volume glasses(stones) series

But if each choice poses no side effect on later choices, and local optimal leads to global optimal
    => greedy algorithm is more efficient.
Greedy for continuous or 2-power series glasses(stones) 0-1 knapsack
    => only 1 of each glass, greedy won't work on power of 3 or larger base.
Infinite knapsack => unlimited glasses, greedy can work on any power base.
'''

import collections

class Solution:

    # Method 1: Dictionary DP
    def minNumGlasses(self, N: int, K: int) -> int:
        # dict {possible volume: min count of glasses}
        book = collections.defaultdict(int)
        book[0] = 0
        for glass in range(1, N+1):
            # update dict with new glass capacity
            # avoid updating dict in place
            for k, v in list(book.items()):
                if v + glass > K:
                    break
                book[k + glass] = min(v + 1, book.get(k + glass, float('inf')))
        return book.get(K, -1)
    

    # Method 2: Greedy choice
    def minNumGlasses(self, N: int, K: int) -> int:
        # check if K is feasible
        if N*(N+1)//2 < K:
            return -1

        count = 0
        # subtract K with current largest glass
        # since glasses are "continuous", we can always find a glass with capacity <= K
        while K > 0:
            if K >= N:
                K -= N
                N -= 1
            else:
                K = 0
            count += 1
        return count

if __name__ == "__main__":
    print(Solution().minNumGlasses(4, 10))