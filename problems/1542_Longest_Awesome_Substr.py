'''
Leetcode 1542. Find Longest Awesome Substring
Given a string of digits, find length of longest substr that can be rearranged as a palindrome.

First comes to mind is "two sum" problem technique:
	check prefix array's digit count, and compare with earlier prefix digit count.
But palindromic subarr requires subtraction of digit count dictionary, not just end-point seen/not seen
And we need a palindromic subarr, which require only odd/even for each digit
	=> record only oddity of prefix digit frequencies, transform digit count subtraction into bit oddity match
	=> we can "encode" the digit count into string/bits, alter this encoded prefix digit count to match any seen ones

Suppose s = "3242415"
At idx = 0, prefix digit count(oddity): {3:1}
	=> digit count array (oddity) [0,0,0,0,0,0,1,0,0,0], from right meaning only 1x 3, and is odd
	=> bit encoding: 0b1000 = 8
At idx 5, prefix subarr "324241", digit count: {2:2, 3:1, 4:2, 1:1}
	=> digit count array (oddity) [0,0,0,0,0,0,1,0,1,0], only 1 and 3 appear in odd frequency
    => bit encoding: 0b1010 = 10
Use unique bit encoding of each prefix as key, record its earliest appearance

Subarr is even length palindrome => current bit encoding/config is seen.
Subarr is odd length palindrome => alter 1 bit and new encoding is seen.

Time O(n), Space O(1)
'''

class Solution:
    def longestAwesome(self, s: str) -> int:
        zero = ord("0")
        book = {0: -1}
        pref, res = 0, 0
        for i, c in enumerate(s):
            # find the current oddity config of 9~0
            pref ^= 1 << ord(c) - zero
            # if palindrome is even length, should have seen this pref config before
            res = max(res, i - book.get(pref, i))
            # if palindrome is odd length, change one oddity of pref config and check if seen
            for j in range(10):
                digit = 1 << j
                res = max(res, i - book.get(pref ^ digit, i))
            # update new pref config idx, thus to keep the smallest seen idx.
            if pref not in book:
                book[pref] = i
        return res