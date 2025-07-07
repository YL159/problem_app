'''
Leetcode 1987. Number of Unique Good Subsequences
Given a binary array, find its unique subseq without leading 0, except 0 itself.

Method 1, use idea from #940, but only '1'/'0' chars
For each new char, to obtain new unique subseq:
	append it to recent new subseq from cur char's last appearance and on
Use prefix sum array to represent DP array, and use 0/1 latest position instead of letter-index dictionary
Time O(n), Space O(n)

Method 2, use idea from #115, promote all previous subseqs as current subseqs.
	Prev all unique => currently all unique after appending 0 or 1
	New char is '1' then should preserve additional '1' as new subseq, cus prev '1' was promoted to '10' or '11'
    New char is '0' then just promote all prev subseq, '0' as start is not considered right now.
Time O(n), Space O(1)

For both methods, consider '0' separately.
'''
class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        # # similar to #940
        # # new char only append to recent subseq from last same char and on
        # pref = [0]
        # pos = [-1, -1]
        # has_0 = False
        # for i, c in enumerate(binary):
        #     has_0 |= c == '0'
        #     idx = c == '1'
        #     if pos[idx] < 0:
        #         if idx:
        #             pref.append(1)
        #         elif pos[1] < 0:
        #             pref.append(0)
        #         else:
        #             pref.append(2*pref[-1])
        #     else:
        #         pref.append(2*pref[-1] - pref[pos[idx]])
        #     pos[idx] = i
        #     # print(pref)
        # return (pref[-1] + has_0) % (10**9+7)

        # idea from #115, but each char unconditionally promote all subseq to longer subseq
        end1, end0 = 0, 0
        has0 = False
        mod = 10**9+7
        for c in binary:
            if c == '1':
                # update valid subseq ending 1. +1 is compensate promoted '1'
                end1 = (end1 + end0 + 1) % mod
            else:
                # update valid subseq ending 0.
                end0 = (end1 + end0) % mod
                has0 = True
        return (end1+end0+has0) % mod