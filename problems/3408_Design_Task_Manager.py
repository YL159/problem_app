'''
Leetcode 3408. Design Task Manager
Implement a task manager class that:
	Initialize the class object with a list of [userId, taskId, Priority]
    Add a new task with user and priority info. taskId is new to existing tasks
    Edit an existing task with updated priority
    Remove an existing taskId
    Execute the top priority task available. If priority is a tie, execute the largest taskId
		return task userId. If no task available, return -1

Clearly use heap to keep the tasks ordered by (priority, taskId)
Add or edit a task should push the updated task info into the heap
	=> give it a chance to be executed, and we can always skip if invalid
Always update a reference table (dict) of task info (priority and user)
When execute a task, check if the heap top task has valid taskId, priority and user info
'''

from typing import List
import heapq

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        # taskId: (priority, userId) accurate indexing
        self.task = {}
        # min heap of (-priority, -taskId, user) tuple, may contain invalid tasks
        self.hp = []
        for user, t, p in tasks:
            self.hp.append((-p, -t, user))
            self.task[t] = (p, user)
        heapq.heapify(self.hp)
        

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task[taskId] = (priority, userId)
        heapq.heappush(self.hp, (-priority, -taskId, userId))
        

    def edit(self, taskId: int, newPriority: int) -> None:
        _, user = self.task[taskId]
        # push as a new task even same taskId exists in heap
        heapq.heappush(self.hp, (-newPriority, -taskId, user))
        self.task[taskId] = (newPriority, user)
        

    def rmv(self, taskId: int) -> None:
        del self.task[taskId]
        

    def execTop(self) -> int:
        while self.hp:
            p, t, u = heapq.heappop(self.hp)
            # if taskId previously removed, skip
            if -t not in self.task:
                continue
            cur_p, cur_user = self.task[-t]
            # if the task can't match recorded priority or user id, skip
            if p != -cur_p or u != cur_user:
                continue
            # must remove the task index of this exec task
            del self.task[-t]
            return u
        return -1
        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()