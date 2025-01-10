'''
Hackerrank, Minimum street lights
Given an arr of street light loc[] of length n. The street cover [1, n] range.
Each light covers [(max(i-loc[i]), 1), min(i+loc[i], n)] range. All lights are off initially
Find min # of lights to turn on, in order to cover the whole street.

First transform the array into intervals of lights as [start, end].
And greedily record max end for the same starts, help with reduce # of lights

Starts with smallest interval start, find the next interval that links with this interval and reach farthest to the right
If there is any break, return -1 meaning no solution.
Remember to consolidate the last potential choice.
Time O(nlog(n)), space (O(n))
'''
from typing import List

def minStreetLights(locations: List[int]) -> int:
	n = len(locations)
	# intervals store greatest right end coverage of certain left start of a light
	intervals = {}
	for i, loc in enumerate(locations):
		l, r = max(i+1-loc, 1), min(i+1+loc, n)
		intervals[l] = max(intervals.get(l, 0), r)
	count = 0
	end = new_end = 1
	for start in sorted(intervals.keys()):
		# find greated potential new end if current interval links previous one
		if start <= end:
			new_end = max(new_end, intervals[start])
		# consolidate recorded greate potential only when new interval also links with it
		elif start <= new_end:
			end, new_end = new_end, intervals[start]
			count += 1
			# current end covers n, early exit
			if end == n:
				return count
		# can't cover street head or middle
		else:
			return -1
	# can't cover street end
	if new_end < n:
		return -1
	# the last interval covers n
	return count + 1

if __name__ == '__main__':
	arrs = [
		[2,4,2,1,1,1,3,1,0],
		[0,0,0,2,1,1,1,0],
		[1,1,0,0,0,1,2]
	]
	for arr in arrs:
		print(minStreetLights(arr))