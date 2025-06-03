'''
input : 첫째 줄에 로그에 기록된 출입 기록의 수 n이 주어진다
        다음 n개의 줄에는 출입 기록이 순서대로 주어지며, 각 사람이름+"enter or leave"가 주어진다
        enter는 출근, leave는 퇴근
        회사에는 동명이인이 없으며 대소문자가 다른 경우에는 다른 이름이다.
output : 현재 회사에 있는 사람의 이름을 사전 순의 역순으로 한 줄에 한 명씩 출력한다 
'''
import sys

n = int(sys.stdin.readline())
s = set()

for i in range(n):
    a = list(map(str, sys.stdin.readline().strip().split(' ')))
    if a[1] == "enter":
        s.add(a[0])
    elif a[1] == "leave":
        s.remove(a[0])

s = sorted(s, reverse=True)

for i in s:
    print(i)

'''
**시간초과나옴**
import sys

n = int(sys.stdin.readline())
q = []

for i in range(n):
    a = list(map(str, sys.stdin.readline().strip().split(' ')))
    if a[1] == "enter":
        q.append(a[0])
    elif a[1] == "leave":
        q.remove(a[0])

q.sort(reverse=True)

for i in q:
    print(i)
'''