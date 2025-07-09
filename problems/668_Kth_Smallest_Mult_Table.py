'''
Leetcode 668. Kth Smallest Number in Multiplication Table
Given positive int m,n, the multiplication table is [1, m] multiply [1, n]
Find kth smallest # in this mult table

Similar to #719, binary search for mult X, check if exactly k pairs get mult <= X
	for each row, count # in [1, n] range where mult row i <= X
Time O((m+n)log(m*n)), Space O(1)
'''

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        if m == 1 or n == 1:
            return k
        # l: impossible mult; r: max possible mult
        l, r = 0, m*n
        while l < r-1:
            X = (l+r)//2
            count = 0
            # 2 pointer shrinking j to make i*j <= X
            j = n
            for i in range(1, min(m+1, k)):
                while j > 0 and i*j > X:
                    j -= 1
                count += j
            # # method 2, j is continuous [1,n], just div and count
            # for i in range(1, min(m+1, k)):
            #     count += min(X // i, n)
            if count < k:
                l = X
            else:
                r = X
        return r