# Climbing Stairs
# 링크: https://leetcode.com/problems/climbing-stairs/

# [문제접근]
# 피보나치수인듯 하다.

# 문제풀이(1)
def solution(n):
  # DP
  # 피보나치 수열 문제
  dp = [0]*(n+1)
  
  for i in range(1, n+1):
    if i == 1 or i == 2: 
      dp[i] = i
    else:
      dp[i] = dp[i-2] + dp[i-1]
  
  return dp[n]

print(solution(2))  # 2
print(solution(3))  # 3
print(solution(5))  # 8