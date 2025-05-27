'''
input : 첫째 줄에 수의 개수 N이 주어진다.
        둘째 줄부터 N개의 줄에는 수가 주어진다.
        이 수는 절댓값이 1000보다 작거나 같은 정수이다.
        수는 중복되지 않는다.
output : 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

예제)
input : 5
        5
        2
        3
        4
        1
output : 1
         2
         3
         4
         5
'''

import sys

num = int(sys.stdin.readline())
a = []

for _ in range(num):
    b = a.append(int(sys.stdin.readline()))
    
a.sort()

for i in a:
    print(i)