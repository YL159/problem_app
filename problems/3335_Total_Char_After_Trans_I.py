'''
Leetcode 3335. Total Characters in String After Transformations I
Given a string of letters, for each operation:
	Each letter in string is replaced by its next letter
	'z' replaced by 'ab'
Return the length of string after t operations, mod (10^9+7)


Each 26 cycle, a letter repeats itself, and add 1 freq to next letter
but for 'z', it repeats itself, and add 1 freq to both 'a' & 'b'
Time O(26*n + 26*rem) = O(t + 25*rem) = O(t)
Space O(26) = O(1)
'''
import collections

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        a = ord('a')
        book = collections.Counter(s)
        freq = [book[chr(a+i)] for i in range(26)]
        rem, n = t % 26, t // 26
        
        # treat n whole cycles
        for _ in range(n):
            cur = freq[0]
            for i in range(25):
                nex = freq[i+1]
                freq[i+1] = nex + cur
                cur = nex
            freq[0] += cur
            freq[1] += cur
        
        # for remainder cycles, shift frequency array normally
        for _ in range(rem):
            z = freq[-1]
            freq[1:] = freq[:-1]
            freq[0] = z
            freq[1] += z
        
        return sum(freq) % (10**9+7)