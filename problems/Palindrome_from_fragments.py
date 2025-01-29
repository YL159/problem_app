'''
Proposed question by myself.
Given a list of fragment strings containing only lower English letters.
And each fragment can only be used once.
Find the length of the longest palindrome that can be concatenated from the list.
'''
from typing import List
import random, collections

def longestPalindrome(fragments: List[str]) -> int:
	start = {}
	end = {}
	for i, word in enumerate(fragments):
		cur_start = start
		cur_end = end
		j = 0
		while j < len(word):
			a, z = word[j], word[-j-1]
			if a in cur_start:
				cur_start = cur_start[a]
			else:
				cur_start[a] = {}
			if z in cur_end:
				cur_end = cur_end[z]
			else:
				cur_end = {}
			j += 1
		cur_start[0] = i
		cur_end[0] = i
	pass


if __name__ == '__main__':
	pass
