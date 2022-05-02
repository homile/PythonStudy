# 오등큰수
# 링크: https://www.acmicpc.net/problem/17299

# [문제접근]
# 오른쪽으로 진행할 때 자신보다 많이 나온 숫자로 변환한다.

# 문제풀이(1)
# n = int(input())

# # -1로 n만큼 채운 배열을 하나 만든다.
# result = ['-1' for i in range(n)]
# # print(result)

# # 입력 값을 받아온다.
# stack = list(map(int, input().split()))
# print(stack)

# for i in range(n):
#    for j in range(i, len(stack)):
#       # print(stack.count(stack[i]), stack.count(stack[j]))
#       if stack.count(stack[i]) < stack.count(stack[j]):
#          result[i] = str(stack[j])
#          break
   
# print(result)  
# print(' '.join(result))

# 시간초과 -> 2중 for문?


# 문제풀이(2)
n = int(input())

# -1로 n만큼 채운 배열을 하나 만든다.
result = ['-1' for i in range(n)]

# 입력 값을 받아온다.
stack = list(map(int, input().split()))

for i in range(n):
   for j in range(i, len(stack)):
      if stack.count(stack[i]) < stack.count(stack[j]):
         result[i] = str(stack[j])
         break
   
print(' '.join(result))



# 7
# 1 1 2 3 4 2 1
# result: -1 -1 1 2 2 1 -1