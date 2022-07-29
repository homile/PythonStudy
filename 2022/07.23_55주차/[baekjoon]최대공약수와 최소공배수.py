# 최대공약수와 최소공배수
# 링크: https://www.acmicpc.net/submit/2609/43385538

# 문제풀이(1)
numbers  = list(map(int, input().split(' ')))
# numberMax = max(numbers)
# numberMin = min(numbers)

# print(numberMax, numberMin)
def gcd(a, b):
  while b > 0:
    a, b = b, a % b
  return a

print(gcd(numbers[0], numbers[1]))

def lcm(a, b):
  return a * b / gcd(a, b)

print(int(lcm(numbers[0], numbers[1])))


# input
# 24 18

# output
# 6
# 72