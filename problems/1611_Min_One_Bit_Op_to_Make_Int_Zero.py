'''
Leetcode 1611. Minimum One Bit Operations to Make Integers Zero
Given int n, for its binary form, for each operation, choose:
	1. change 0th (least significant) bit of n
    2. change x in ...x10...0 form in binary n
Find min operations to make n 0

Observations: 100 -> 0:
100, 101, 111, 110, 010, 011, 001, 000, total 7 steps for 100 -> 0
	=> the process touches every possible 3-digit binary repr, except for 100 itself
	=> 7 = 2^3-1
1000 -> 0: 1000 --(0->100:7)-> 1100 -(:1)> 0100 -(:7)> 0 = 15
	=> 15 = 2^4-1, also touches every 4-digit binary repr except 1000
Thus operations = 2^n - 1 for n-digit 10...0 number

This means 10...0 -> 0 takes the most steps among all n-digit int
because other form can reduce to 0 half way
	=> for each suffix that is not 10...0, its ops to make itself 0, can help reduce current 10...0 steps to 0
e.g. 101 -> 0 is 6 steps, because 100 -> 0 is 7 steps, but suffix 1 -> 0 is 1 step
	=> from above step showcase, suffix 1 helped reduce 100 -> 0 steps by 1 (starts from 101)
    => 7 - 1 = 6
    => 2^n-1 - steps(suffix) = steps to make current digit '1' to '0'

Time O(log(n)), Space O(log(n))
'''

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        bits = list(bin(n))[2:]
        n = len(bits)
        # precompute arr[i]: op to make 10...0 of i bits to 0
        arr = [0, 1]
        for _ in range(n-1):
            arr.append(arr[-1]*2+1)
        
        def build_0(start: int) -> int:
            if start >= n:
                return 0
            if bits[start] == '0':
                return build_0(start + 1)
            # now 1..., most steps are if 10..0
            # remove steps that keeps it away from 0...0 form
            return arr[n-start] - build_0(start + 1) 
        
        return build_0(0)