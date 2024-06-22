'''
Leetcode 648. Replace Words
Replace each word in a sentence with the shortest prefix from given dictionary

Sort the dictionary, and binary search the range that starts with word[0].
The shortest prefix likely appear in the front of the result range, thus greedily match and break

If asks for the longest prefix, and the dictionary is very long, we may recursively use binary search untill the range is 0 or 1
'''
from typing import List
import bisect

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort()
        first = [w[0] for w in dictionary]
        words = sentence.split()
        # find the range of roots starts with word[0] and greedy
        for i, word in enumerate(words):
            left = bisect.bisect_left(first, word[0])
            right = bisect.bisect_right(first, word[0])
            for w in dictionary[left:right]:
                if word.startswith(w):
                    words[i] = w
                    break
        return ' '.join(words)