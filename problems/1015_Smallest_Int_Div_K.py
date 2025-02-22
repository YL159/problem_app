'''
Leetcode 1015. Smallest Integer Divisible by K
Find the length of some decimal int 1...1 that is divisible by k.
If no such int, return -1

Method 1
Try from 1, 11, 111, ... but this method actually test each 1...1 and divides k, storing bigger numbers in memory

Method 2
Let 1[n] be 1...1 int having n*1s
Let k = 7, currently testing 111, fail. But we record its remainder 111 % 7 = 6
Next 1[4] = 1[3] + 10^3, 1[4] % 7 = (1[3] % 7 + 10^3 % 7) % 7
									known	   unknown
And in future, it needs 10^t % 7. Thus we can generate 10^t % 7 by 10^(t-1) % 7:
	10^t % 7 = ((10^(t-1) % 7) * 10) % 7
				  known
Thus we keep:
1. 1[n] % k remainders and record seen remainders
2. 10^t % k remainders
for the isomorphic structure in incremental iterations.

Once we see 1[n+t] % k remainder is the same as 1[n] % k, that means:
	1[t]*10^(n) % k = 0 => 1[t]*10^(m*n) % k = 0 for m >= 1
i.e. concat mult of 1[t] to current 1[n] won't get any new remainders => loop detected
If the repeated remainder is not 0, then no such 1[n] divides k

Time O(k), since there are max k remainders.
Space O(1), and the constant magitude is limited.
'''
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # k can only end with 1,3,7,9
        # suppose n*1: 1...1 % k = x, then adding 1 is adding x1 = 10^(n+1) % k to x.
        # x1 is 10*x0 % k, where x0 = 10^n % k
        # if new modulo is seen before, then not possible. If 0, return iter count
        count = 1
        rem10n = 1 % k # generate 10^n % k
        rem = rem10n # current 1...1 % k
        seen = set()
        while rem not in seen and rem != 0:
            seen.add(rem)
            rem10n = rem10n*10 % k
            rem = (rem + rem10n) % k
            count += 1
        if not rem:
            return count
        return -1
