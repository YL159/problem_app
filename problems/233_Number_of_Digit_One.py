'''
Leetcode 233. Number of Digit One
Given an int n, count the # of 1s in all non-negative x <= n

Consider 13: 1,2,3,4,5,6,7,8,9,  10,11,12,13
Observation:
1. for each digit position, as long as there are higher position digits:
	It will go through 0~9 for each higher position values:
    	13's unit place go through 0~9 once, 13//10 = 1
        101's unit place go through 0~9 10 times, 101//10 = 10
	In each 0~9 run, 1 will appear 10^(x-1) times, x is digit position
		101's ten's place go through 0~9 once, 101//100 = 1
        but each run it appears 10 times (10~19), 10^(2-1) = 1
Thus each digit's bulk appearance is higher digit number * 10^(lower digit count)

2. at digit position x, suffix number also contributes to current 1
	If digit = 1, addition relies on suffix.
    	13 digit 1's residual 1 count is 10,11,12,13, suffix 3 + 1 = 4
    If digit > 1, addition is max 10^(lower digit count)
		13 digit 3's residual 1 count is 11, 10^0 = 1

Thus the algorithm is:
at x digit from right, 1 appear n//10^x*10^(x-1) +
	if x digit == 1, n%10^(x-1)+1 times
	elif x digit > 1, 10^(x-1) times

Time O(log(n)), Space O(1)

e.g.
13: 1st digit 3: 13//10*1 + 1 = 2, 2nd digit 1: 13//100*10 + 13%10+1 = 4
Total 2+4 = 6

101: 1st digit 1: 101//10*1 + 1 = 11, 2nd digit 0: 101//100*10 + 0 = 10
3rd digit 1: 101//1000*100 + 101%100+1 = 2
Total = 11+10+2 = 23
'''

class Solution:
    def countDigitOne(self, n: int) -> int:
        # p is 10^(suffix digit count), suffix is num till x position from right
        p, suffix = 1, 0
        res = 0
        while n:
            d = n % 10
            n //= 10
            # bulk 1 appearances, depending on prefix (remaining n)
            res += n * p
            # residual 1 appearance, depending on suffix
            if d == 1:
                res += suffix + 1
            elif d > 1:
                res += p
            suffix += d * p
            p *= 10
        return res