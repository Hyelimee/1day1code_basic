'''
input : 첫째 줄에 자연수 N이 주어진다
        다음 줄에는 N개의 정수가 주어진다(A[1], A[2], ..., A[N])
        다음 줄에는 M개의 수가 주어진다
        다음 줄의 수 들이 A안에 존재하는지 알아낸다
output : M개의 줄에 답을 출력한다. 존재하면 1, 존재하지 않으면 0을 출력한다.
'''

import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))


for b in B:
    if b in A:
        print(1)
    else:
        print(0)