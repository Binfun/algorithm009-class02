import queue
from collections import deque
q = queue.Queue()

for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get())

d = deque()
for i in range(5):
    d.append(i)

while d:
    print(d.popleft())
