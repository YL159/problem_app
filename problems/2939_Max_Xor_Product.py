'''
Leetcode 2939. Maximum Xor Product
Given int a, b, n. Find max (a xor x) * (b xor x) for all int x that 0 <= x < 2^n.

Suppose a and b xor with x and x', surely both (a xor x) and (b xor x') can be maximized
	=> choosing x = a & (2^n-1) xor (2^n-1), same for x' and b.
    => lease significant n bits of a and b will be maximized to 111...1 in (a/b xor x/x')
But x may not agree with x' at every bit
	=> keep the same bits they agree, and decide the varied bits

e.g. a = 0:000, b = 7:111, n = 2
va = a xor (11) = 0(11), vb = b xor (11) = 1(00)
We focus on bracket part, where x affects. Here x = (11), x' = (00), disagree on every bit
	=> for each bit they disagree, complying with x or x' at this bit will bring different increment to (a/b xor x/x')
	=> each bit they agree, greedily complying with x or x' will result the same increment of both (a/b xor x/x')

The base of such increment is:	ta = a & va = 0(00), tb = b & vb = 1(00)
	reset a/b bits that disagree when comparing x/x' as 0
    
Now consider y = (m+t1) * (n+t2), where t1+t2 is fixed, and want to maximize y
	=> easy to see max y is reached only when (m+t1) and (n+t2) are as close as possible
    => distribute t1 and t2 to make them closer
Here we should distribute disagreed bits from significant to insignificant
because 2^n > 2^(n-1) + 2^(n-2) + ... + 2 + 1
	=> check new ta, tb after each asignment, comply new disgreed bit to the side that is smaller
		for bits that agree, sure we can increase both ta and tb, but it won't change ta tb comparison
    => this strategy guarantees closest final ta tb.

Time O(n), Space O(1)
'''

class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        mod = 10**9 + 7
        if n == 0:
            return a*b%mod
        m = (1 << n) - 1
        va, vb = a ^ m, b ^ m
        x1, x2 = va & m, vb & m
		# early exit if all bits of x agree with x'
        if x1 == x2:
            return (x1^a) * (x1^b) % mod
        x = x1 & x2
        mask = 1 << n - 1
        ta, tb = a & va, b & vb
        while mask > 0:
            if mask & va != mask & vb:
                if ta >= tb:
                    # comply vb's current bit's choice of 0/1
                    x |= mask & vb
                    # compliance gives increment of mas to tb
                    tb |= mask
                else:
                    # comply va's current bit, and increment to ta
                    x |= mask & va
                    ta |= mask
            mask >>= 1
        return (x^a) * (x^b) % mod
        
	# method 2, from discussion
    # assign each bit if it contributes to overall target increment
    # because each bit is independent
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        for x in (2**i for i in range(n)):
            if a * b < (a ^ x) * (b ^ x):
                a ^= x
                b ^= x
        return a * b % int(1e9 + 7)