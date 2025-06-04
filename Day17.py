'''
input : 첫째 줄에 상근이가 가지고있는 숫자카드 개수 N이 주어진다
        둘째 줄에 숫자카드에 적혀있는 정수가 주어진다. -10,000,000~10,000,000, 중복없음
        셋째 줄에 M이 주어진다
        넷째 줄에 상근이가 가지고 있는 카드인지 아닌지 구해야할 M개의 정수가 주어진다
output : 첫째 줄에 입력으로 주어진 M개의 수에 대해서 
         각 수가 적힌 숫자 카드를 상근이가 가지고 있으면 1, 아니면 0 출력
''' 

import sys

N = int(sys.stdin.readline())  #상근이가 가지고있는 숫자 카드 수

num_card = set(map(int, sys.stdin.readline().split(' ')))
#print(num_card)

M = int(sys.stdin.readline())  #상근이가 맞춰야하는 카드 수

card = list(map(int, sys.stdin.readline().split(' ')))
#print(card)

ans = []

for i in range(M):
    if card[i] in num_card:
        ans.append(1)
    else:
        ans.append(0)
print(*ans)

'''
**시간초과**
import sys

N = int(sys.stdin.readline())  #상근이가 가지고있는 숫자 카드 수

num_card = list(map(int, sys.stdin.readline().split(' ')))
#print(num_card)

M = int(sys.stdin.readline())  #상근이가 맞춰야하는 카드 수

card = list(map(int, sys.stdin.readline().split(' ')))
#print(card)

ans = []

for i in range(M):
    if card[i] in num_card:
        ans.append(1)
    else:
        ans.append(0)
print(*ans)
'''