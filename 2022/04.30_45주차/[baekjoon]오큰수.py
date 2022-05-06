# 오큰수
# 링크: https://www.acmicpc.net/problem/17298

# 문제풀이(1)
# n = int(input())
# a = list(map(int, input().split()))

# # -1로 n만큼 초기값 지정
# big = [-1] * n

# for i in range(n):
#    for j in range(i,n):
#       if a[i] < a[j]:
#          big[i] = a[j]
#          break

# print(*big)

# js에서와 같은 실수 시간초과


# 문제풀이(2)
n = int(input())
a = list(map(int, input().split()))

# -1로 n만큼 초기값 지정
big = [-1] * n

stack = []

for i in range(n):
   while stack and a[stack[-1]] < a[i]:
      print(a[stack[-1]])
      big[stack.pop()] = a[i]
      print(big)
   stack.append(i)

print(*big)
# 3 5 2 7    | 5 7 7 -1