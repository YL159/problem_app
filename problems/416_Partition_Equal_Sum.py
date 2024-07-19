'''
LeetCode 416 Partition Equal Subset Sum
memo set record existing sums from all paths
optimize by record those smaller than target
'''
from typing import List

def canPartition(nums: List[int]) -> bool:
	if len(nums) == 1:
		return False
	s = sum(nums)
	if s % 2:
		return False
	# record path sums and check target
	target = s // 2
	memo = set([0, nums[0]])
	for x in nums[1:]:
		tmp = set()
		for y in memo:
			z = x + y
			if z == target:
				return True
			elif z < target:
				tmp.add(z)
		memo = memo.union(tmp)
	return False