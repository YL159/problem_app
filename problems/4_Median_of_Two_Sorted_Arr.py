'''
Leetcode 4. Median of Two Sorted Arrays
Given 2 sorted array, find median if merged as 1 array.
Time log(m+n)

Method 1, naively merge arrs and find median, O(m+n)

Method 2, outer loop binary search nums1, inner bisect on nums2 with nums1[mid], O(log(m)*log(n))

Method 3, great idea from discussion
recursively cut smallest target//2 numbers from 2 lists.
Initially Target = total//2, and it will reduce by # of cut numbers.

Method 4, similar to method 2, but we don't have to bisect nums2 repeatedly in outer loop
Since the 2 array are sorted, the result arr[0,median] must be the combination of nums1[0,m1], nums2[0,m2]
	=> find such m1, m2 pairs and maintain m1 + m2 + 2(idx start at 0) = total//2
	=> m2 is determined once m1 is determined, thus degree of freedom is only m1
    => binary search m1 on nums1
Then check m1, m2 are valid, as binary search criteria
	<=> if we color nums1[0,m1] and nums2[0,m2] in final array, they should produce no "holes"
    	i.e. no uncolored numbers in final[0,median]

e.g. nums1 = [1,2,5,7,8], nums2= [2,4,6]. Total = 8, m1+m2+2 = 5
1. m1 = 2(5), m2 thus 1(4). This is valid because all nums2[,m2] < nums1[m1], and all nums2[m2+1,] >= nums1[m1]
	=> nums1[m1] separates nums2 in the same way as nums2[m2] separate nums2
    => no "holes"
2. m1 = 3(7), m2 thus 0(2). This is invalid because nums2[m2+1] = 4 still < nums1[m1] = 7
	=> the excluded 4 is supposed to be included, because nums1[m1] is already 7
    => "holes" in combined array
    => m1 too large, should move left
3. m1 = 1(2), m2 thus 2(6). Invalid again because nums1[m1+1] = 5 still < nums2[m2] = 6
	=> exculded 5 should be included because < 6
    => m1 too small, should move right
Other cases are m2 are out of bound
	=> either m1 too large or too small so that m2 became abnormal to compensate it
    => move m1 accordingly

Then finally check & out put the correct median in all cases.

This method uses unconventional binary search structure and used middle idx for later calculation.
Time O(log(min(m, n)), space O(1)

'''
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        if not nums1:
            return (nums2[(n2-1)//2] + nums2[n2//2])/2
        if not nums2:
            return (nums1[(n1-1)//2] + nums1[n1//2])/2
        # use shorter nums1 as binary search pool
        # because here nums2 search by count, not by controling its idx
        if n1 > n2:
            nums1, nums2 = nums2, nums1
            n1, n2 = n2, n1
        # want the count of lefts in both nums include median
        target = (n1 + n2) // 2 + 1
        l, r = -1, n1
        # criteria: nums1[,m1] + nums2[,m2] is the left half of merged sorted array
        while l < r:
            m1 = (l+r)//2
            m2 = target - 2 - m1
            # m2<0 => nums1 included too many
            # Or m2 right neighbor is smaller than nums1[m1], invalid
            # if nums1[m1] is included, so should nums2[m2+1]
            # => nums1 range is large, 
            if m2 < 0 or m2 < n2-1 and nums2[m2+1] < nums1[m1]:
                r = m1
            # m2>=n2, => nums1 included too few
            # Or m1 right neighbor is smaller than nums2[m2]
            # again invalid because thus nums1[m1+1] should also be included
            # => nums1 range is too small
            elif m2 >= n2 or m1 < n1-1 and nums2[m2] > nums1[m1+1]:
                l = m1
			# now m1, m2 are definitely valid, note m1 in [-1, n1-1] range
            else:
                break
        # odd total
        if (n1+n2) % 2:
            if m1 == -1:
                return nums2[m2]
            return max(nums1[m1], nums2[m2])
        # even total
        if m1 == -1:
            return (nums2[(n1+n2-1)//2] + nums2[(n1+n2)//2])/2
        a, b = float('-inf') if m1 <= 0 else nums1[m1-1], nums1[m1]
        c, d = float('-inf') if m2 <= 0 else nums2[m2-1], nums2[m2]
        return sum(sorted([a,b,c,d])[-2:])/2