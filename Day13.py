'''
input : 첫째 줄에 주어지는 명령의 수 N이 주어진다.
        둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다.
        주어지는 정수는 1보다 크거나 같고 100,000보다 작거나 같다.
        문제에 나와있지 않은 명령이 주어지는 경우는 없다.
output : 출력해야하는 명령이 주어질 때마다, 한줄에 하나씩 출력한다.

pushX=정수X를 스택에 넣는 연산
pop=스택에서 가장 위에 있는 정수를 빼고 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size=스택에 들어있는 정수의 개수를 출력한다
empty=스택이 비어있으면 1, 아니면 0을 출력한다
top=스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다
'''
import sys

N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    a = list(sys.stdin.readline().strip().split(' ')) #strip으로 줄바꿈 제거

    if a[0] == "push":
        stack.append(a[1])
        continue
    elif a[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
        continue
    elif a[0] == "size":
        print(len(stack))
        continue
    elif a[0] == "empty":
        if len(stack) == 0:
            print(1)
        else :
            print(0)
        continue
    elif a[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:    
            print(stack[-1])
        continue
