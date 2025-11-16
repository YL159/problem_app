'''
Leetcode 3228. Maximum Number of Operations to Move Ones to the End
Given a binary string, within 1 operation:
	choose a '1' that is left neighbor of a '0', and shift it to left of next '1', or end of the str
Find the max # of operations possible.

Method 1, for each grouped 1s, move right-most 1 to right
1011001 -2> 0_110011 -1> 0_100111 -1> 000_1111, 4 op
Looks like shifting str to left. Shift one group of 1s takes rem_group_count * cur_group_size
10011101, exclude the last group of 1s
1st group, 2 * 1 op to disapear,
2nd group, 1 * 3 op to disapear. Total 5 op
Time O(n), Space O(1)

Method 2, from left, push each 1 to right, from solutions
Lazy push each 1 to right, gradually merging groups together
At the end of a '1' group, should one by one push they to the next group, op += # of '1' in current group
Time O(n), Space O(1)
'''

class Solution:
    # method 1
    def maxOperations(self, s: str) -> int:
        res = 0
        # groups of 1 from cur to end
        groups = 0
        # count of 1 in a group
        count = 0
        # exclude the immovable group of 1 at the end
        if s[-1] == '1':
            groups -= 1
        prev = '0'
        for i in range(len(s)-1, -1, -1):
            if s[i] == '1':
                if s[i] != prev:
                    groups += 1
                count += 1
            elif s[i] != prev:
                res += groups * count
                count = 0
            prev = s[i]
        # left padding by 0 if no 0
        if s[0] == '1':
            res += groups * count
        return res
    
	# method 2
    def maxOperations(self, s: str) -> int:
        total = 0
        ones = 0
        for i in range(len(s) - 1):
            # accumulated count of '1' in current group
            if s[i] == "1":
                ones += 1
				# now have to push one by one to next group, thus op += ones
                if s[i+1] == "0":
                    total += ones

        return total