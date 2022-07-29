# 소수 찾기
# 링크: https://www.acmicpc.net/problem/1978

# 문제풀이(1)
# 판별할 수의 개수
n = int(input())

# 판별할 수들
numbers = list(map(int, input().split(' ')))
print(numbers)

answer = 0
for i in numbers:
  result = 0
  if i > 1:
    for j in range(2, i):
      if i % j == 0:
        result += 1
  
    if result == 0:
      answer += 1

print(answer)