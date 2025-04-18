'''
Leetcode 904. Fruit Into Baskets
Given an array of ints representing fruit types for each tree, with basket carrying max 2 fruit type
Find the longest subarr that has only 2 type of fruits.

Sliding window, that keeps max 2 types of fruits in the window.
Collect local subarr length when visiting 3rd type or end of array
thus to get global max length

Time O(n), Space O(1)
'''
from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # sliding window method, but refined
        res = 0
        basket = {}
        i, j = 0, 0
        while j < len(fruits):
            if len(basket) < 2 or fruits[j] in basket:
                # record the lates idx for current fruit
                basket[fruits[j]] = j
                j += 1
                continue
            res = max(res, j - i)
            other = (set(basket.keys()) - {fruits[j-1]}).pop()
            i = basket[other] + 1
            del basket[other]
        return max(res, j - i)
            
        # history, current = 0, 0
        # curset = {fruits[0]}
        # i, j = 0, 0
        # prev = fruits[0]
        # for index in (range(len(fruits))):
        #     if fruits[index] != prev:
        #         i, j = j, index
        #         prev = fruits[index]
        #         # Keep track of most recent 2 number's left most repeating index
        #     if fruits[index] in curset:
        #         current += 1
        #     elif len(curset) < 2: # In case of repeating latest number
        #         current += 1
        #         curset.add(fruits[index])
        #     else:
        #         curset = {fruits[i], fruits[j]}
        #         current = index - i + 1 # Consider repeated fruits[i] number
        #     history = max(current, history)
        # return history