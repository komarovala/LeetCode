# https://leetcode.com/problems/task-scheduler/
from collections import Counter
import heapq
tasks = ["A", "A", "A", "B", "B", "B"]
cnt = Counter(tasks)
idle = 0

task_order = []
used_tasks = {}
lst = []
time = 0

h = []
for key, value in cnt.items():
    heapq.heappush(h, (-value, key))

while h or lst:
    if h:
        task_max = heapq.heappop(h)
        if task_max[1] not in used_tasks:
            used_tasks[task_max[1]] = time + 1
            task_order.append(task_max[1])
            for i in lst:
                heapq.heappush(h, i)
            del lst[:]
            time += 1
            if task_max[0] + 1 < 0:
                heapq.heappush(h, (task_max[0] + 1, task_max[1]))
        elif (time - used_tasks[task_max[1]]) < idle:
            print(f"Diff {time - used_tasks[task_max[1]]}")
            lst.append(task_max)
        else:
            task_order.append(task_max[1])
            used_tasks[task_max[1]] = time + 1
            for i in lst:
                heapq.heappush(h, i)
            del lst[:]
            time += 1
            if task_max[0] + 1 < 0:
                heapq.heappush(h, (task_max[0] + 1, task_max[1]))
    else:
        h = lst
        lst = []
        heapq.heapify(h)
        time += 1


print(task_order, time)




