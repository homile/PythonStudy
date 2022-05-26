# 입국심사
# 링크: https://programmers.co.kr/learn/courses/30/lessons/43238

# 문제접근
# 사람 6명이 입국 심사를 받아야한다.
# 가장 첫 두 사람은 바로 심사를 받으러 간다. 
# 1번(7분) -> 3번(7분) -> 5번(7분) -> 6번(7분)
# 2번(10분) -> 4번(20분)

# 이분탐색: 중간에서 범위 탐색

# 문제풀이(1)
def solution(n, times):
  answer = 0

  # 최소 시간
  left = min(times)
  # 모든 인원이 최대 시간으로 입국심사를 받을 경우
  right = max(times) * n
  print(left, right)

  while left <= right:
    mid = (left + right) // 2
    check = 0
    for time in times:
      check += mid // time

      if check >= n:
        break
    
    if check >= n:
      answer = mid
      right = mid - 1
    elif check < n:
      left = mid + 1
  
  return answer


print(solution(6, [7, 10]))   # 28


# 참고자료: # https://happy-obok.tistory.com/10