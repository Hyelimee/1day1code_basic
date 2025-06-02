'''
input : 첫째 줄에 명령의 수 N이 주어진다
        둘째 줄부터 N개 줄에 명령이 하나씩 주어진다
        출력을 요구하는 명령은 하나 이상 주어진다
output : 출력을 요구하는 명령이 주어질 때마다 명령의 결과를 한 줄에 하나씩 출력한다.

1x : 정수 X를 덱의 앞에 넣는다
2x : 정수 x를 덱의 뒤에 넣는다
3 : 덱에 정수가 있다면 맨 앞의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다
4 : 덱에 정수가 있다면 맨 뒤의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다
5 : 덱에 들어있는 정수의 개수를 출력한다
6 : 덱이 비어있으면 1, 아니면 0을 출력한다
7 : 덱에 정수가 있다면 맨 앞의 정수를 출력한다. 없다면 -1을 대신 출력한다
8 : 덱에 정수가 있다면 맨 뒤의 정수를 출력한다. 없다면 -1을 대신 출력한다
'''
import sys
from collections import deque

N = int(sys.stdin.readline())
dq = deque()

for i in range(N):
    a = list(map(int, sys.stdin.readline().strip().split(' ')))
    if a[0] == 1:
        dq.appendleft(a[1])
    elif a[0] == 2:
        dq.append(a[1])
    elif a[0] == 3:
        if  len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())
    elif a[0] == 4:
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.pop())
    elif a[0] == 5:
        print(len(dq))
    elif a[0] == 6:
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == 7:
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    elif a[0] == 8:
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])
