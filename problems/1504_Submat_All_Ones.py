'''
Leetcode 1504. Count Submatrices With All Ones
Given a matrix of only 0/1s, count the number of submat with all 1s.

Transform the matrix with idea from 1727. Largest Submatrix With Rearrangements
For each column, at row idx, count consecutive 1s from idx and above.
1,1,0		1,1,0
0,1,1	=> 	0,2,1
1,1,1		1,3,2
Process rows also work, but inspect columns in later operations.

Now for each row, we have 3 ways to count desired submat. Number is consecutive 1s above.
Idea similar to 84. Largest Rectangle in Histogram

Method 1: For each index, go left and find cur = min(cur, row[j]), till row[j] = 0.
Add them to result.
e.g. row i: 1,0,1,2,3,1,2,0,1
						|
				1,1,1,1,2	are the results for the second 2. Sum them to result.
And move on. This is O(n^2) time for inner loop. Overall O(mn^2)

Method 2: create a monotonic increasing stack for each row, but not popping larger stack tops.
And maintain a prefix sum of the stack to avoid repeated summation.
e.g. row i: 1,0,1,2,3,1,2,0,1
					| | |
		stack  [1,2,3]| |	pref = 6 => add pref to result. This is for that 3 in the row
		stack  [1,1,1,1]| 	pref = 4 => add pref to result, for third 1 in the row
		stack  [1,1,1,1,2]	pref = 6 => for second 2 in the row, add to result
Encountering any 0, reinitialte stack to empty and pref = 0
This is also worst case O(n^2), but with prefix sum, overall performance is somewhat better.

Method 3: Similar to method 2, using monotonic increasing stack.
But we can indeed pop those on stack top that is > mat[i][j].
Meanwhile also maintain the prefix sum the same as method 2,
	by counting the popped idx with stack top idx, these idxs must be the same, and reduce them to mat[i][j]
Add prefix to result as well.
This has the same effect as method 2, but time complexity is strict O(n) for the inner loop.
'''
from typing import List

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        # for each col, count consecutive 1 at each idx
        m, n = len(mat), len(mat[0])
        for j in range(n):
            count = 0
            for i in range(m):
                if mat[i][j] == 1:
                    count += 1
                else:
                    count = 0
                mat[i][j] = count

        res = 0
        # for each row, count submat ending at i,j
        
        # # 1. each i,j, check prev non-greater col, inner loop O(n^2)
        # for i in range(m):
        #     for j in range(n):
        #         # add submat of width >= 1, ending at i,j
        #         cur = mat[i][j]
        #         for k in range(j, -1, -1):
        #             if mat[i][k] == 0:
        #                 break
        #             cur = min(cur, mat[i][k])
        #             res += cur

        # # 2. similar to 84. largest rectangle in histogram
        # # but recording/modify right-ward monotonic stack with its prefix sum
        # # but inner loop still worst case O(n^2)
        # for i in range(m):
        #     stack = []
        #     pref = 0
        #     for j in range(n):
        #         if mat[i][j] == 0:
        #             stack = []
        #             pref = 0
        #             continue
        #         k = len(stack) - 1
        #         while k >= 0 and stack[k] > mat[i][j]:
        #             pref -= stack[k] - mat[i][j]
        #             stack[k] = mat[i][j]
        #             k -= 1
        #         stack.append(mat[i][j])
        #         pref += mat[i][j]
        #         res += pref
                
		# 3. similar to method 2, but we can pop the stack and maintain pref the same value as method 2,
        # without traversing stack, instead pref -= (row[stack[-1]] - mat[i][j]) * idx_difference
        # strictly O(n) for inner loop
        for i in range(m):
            row = mat[i]
            stack = []
            pref = 0
            for j in range(n):
                while stack and row[stack[-1]] > row[j]:
                    idx = stack.pop()
                    # maintain pref sum to match current state of stack in method 2
                    # stack[-1] idx is possibly related to 0, thus keep 0's index for correct start
                    start = stack[-1] if stack else - 1
                    # from idx to current stack[-1] all are the same row[idx], reduce them to row[j]
                    pref -= (row[idx] - row[j]) * (idx - start)
                stack.append(j)
                pref += row[j]
                res += pref

        return res
