'''
input : 첫째 줄에 행렬의 크기 N과 M이 주어진다
        둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다.
        이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다.
        N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작은 정수이다.
output : 첫째 줄부터 N개의 줄에 행렬 A와 B를 더한 행렬을 출력한다
         행렬의 각 원소는 공백으로 구분한다. 

예제)
input : 3 3
        1 1 1
        2 2 2
        0 1 0
        3 3 3
        4 4 4
        5 5 100
output : 4 4 4
         6 6 6
         5 6 100
'''

import sys

matrix = list(map(int, sys.stdin.readline().split(' ')))
N, M = matrix[0], matrix[1]

A = []
B = []
output = []

for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split(' '))))
for _ in range(N):
    B.append(list(map(int, sys.stdin.readline().split(' '))))

for i in range(N):
    row = []
    for j in range(M):
        row.append(A[i][j] + B[i][j])
    output.append(row)

for row in output:
    print(*row)




