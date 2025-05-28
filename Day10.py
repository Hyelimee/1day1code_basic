'''
input : 첫째 줄부터 다섯째 줄까지 한 줄에 하나씩 자연수가 주어진다.
        주어지는 자연수는 100보다 작은 10의 배수이다.
output : 첫째 줄에는 평균을 출력하고, 둘째 줄에는 중앙값을 출력한다.
         평균과 중앙값은 모두 자연수이다.

예제)
input : 10
        40
        30
        60
        30
output : 34
         30
'''

import sys
from statistics import mean

a = []

for i in range(5):
    b = int(sys.stdin.readline())
    a.append(b)

a.sort()

print(mean(a))
print(a[2])