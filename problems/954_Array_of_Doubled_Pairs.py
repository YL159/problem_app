'''
Leetcode 954. Array of Doubled Pairs
Check if an int array can be rearranged into [a,2a, b,2b...] form

Equivalent to all the following:
1. positive part and negative part have even length
2. each number after matching its half, remaining count should also match its double.
'''
from typing import List
import bisect, collections

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        new_arr = sorted(arr)
        index = bisect.bisect(new_arr, 0)
        return self.check(new_arr[index:]) and self.check(new_arr[:index])
    
    # check ar of same sign ints.
    # Greedily check if smaller ints have corresponding bigger ints, and up
    def check(self, ar: List[int]) -> bool:
        if not ar:
            return True
        if len(ar) % 2:
            return False
        book = collections.Counter(ar)
        keys = sorted(list(book.keys()), reverse=ar[0]<0)
        for a in keys:
            if book[a]:
                if a*2 not in book or book[a*2] < book[a]:
                    return False
                book[a*2] -= book[a]
        return True