'''
Leetcode 3260. Find the Largest Palindrome Divisible by K
Find the largest palindromic integer of length n that is divisible by k

Checking each n/2 digit choice takes 10^n time

Method 1, dp on available remainder with max choice of digits
O(100*n) => O(n) iterations
head tail is the power factor of 10^head 10^tail at corresponding palindrome positions
works for any k
but tuple copying takes time, overall Time O(n^2) TLE

Method 2, 

'''

class Solution:
    # method 1, build from previous remainders, copy digit selection tuple
    # Time O(n^2)
    def largestPalindrome(self, n: int, k: int) -> str:
        # initialize remainder array for 10^x % k considering remainder loop
        rem10 = []
        p_rem = 1
        a0, count = 0, 1
        for _ in range(n):
            if p_rem in rem10:
                a0 = rem10.index(p_rem)
                count = len(rem10) - a0
                break
            rem10.append(p_rem)
            p_rem = p_rem * 10 % k
        head, tail = n-1, 0
        cur, nex = {0: ()}, {}
        while head >= tail:
            hd = head if head < len(rem10) else (head-a0)%count+a0
            tl = tail if tail < len(rem10) else (tail-a0)%count+a0
            for x in range(9, -1, -1):
                if tail == 1 and x == 0:
                    break
                cur_rem = (rem10[hd] + rem10[tl]) * x % k
                if head == tail:
                    cur_rem = (cur_rem - rem10[tl] * x) % k
                for r, t in cur.items():
                    r1 = (cur_rem + r) % k
                    if nex.get(r1, ()) <= t:
                        nex[r1] = (*t, x)

            cur, nex = nex, {}
            head -= 1
            tail += 1

        # key 0 in cur means final best choice for hal palindrome
        if n % 2:
            return ''.join(str(x) for x in (cur[0] + cur[0][::-1][1:]))
        return ''.join(str(x) for x in (cur[0] + cur[0][::-1]))

