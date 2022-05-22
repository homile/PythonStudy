# 입국심사
# 링크: https://programmers.co.kr/learn/courses/30/lessons/43238

# 문제접근
# 사람 6명이 입국 심사를 받아야한다.
# 가장 첫 두 사람은 바로 심사를 받으러 간다. 
# 1번(7분) -> 3번(7분) -> 5번(7분) -> 6번(7분)
# 2번(10분) -> 4번(20분)

# 문제풀이(1)
def solution(n, times):
  answer = 0

  # 최소 시간
  left = min(times)
  # 모든 인원이 최대 시간으로 입국심사를 받을 경우
  right = max(times) * n
  print(left, right)

  
  return answer


print(solution(6, [7, 10]))   # 28