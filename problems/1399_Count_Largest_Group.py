'''
Leetcode 1399. Count Largest Group
For int in [1, n], each has a digit sum.
Some # have the same digit sum, like 12, 21 and 3, thus they belong to the same group.
Find the # of groups that has the max members

Method 1, iterate each int and increment the digit sum group size.
This is a naive approach, and the reason it's easy question.
Time O(nlog(n)), Space O(log(n))

Method 2, digit sum group size from memo table
Consider int 1234 and 1235, their digit sum differ by only 1, but (1+2+3) part is repeatedly calculated
	=> iterate over [1, n] produce a lot of repeated addition

Suppose n = 223, and we fix the digit sum = 7. Int has max 3 digits
For cases	0__ => need # of 2 digit int that sums to 7
			1__ => need # of 2 digit int that sums to 6
            2__ => special treatment, can't use all # that has 2 digit and sums 5, like 232, 241, 250 > 223
Thus we should build a memo table that remembers # of integers that:
	Has x digits (can have leading 0), AND with digit sum y
The table will have log_10(n) rows, and 9*log_10(n) columns. Because x digits get max digit sum 9*x
While populating the table, use previous row's prefix sum to reduce cell calculation complexity to O(1)

For 3 digit n, the memo table is:
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[1, 2, 3, 4, 5, 6, 7, 8, 9,10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[1, 3, 6,10,15,21,28,36,45,55,63,69,73,75,75,73,69,63,55,45,36,28,21,15,10, 6, 3, 1]
The table is fixed for any x digit n.

Then fixing each possible digit sum [1, 9*log_10(n)], use the table to find the count of ints within [1, n] range
Special treatment at n only when reaching the last digit for some digit sum.
Check if remaining digit sum is over or under n's last digit.

Time O(log^2(n)), Space O(log^2(n))
'''

class Solution:
    def countLargestGroup(self, n: int) -> int:
        # # of groups is about 9*log_10(n)
        # find each group's size is quicker than processing each int
        # make a memo table of (max int length, digit sum)
        m = len(str(n))
        memo = [[0] * (9*m+1) for _ in range(m+1)]
        memo[0][0] = 1
        
        # we don't need 0th row, which represents int length 0
        # but 0th row can help with building 1st row with the same logic
        pref = [1]*(9*m+1)
        for length in range(1, m+1):
            nex_pref = [1]
            memo[length][0] = 1
            for s in range(1, 9*m+1):
                prev = 0
                if s >= 10:
                    prev = pref[s-10]
                memo[length][s] = pref[s] - prev
                nex_pref.append(nex_pref[-1] + memo[length][s])
            pref = nex_pref
        
        N = [int(d) for d in str(n)]
        # iterate digit sum from 1 to max possible 9*log(n)
        max_size, count = 0, 0
        for ds in range(1, 9*m+1):
            # find how many numbers has digit sum ds
            ds_size = 0
            # loop for each digit of n, max 9*log(n) iterations
            for i, d_max in enumerate(N[:-1]):
                for _ in range(d_max):
                    if ds < 0:
                        break
                    ds_size += memo[m-i-1][ds]
                    ds -= 1
            if 0 <= ds <= N[-1]:
                ds_size += 1
            
            if ds_size > max_size:
                max_size = ds_size
                count = 1
            elif ds_size == max_size:
                count += 1
        return count
