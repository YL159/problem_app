'''
Leetcode 2429. Minimize XOR
Given 2 int n1, n2, find positive int x:
1. Has same count of set bits as n2.
2. x XOR n1 is minimal

x has the same number of 1s as binary n2.
	e.g. n2=11: 1011, x has 3 set bits
To minimize x XOR n1, we want to cancel as many significant bits in n1 as possible
Case 1:	x has set bits <= n1's set bits => cancel n1 from significant bits
	n1:	110 0101, x has 3 set bits
	x:	110 0100, thus x XOR n1 = 000 0001 = 1
Case 2: x has more set bits
	n1:	110 0101, x has 5 set bits
	x':	110 0101, now XOR cancels all n1 set bits, but x has 1 more set bit
	Thus fill the non-set bit from least significant bit, to minimize final result
	x:	110 0111
'''
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # if n2 set bits <= n1, x set bits are all higher set bits of n1
        c1 = num1.bit_count()
        c2 = num2.bit_count()
        if c2 <= c1:
            rem = c1 - c2
            count = 0
            x = num1
            while rem > 0:
                if num1 & 1:
                    rem -= 1
                count += 1
                num1 >>= 1
            x >>= count
            return x << count
        
        # otherwise, x cover all set bits of n1, and fill n1's non-set bit from lsb
        rem = c2 - c1
        x = num1
        count = 0
        while rem > 0:
            if not num1 & 1:
                rem -= 1
                x |= 1 << count
            count += 1
            num1 >>= 1
        return x