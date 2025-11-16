'''
Leetcode 3234. Count the Number of Substrings With Dominant Ones
Given a binary string, find the number of substr that:
	count of 1 >= (count of 0)^2

Brutal force check each subarr with prefix count, takes O(n^2) time.

From hint, check only limited number of preceeding 0s
Suppose subarr s[j,i] has length l, let max x 0s in it
	=> x + x^2 <= l, 0 <= x < sqrt(l)
Thus for each right index, check left max sqrt(l) number of 0s, instead of from beginning

e.g. prefix 111011101011, count all valid subarr ending at last idx
Initially 11 from right are valid (no 0), count is 2
Including 1st 0, consider max reach of 1x 0: 11011
	=> subarr need at least 1 + 1^2 length, currently already 3 (011)
	=> 011, 1011 are all valid, count is 2
Including 2nd 0, max reach of 2x 0: 11101011
	=> subarr need at least 2 + 2^2 = 6 length, currently only 5 (01011)
    => has to count only 101011, 1101011, 11101011, count is 3. 01011 is invalid
Includeing 3rd 0, max reach is whole prefix: 111011101011
	=> subarr need at least 3 + 3^2 = 12 length, currently only 9 (011101011)
    => start from length 12, only 111011101011, count is 1
Thus ending at this last idx, the total valid count = 2+2+3+1 = 8

Time O(nsqrt(n)), Space O(n) for storing each 0's idx
'''

import math

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # # TLE
        # # prefix count and n^2 check for each subarr
        # # prefix subarr, count of 0 and 1
        # r0, r1 = 0, 0
        # res = 0
        # for i in range(len(s)):
        #     r0 += s[i] == '0'
        #     r1 += s[i] == '1'
        #     l0, l1 = 0, 0
        #     for j in range(i+1):
        #         if r1 - l1 >= (r0 - l0)**2:
        #             res += 1
        #         l0 += s[j] == '0'
        #         l1 += s[j] == '1'
        # return res

        zeros = []
        res = 0
        for i in range(len(s)):
            if s[i] == '0':
                zeros.append(i)
            target = math.floor(math.sqrt(i+1))
            zero = 0
            n = len(zeros)
            # count any immediate 1's subarr to the left
            res += i - (zeros[-1] if zeros else -1)
            for idx in range(n-1, max(n-1-target, -1), -1):
                zero += 1
                # lim is the max reachable idx to the left of current 0
                lim = zeros[idx-1] if idx > 0 else -1
                # length from i to left
                # at least zero^2+zero or till this zero (more 1s than needed)
                length = max(zero*zero+zero, i-zeros[idx]+1)
                res += max(i-length+1-lim, 0)
        return res
