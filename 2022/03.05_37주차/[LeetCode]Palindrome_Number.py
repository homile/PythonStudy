# Palindrome Number
# 링크: https://leetcode.com/problems/palindrome-number/

# [문제]
# 정수가 주어지면 회문 정수인 경우 x를 반환 합니다.truex

# 정수는 정방향과 역방향이 같을 때 회문 입니다.

# 예를 들어 121는 회문이고 123는 그렇지 않습니다.

# [문제접근]
# 주어진 정수와 reverse했을 때의 값이 같을 때 true를 반환하고
# 다를 경우 false를 반환한다.

# 문제풀이(1)
def solution(x):
   x = str(x)
   if x == x[::-1]:
      return True
   else:
      return False

print(solution(121))    # true
print(solution(-121))   # false
print(solution(10))     # false