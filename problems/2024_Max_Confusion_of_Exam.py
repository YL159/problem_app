'''
Leetcode 2024. Maximize the Confusion of an Exam
Given a string of T/F representing true/false of a question
find the longest substr of only T or F, if flipping at most k answers

Method 1, binary search for the longest substr length in [1, len(str)+1]
1 is definitely possible, len(str)+1 is definitely NOT possible
then use the fixed window size to check if such subarr has T/F <= k
Time O(nlogn), space O(1)

Method 2, sliding window with variable length
For T, keep exactly k Fs in the window. Right consumes an F, then left must spit out an F
Record max length. So does that for F
Or record both T and F, carefully move right/left. 1 pass
Time O(n), space O(1)
'''
import collections

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # method 1, fix the consecutive window size, check if possible within k op
        l, r = 1, len(answerKey)+1
        while l < r-1:
            mid = (l+r)//2
            book = collections.Counter(answerKey[:mid-1])
            for i in range(mid-1, len(answerKey)):
                book[answerKey[i]] += 1
                if book["F"] <= k or book["T"] <= k:
                    l = mid
                    break
                book[answerKey[i-mid+1]] -= 1
            else:
                r = mid
        return l

    def maxConsecutiveAnswers2(self, answerKey: str, k: int) -> int:
        # method 2, sliding window, keep exactly k T/F within window
        def maxCon(ans: str) -> int:
            l, r = 0, 0
            count = 0
            res = 0
            while r < len(answerKey):
                while r < len(answerKey) and count <= k:
                    if count < k:
                        count += answerKey[r] != ans
                    elif answerKey[r] != ans:
                        break
                    r += 1
                # now answerKey[l:r] contains k flip(ans)
                res = max(res, r - l)
                while count >= k:
                    count -= answerKey[l] != ans
                    l += 1
            return res

        return max(maxCon('T'), maxCon('F'))