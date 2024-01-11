import pytest
from typing import List
from random import randint, sample
'''
A single threaded CPU processing a series of processes/tasks with 0-indexed PIDs. While some task is occupying the CPU,
another task may cut in line because of higher priority, and the current task is pre-empted until that task is done, and thus
resume its CPU time.
Given the total number of tasks n, and a list of CPU logs with format "pid(int):start/stop:time(int)", calculate the respective
total CPU time of each process in the order of increasing PID.
'''

def logProcessing(n:int, logs:List[str]) -> List:
	# record cumulative CPU time of each process
	book = { i:0 for i in range(n)}
	# process on the top of the stack is under processing
	stack = []
	prev = 0
	for log in logs:
		pid, event, t = log.split(':')
		end = event == 'stop'
		pid, t = int(pid), int(t)
		# the process still occupies the ending time frame
		if end:
			t += 1
		if not stack:
			stack.append(pid)
		elif pid == stack[-1]:
			# this process must be ending now
			book[pid] += t - prev
			stack.pop()
		else:
			# a new process pre-empt the current process
			book[stack[-1]] += t - prev
			stack.append(pid)
		prev = t

	return [book[i] for i in range(n)]

def processLogsGen(n:int) -> None:
	# Generate n random legal logs lists. Each represents 1-10 processes
	ns = sorted([randint(1, 10) for i in range(n)])
	for i in ns:
		print(f'Number of prcesses: {i}')
		logs = []
		ts = sorted(sample(range(100), i*2))
		for pid in range(i):
			event = [f'{pid}:start:', f'{pid}:stop:']
			index = randint(0, len(logs))
			logs[index:index] = event
		for j in range(len(ts)):
			logs[j] = logs[j] + str(ts[j])
		print(f'Logs: {logs}\n')

if __name__ == '__main__':
	processLogsGen(5)

def test_case1():
	n = 3
	logs = ['0:start:0', '1:start:4', '1:stop:5', '2:start:7', '2:stop:10', '0:stop:11']
	res = logProcessing(n, logs)
	assert res == [6, 2, 4]
	return

def test_case2():
	n = 4
	logs = ['0:start:15', '0:stop:32', '1:start:35', '3:start:37', '3:stop:45', '1:stop:79', '2:start:81', '2:stop:93']
	res = logProcessing(n, logs)
	assert res == [18, 36, 13, 9]
	return

def test_case3():
	n = 6
	logs = ['2:start:12', '2:stop:27', '3:start:35', '3:stop:36', '0:start:52', '0:stop:53', '1:start:66', '4:start:68', \
		 	'4:stop:71', '5:start:74', '5:stop:84', '1:stop:90']
	res = logProcessing(n, logs)
	assert res == [2, 10, 16, 2, 4, 11]
	return

def test_case4():
	n = 10
	logs = ['0:start:2', '5:start:18', '7:start:22', '7:stop:23', '6:start:27', '9:start:28', '9:stop:32', \
		 	'8:start:33', '8:stop:43', '6:stop:48', '5:stop:49', '4:start:54', '4:stop:55', '2:start:59', '2:stop:70', \
			'1:start:75', '1:stop:86', '3:start:90', '3:stop:94', '0:stop:96']
	res = logProcessing(n, logs)
	assert res == [32, 12, 12, 5, 2, 8, 6, 2, 11, 5]
	return
