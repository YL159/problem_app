'''
Leetcode 1462. Course Schedule IV
Given number or courses, and course prerequisites: list([prereq for i, course i]). Prerequisites are transitive
For each query [u, v] in query list, answer if u is prerequisite of v

In order to quick answer to each query, we need to know all courses unlocked by u.
Use recursive early-exit function calls to find out all prerequisites.
A course unlocks all immediate other courses mentioned in prerequisite list,
	and all the courses unlocked by those courses,
    untill some final courses that don't unlock any new courses.
Record intermediate results (subtree) for early return.
'''
from typing import List
import collections

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # get all courses unlocked by course i, recursive for easier memo
        # query check will be faster
        unlock = collections.defaultdict(set)
        for a, b in prerequisites:
            unlock[a].add(b)
        
        book = collections.defaultdict(set)
        def resolve(course: int) -> set:
            if course not in unlock:
                return set()
            if course in book:
                return book[course]
            book[course] |= unlock[course]
            for c in unlock[course]:
                book[course] |= resolve(c)
            return book[course]
        
        for i in range(numCourses):
            book[i] = resolve(i)
        
        res = []
        for u, v in queries:
            res.append(v in book[u])
        return res