'''
Leetcode 1458. Max Dot Product of Two Subsequences
Given int array nums1 and nums2, respectively select subsequences of the same length, and get their dot product
Find the max dot product.

Since the selected subseqs can start at any position in both array, the time complexity is at least O(mn).
Thus consider using 2D table to track some best result of all possible suffix combinations of two arrays

Method 1, 2D table best result DP[i][j] is: subseq starting at nums1[i] and nums2[j]
The problem is, DP[i][j] = nums1[i]*nums2[j] + max(DP[i+x][j+y])) since we don't know the next dot product pair
Time complexity O(n^2*m^2), with row max tracking still O(nm*min(m, n))

Method 2, 2D table best result DP[i][j] is: subseq selection range of nums1[i:] and nums2[j:]
This provides soft constraint on DP compared to method 1, without forcing subseq starts with i-j
The selection range expand from right to left for both array. At i-j position:
    either i-j won't pair, thus inherit best result from nums1[i+1:] ~ nums2[j:] and nums1[i:] ~ nums2[j+1]
    or i-j pair, and combine with best result from nums1[i+1:] ~ nums2[j+1:]
        since i-j are paired, remaining subseq can be empty, thus minimum 0
Similar to LCS (longest common subsequence) state trasition logic, with different processing

Time O(mn), Space O(mn) can be O(min(m, n)) if keeping only 2 adjacent rows
'''

from typing import List

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        # dp[i][j] is the best result if considering nums1[i:] and nums2[j:]
        # final result is dp[0][0]
        dp = [[0] * n for _ in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                # include nums1[i] but not pairing with nums2
                down = dp[i+1][j] if i < m-1 else float("-inf")

                # include nums2[j] but not pairing with nums1
                right = dp[i][j+1] if j < n-1 else float("-inf")

                # down-right best result
                # forcing nums1[i]*nums2[j] makes subseq non-empty
                # thus down-right best subseq can be empty, hence 0
                dr = max(dp[i+1][j+1], 0) if i < m-1 and j < n-1 else 0
                
                # best result comes from pairing i-j plus down-right
                # or not pairing and just inherit down or right
                dp[i][j] = max(down, right, nums1[i] * nums2[j] + dr)

        return dp[0][0]