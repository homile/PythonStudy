# 양궁대회
# 링크: https://programmers.co.kr/learn/courses/30/lessons/92342

# [문제설명]
# 어피치와 라이언이 결승전에서 만났는데 전 대회 우승자인 라이언이 불리한 룰이 생김.
# 어피치가 먼저 화살을 쏘고 라이언이 화살을 쏨
# k점을 어피치가 a발 맞히고 라이언이 b발을 맞힐 경우
# 더 많은 화살이 k 점에 맞힌 선수가 점수를 가져가는데 
# a = b일 경우, 어피치가 점수를 가져가며 k점을 여러 발 맞혀도 점수는 한번 줌.
# 최종 점수가 같을 경우 어피치가 우승
# 라이언이 어피치를 가장 큰 점수 차이로 이겨야함.
# 라이언이 지거나 비기면 -1return

# [문제접근]
# 라이언이 가장 큰 점수 차이로 우승할 수 있는 방법이 여러 가지 일 경우, 
# 가장 낮은 점수를 더 많이 맞힌 경우를 return 해주세요.
# 구현문제이다.
# 위의 부분을 볼 때 하나하나 비교해가는 넓이 탐색방법인 BFS일 듯,
# 근데 노드의 개수가 10개로 정리되어 있어서 깊이 탐색방법인 DFS도 가능 할 듯?
# BFS로 어피치보다 라이언이 점수를 많이 받아 이길수 있는 수를 구해야함.
# 이때, 문제설명의 조건처럼 하나하나 해가면 됨.

# BFS/DFS 문제는 많이 어려운 듯 하다.
# 이유? 넓이, 깊이 탐색방법이라는 것과 공식을 알고 있지만
# 조금이라도 대입식이 달라지면 머리가 멈춤. 많이 풀어보고 다시 한번 공부해야함.

# 문제풀이(1)
from collections import deque
def bfs(n, info):
   queue = deque([(0, [0 for i in range(11)])])

   while queue:
      count, arrow = queue.popleft()
      score_board = arrow
      for i in range(11):
         score_board[count] = info[count] + 1
         print(count, arrow, score_board)

   return True


def solution(n, info):
    answer = []
    score = bfs(n, info)

    print(score)
    return answer


# 문제풀이(2)
maxScore = 0
maxList = []
# 화살을 쏜 경우의 수 계산
def dfs(n, info, index, lion_score_board):
   if n == 0:
      # print(lion_score_board)
      global maxScore, maxList
      lion_score, apeach_score = 0, 0

      for i in range(11):
         # print(lion_socre, apeach_score)
         if info[i] == 0 and lion_score_board[i] == 0:
            continue

         if lion_score_board[i] > info[i]:
            # i = 0부터시작 idex num = 0 = 10점
            lion_score += 10 - i
         else:
            apeach_score += 10 - i

      if lion_score > apeach_score:
         diff = lion_score - apeach_score
         if diff > maxScore:
            # print(lion_socre, lion_score_board)
            maxScore = lion_score
            # print(lion_score_board)
            maxList = list(lion_score_board)
      

   # 0~10까지의 11개의 점수가 존재
   if index == 11: 
      return True

   apeach = info[index]
   for i in range(apeach+2):
      if n >= i:
         lion_score_board[index] = i
         # 쏜 화살을 개수 빼기, 다음 번호 + 1
         dfs(n-i, info, index+1, lion_score_board)
         lion_score_board[index] = 0
   # print(lion_score_board)


def solution(n, info):
    answer = []
    index = 0
    lion_score_board = [0 for i in range(11)]
    score = dfs(n, info, index, lion_score_board)

    print(score, maxScore, maxList)
    answer = maxList
    return answer



# 다른 사람의 풀이들
# https://velog.io/@hygge/Python-프로그래머스-양궁대회-2022-KAKAO-BLIND-RECRUITMENT-BFS
# https://tech.kakao.com/2022/01/14/2022-kakao-recruitment-round-1/
# https://velog.io/@jadenkim5179/프로그래머스-양궁대회
# https://yensr.tistory.com/m/24


print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))     # [0,2,2,0,1,0,0,0,0,0,0]
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))     # [-1]