# 알고리즘 스택
# 링크: https://www.acmicpc.net/problem/10828

# [문제]
# 정수를 저장하는 스택을 구현한 다음, 
# 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# 명령은 총 다섯 가지이다.

# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 
# 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 
# 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# [입력]
# 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 
# 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 
# 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 
# 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

# [출력]
# 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

# [문제접근]
# push 12 -> list.append(12)
# pop -> pop() or len(list) == 0: return -1
# size -> len(list)
# empty -> if len(list) == 0: return 1 else: return 0
# top -> if len(list) != 0: return list[-1] else: return -1

# 첫째 줄은 명령의 수를 int(input())으로 받아오고
# for문을 사용해 명령의 수 만큼 값을 받아오는 list를 생성


# 문제풀이(1)
a = int(input())
result = []

for i in range(a):
    command = input().split()
    
    if command[0] == "push":
        result.append(command[1])

    elif command[0] == "pop":
        if len(result) == 0:
            print(-1)
        else:
            print(command.pop())

    elif command[0] == "size":
        print(len(result))

    elif command[0] == "empty":
        if len(result) == 0:
            print(1)
        else:
            print(0)

    elif command[0] == "top":
        if len(result) == 0:
            print(-1)
        else:
            print(result[-1])

# 조건문에 다시 맞게 != 대신 == 을 사용해보자
# pop명령어를 입력할 경우 pop이 출력됨
# 이유를 알기까지 얼마 걸리지 않음 -> result.pop을 해야하는데 command에서 함
# 바꿔도 시간초과 났음
# 이유
# 입출력 속도 비교 : sys.stdin.readline > raw_input() > input()


# 문제풀이(2)
# import sys
# a = int(sys.stdin.readline())
a = int(input())
result = []

for i in range(a):
    # command = sys.stdin.readline().split()
    command = input().split()
    
    if command[0] == "push":
        result.append(command[1])

    elif command[0] == "pop":
        if len(result) == 0:
            print(-1)
        else:
            print(result.pop())

    elif command[0] == "size":
        print(len(result))

    elif command[0] == "empty":
        if len(result) == 0:
            print(1)
        else:
            print(0)

    elif command[0] == "top":
        if len(result) != 0:
            print(result[-1])
        else:
            print(-1)

# 입력
# 14
# push 1
# push 2
# top
# size
# empty
# pop
# pop
# pop
# size
# empty
# pop
# push 3
# empty
# top