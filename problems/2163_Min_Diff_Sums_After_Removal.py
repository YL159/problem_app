'''
Leetcode 2163. Minimum Difference in Sums After Removal of Elements
Given a num list of 3n length, remove n #
partition remaining 2n # into 2 parts of n #, find the min value of sum(part1) - sum(part2)

Observation:
There are 2^n ways to remove n numbers, finding parts' difference takes O(n) time
	=> brutal force time O(n2^n)
The cut will always take place in gaps of nums[n:2n], including gap before head.
	=> decide the cut, O(n). Then optimally remove excessive # in 2 parts
    => remove k max # from part1, and remove n-k min # from part2, thus to get the min diff value of current cut

Incrementally use outer loop of n to assign 1 middle # from part2 to part1
Use heap to decide popping largest # in part1 after taking new #, maintain sum(part1)
But using heap to maintain part2 is difficult:
	the leaving middle # may participate in sum(part2)
    the leaving middle # is not necessarily the min or max in the heap, removing it and re-heap is hard
=> use incremental heap from right to left for part2, and then reverse the result

Time O(nlogn), Space O(n)
'''

import heapq
from typing import List

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3

        # divide nums into n+k and 2n-k parts
        # if 1 pass adding middle element to 1st part is easy
        # but dealing with removing that element from 2nd part is hard
        # thus taking 2 pass, but for 2nd part reverse the deletion into addition
        
        # default finding largest n+1 sums within arr + increment, using min heap popping min #
        def incrementalAdd(arr: List[int], increment: List[int]) -> List[int]:
            s = sum(arr)
            heapq.heapify(arr)
            s_arr = [s]
            for x in increment:
				# x > min, definitely go into sum, thus pop before push
                if x > arr[0]:
                    s += x - heapq.heapreplace(arr, x)
                # or use heapq.heappushpop(arr, x), push before pop
                s_arr.append(s)
            return s_arr

        # find max optimum sum array for 2nd part
        # incremental middle n # is reversed for addition, thus result arr is also reversed
        s2 = incrementalAdd(nums[2*n:], nums[n:2*n][::-1])[::-1]

        # find min optimum sum array for 1st part
        # negative values to adapt min heap
        tmp = incrementalAdd([-x for x in nums[:n]], [-x for x in nums[n:2*n]])
        s1 = [-x for x in tmp]

        return min(a - b for a, b in zip(s1, s2))