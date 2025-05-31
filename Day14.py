'''
input : 첫째 줄에 주어지는 명령의 수 N이 주어진다.
        둘째 주부터 N개의 줄에는 명령이 하나씩 주어진다.
        주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다.
        문제에 나와있지 않은 명령이 주어지는 경우는 없다.
output : 출력해야하는 명령이 주어질때마다, 한 줄에 하나씩 출력한다.

push X = 정수 X를 큐에 넣는 연산
pop = 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다
size = 큐에 들어있는 정수의 개수를 출력한다
empty = 큐가 비어있으면 1, 아니면 0을 출력한다
front = 큐의 가장 앞에있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다
back = 큐의 가장 뒤에있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다
'''

import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque()

for _ in range(N):
    a = sys.stdin.readline().strip().split(' ')
    if a[0] == "push":
        queue.append(a[1])
        continue
    elif a[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
        continue
    elif a[0] == "size":
        print(len(queue))
        continue
    elif a[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
        continue
    elif a[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
        continue
    elif a[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
        continue