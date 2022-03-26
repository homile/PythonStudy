# 에디터
# 링크: https://www.acmicpc.net/problem/1406

# 문제풀이(1)
# left = list(input())
# right = []
# n = int(input())
# print(left)
# for i in range(n):
#    command = input().split(' ')
#    if command[0] == 'L':
#       if len(left) != 0:
#          right.append(left.pop())
#    elif command[0] == 'D':
#       if len(right) != 0:
#          left.append(right.pop())
#    elif command[0] == 'B':
#       if len(left) != 0:
#          left.pop()
#    elif command[0] == 'P':
#       left.append(command[1])

# print(''.join(left + list(reversed(right))))

# js에서 풀었던데로 풀어봤지만 풀리지 않음
# 시간초과가 났다.
# 이유 문자열은 10만이 최고이지만 명령어는 50만까지 올라가서 그렇다함.


# 문제풀이(2)
import sys
left = list(sys.stdin.readline().rstrip())
right = []
# print(left)

for i in range(int(sys.stdin.readline())):
   command = list(sys.stdin.readline().split())
   print(command)
   if command[0] == 'L':
      if len(left) != 0:
         right.append(left.pop())
   elif command[0] == 'D':
      if len(right) != 0:
         left.append(right.pop())
   elif command[0] == 'B':
      if len(left) != 0:
         left.pop()
   elif command[0] == 'P':
      left.append(command[1])

print(''.join(left + list(reversed(right))))
