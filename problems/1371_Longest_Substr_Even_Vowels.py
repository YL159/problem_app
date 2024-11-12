'''
Leetcode 1371. Find the Longest Substring Containing Vowels in Even Counts
As title describes. Vowels are 'aeiou'

Standard solution uses bit mask prefix XOR to note each vowel's count parity.
And bit mask is translated(hash) to idx of last appearance array.

Here is the same general idea with different approach
Using 'vowel count % 2' instead of bit mask XOR to record parity.
Using 'vowel count parity string' to hash instead of bit mask idx.
Skip checking consonants, use only vowel idx as event wake up.

Time O(n), space O(n).
Space can be potentially O(2^5) -> O(1) if integrating 'non_vowel' consonant length checking into the main for loop.
'''
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # record vowel positions, padding with -1 and len(s)
        positions = [-1]
        record = {'00000': -1}
        vow = 'aeiou'
        vowels = set(vow)
        # vowel count % 2, parity of each 'aeiou'
        count = [0, 0, 0, 0, 0]
        get_res = False
        res = 0
        for i, c in enumerate(s):
            if c not in vowels:
                continue
            positions.append(i)
            if get_res:
                res = max(res, i - 1 - record[to_get])
                get_res = False
            idx = vow.index(c)
            count[idx] = (count[idx] + 1) % 2
            # vowel count parity code for current position
            # "a:0, e:1, i:4, o:3, u:0" -> '01010'
            code = ''.join(str(x) for x in count)
            # if the code is seen, substr in between must have even vowels
            # resolve it at next vowel event to include possible consonants afterwards
            if code in record:
                get_res = True
                to_get = code
            else:
                record[code] = i
        # complete the vowel event resolution
        if get_res:
            res = max(res, i - record[to_get])
        if len(record) == 1:
            return len(s)
		# check substr containing only consonants
        positions.append(len(s))
        non_vowel = 0
        for j in range(1, len(positions)):
            non_vowel = max(non_vowel, positions[j] - positions[j-1] - 1)
        return max(res, non_vowel)