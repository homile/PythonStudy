# Add Binary
# 링크: https://leetcode.com/problems/add-binary/

# 문제풀이(1)
# bin: 10진수 -> 2진수
# int: 2진수 -> 10진수
# 이렇게 풀어도 되려나????
def solution(a, b):
  a = int(a,2)
  b = int(b,2)
  answer = bin(a + b)[2:]

  return answer

print(solution('11', '1'))    # "100"