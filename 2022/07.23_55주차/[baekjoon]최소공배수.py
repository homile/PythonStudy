# 최소공배수
# 링크: https://www.acmicpc.net/problem/1934

# 문제풀이(1)
# 최대공약수 구하는 라이브러리
from math import gcd
n = int(input())

def lcm(a ,b):
  return a * b // gcd(a, b)

for i in range(n):
  numbers  = list(map(int, input().split(' ')))
  print(lcm(numbers[0], numbers[1]))
  

# input
# 3
# 1 45000
# 6 10
# 13 17

# output
# 45000
# 30
# 221