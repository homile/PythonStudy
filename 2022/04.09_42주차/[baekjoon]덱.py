# 덱 (10866번)
# 링크: https://www.acmicpc.net/problem/10866

# 문제풀이(1)
import sys
from collections import deque

n = int(sys.stdin.readline())

de = deque()

for i in range(n):
   command = sys.stdin.readline().split()

   if command[0] == 'push_front':
      de.appendleft(command[1])
   elif command[0] == 'push_back':
      de.append(command[1])
   elif command[0] == 'pop_front':
      if len(de) != 0:
         print(de.popleft())
      else:
         print(-1)
   elif command[0] == 'pop_back':
      if len(de) != 0:
         print(de.pop())
      else:
         print(-1)
   elif command[0] == 'size':
      print(len(de))
   elif command[0] == 'empty':
      if len(de) != 0:
         print(0)
      else:
         print(1)
   elif command[0] == 'front':
      if len(de) != 0:
         print(de[0])
      else:
         print(-1)
   elif command[0] == 'back':
      if len(de) != 0:
         print(de[-1])
      else:
         print(-1)



# '15'
# 'push_back 1'
# 'push_front 2'
# 'front'
# 'back'
# 'size'
# 'empty'
# 'pop_front'
# 'pop_back'
# 'pop_front'
# 'size'
# 'empty'
# 'pop_back'
# 'push_front 3'
# 'empty'
# 'front'