'''
input : 첫째 줄에는 영수증에 적힌 총 금액 X가 주어진다
        둘째 줄에는 영수증에 적힌 구매한 물건의 종류의 수 N이 주어진다
        이후 N개의 줄에는 각 물건의 가격 a와 개수 b가 공백을 사이에 두고 주어진다
output : 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하면 yes 출력
         일치하지 않으면 No 출력

예시)
input : 260000
        4
        20000 5
        30000 2
        10000 6
        5000 8
output : Yes
'''

import sys

X = int(sys.stdin.readline())  #총 금액 가져오기
N = int(sys.stdin.readline())  #구매한 물건의 종류 수
T = []

for _ in range(N):
    l = sys.stdin.readline()  #다음 줄 가져오기
    a, b = map(int, l.split(' '))
    T.append(a*b)

if sum(T) == X :
    print('Yes')
else :
    print('No')