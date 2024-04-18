'''
Leetcode 1387. Sort Integers by The Power Value
Each # can be reduced to 1, power is the # of steps to reach 1

Hashtable store every encountered # with its steps to reach 1
'''
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        book = {1: 0}
		# lazy inner func using 'book' as external public memo
        def powers(n: int) -> int:
            if n in book:
                return book[n]
            p = 0
            if n % 2:
                tmp = 3*n + 1
            else:
                tmp = n // 2
            p += 1
            if tmp in book:
                p += book[tmp]
            else:
                p += powers(tmp)
            book[n] = p
            return p
        
        sor = list(range(lo, hi+1))
        power = [powers(x) for x in sor]
        res = [a for _, a in sorted(zip(power, sor))]
        return res[k-1]