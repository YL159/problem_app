'''
Leetcode 2528. Maximize the Minimum Powered City
Given a list of power plant # of each city.
One city's power can supply itself and all neighbors in r radius with the same units of power.
Now we plan to add k more power plants to some cities, find the max of min total power of these cities.

Directly assigning k power is a hard choice, cus global min power is unknow
Conversely fix this global min power, check if k power can satisfy it
	=> greedily add some power plants to (i+r) city to make ith city get this min power
    => maximize new power plants' effective range
    => line sweep O(n) time and space to check k validity
Then binary search for the max global min power that requires <= k new plants

Time O(nlog(max(power)+k)), Space O(n)
'''

from typing import List

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        # find initial line sweep for each city, left padding r
        line = [0]*(n+r)
        for i, t in enumerate(stations):
            line[i] += t
            idx = i+2*r+1
            if idx < len(line):
                line[i+r*2+1] -= t
        start = sum(line[:r])

		# find how many new plants needed to meet min m power for all stations
        # line sweep O(n)
        def check(m: int) -> int:
            arr = [0]*n
            pref, res = start, 0
            for i in range(n):
                pref += arr[i] + line[i+r]
                if pref >= m:
                    continue
                diff = m - pref
                idx = i+2*r+1
                if idx < n:
                    arr[idx] -= diff
                pref = m
                res += diff
            return res

        # left: definitely possible global min power
        # right: definitely impossible min power if only k new plants
        left = 0
        right = sum(stations) + k + 1
        while left < right-1:
            mid = (left + right)//2
            if check(mid) > k:
                right = mid
            else:
                left = mid
        return left

