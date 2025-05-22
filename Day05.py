'''
input : 첫째 줄에 정수의 개수 N이 주어진다.
        둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다
        모든 정수는 -1000000보다 크거나 같고 1000000보다 작거나 같은 정수이다
output : 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다

예시)
input : 5
        20 10 35 30 7
output : 7 35
'''

import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split(' ')))
#num = [int(i) for i in num]  #map 말고, list comprehension
#print(num)

a, b = min(num), max(num)
print(f"{a} {b}")