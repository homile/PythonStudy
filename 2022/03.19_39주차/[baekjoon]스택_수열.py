# 스택 수열
# 링크: https://www.acmicpc.net/problem/1874

# 문제풀이(1)
n = int(input("숫자를 입력하세요: "))
answer = []
stack = []
count = 1

for i in range(n):
   num = int(input())
   while count <= num:
      stack.append(count)
      count += 1
      answer.append('+')
   if stack[-1] == num:
      stack.pop()
      answer.append('-')
   else:
      print('NO')
      # break
      exit(0)

for i in answer:
   print(i)

# 입력
#  8
#  4
#  3   
#  6
#  8
#  7
#  5
#  2
#  1