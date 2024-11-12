'''
Hackerrank, Correlation Sum
Given 2 int array of the same length: a, b
Rearrange b so that the sum of b[i] that are greater than a[i] is maximum

As we can rearrange b freely, we start with sorting a, and try to assign as many b[i] to be larger than a[i]
First, sort b in descending order, which garantees lower limit of acceptible b[i]
Then try to swap next (greedy) biggest b[i] that is smaller than a[i] with some previous b[j],
	if after swapping, b[j] > a[i] and b[i] > a[j], maintaining the 'greater than' structure of b[:i]

Time O(nlogn), space(O(1))
'''
import random

def correlationSum(a: list, b: list) -> int:
    a.sort()
    b.sort(reverse=True)
    idx = 0
    s = 0
    # find the starting index where b[i] <= a[i]
    while idx < len(b):
        if b[idx] <= a[idx]:
            break
        s += b[idx]
        idx += 1
    # print('sorted a = ', ' '.join([f'{x:>2}' for x in a]))
    # print('sorted b = ', ' '.join([f'{x:>2}' for x in b]))
    
    if idx == len(b):
        return s
    # another pointer j trace back from idx to find smallest b[j]
    # -- that can safely swap with current(next largest) b[idx]
    # thus to include b[idx] in result and maintaining all included b[i] > a[i]
    j = idx - 1
    while j >= 0 and idx < len(b):
        if b[j] > a[idx] and b[idx] > a[j]:
            s += b[idx]
            b[j], b[idx] = b[idx], b[j]
            idx += 1
        j -= 1
    # print('optimu b = ', ' '.join([f'{x:>2}' for x in b]))
    return s

if __name__ == '__main__':
    # a = [1,2,3,4,5]
    # b = [3,5,4,6,2]
    # print(correlationSum(a, b))
    for _ in range(5):
        a = [random.randint(1, 30) for _ in range(20)]
        b = [random.randint(1, 30) for _ in range(20)]
        print()
        print(correlationSum(a, b))