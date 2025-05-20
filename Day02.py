'''
input : 첫 줄에 테스트케이스의 개수 T가 주어진다. T는 최대 1,000,000이다. 다음 T줄에는 각각 두 정수 A와 B가 주어진다. A와 B는 1이상, 1000이하이다.
output : 각 테스트케이스마다 A+B를 한 줄에 하나씩 순서대로 출력한다.

예제)
input : 5
        1 1
        12 34
        5 500
        40 60
        1000 1000
output :2
        46
        505
        100
        2000

*tip : input대신 sys.stdin.readline을 사용할 수 있다.
'''


import sys

T = int(sys.stdin.readline())

for i in range(T):
    l = sys.stdin.readline()
    a, b = map(int, l.split(' '))
    print(a+b)




