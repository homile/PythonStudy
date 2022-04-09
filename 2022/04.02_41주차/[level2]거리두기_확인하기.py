# 거리두기 확인하기
# 링크: https://programmers.co.kr/learn/courses/30/lessons/81302#fn1

# [문제설명]
# 1. 대기실은 5개이며, 각 대기실은 5x5 크기입니다.
# 2. 거리두기를 위하여 응시자들 끼리는 맨해튼 거리가 2이하로 앉지 말아 주세요.
# 3. 단 응시자가 앉아있는 자리 사이가 파티션으로 막혀 있을 경우에는 허용합니다.

# 맨해튼 거리: 
# 두 테이블 T1, T2가 행렬 (r1, c1), (r2, c2)에 각각 위치하고 있다면, 
# T1, T2 사이의 맨해튼 거리는 |r1 - r2| + |c1 - c2| 입니다

# [문제접근]
# P = 응시자가 앉아있는 자리, O는 빈 테이블, X는 파티션
# 한명이라도 거리두기를 지키고 있지 않으면 0, 모두 지키고 있다면 1
# 거리관련 문제이므로 BFS?
# BFS라면 그래프를 그리고 방문노드를 찾아야함
# 찾아낸 후 저거머냐 맨해튼거리 유무를 판단해야함.


# 문제풀이(1)
from collections import deque

# BFS 메서드 정의
def bfs(graph, i, j):
   # 방문 경로를 0으로 구현
   visited = [[0]*5 for _ in range(5)]
	# 큐 구현을 위해 deque 라이브러리 사용
   q = deque()
   q.append((i, j, 0))
	# 현재 노드를 방문 거리
   visited[i][j] = 1
	# 큐가 빌 때 까지 반복
   while q:
		# 큐에서 하나의 원소를 뽑아 출력
      v = q.popleft()
      print(v, end=' ')
      # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
      # for i in graph[v]:
      #    if not visited[i]:
      #       q.append(i)
      #       visited[i] = True
   
   return True


def solution(places):
   queue = deque()
   answer = []

   # graph 그리기
   for place in places:
      for i in range(5):
         for j in range(5):
            if place[i][j] == 'P':
               if not bfs(place, i, j):
                  answer.append(0)

   print(answer)

   return answer


# 다른 사람 문제풀이(1)
from collections import deque

def bfs(p):
    start = []
    
    for i in range(5): # 시작점이 되는 P 좌표 구하기
        for j in range(5):
            if p[i][j] == 'P':
                start.append([i, j])
    
    for s in start:
        queue = deque([s])  # 큐에 초기값
        visited = [[0]*5 for i in range(5)]   # 방문 처리 리스트
        distance = [[0]*5 for i in range(5)]  # 경로 길이 리스트
        visited[s[0]][s[1]] = 1
        
        while queue:
            y, x = queue.popleft()
        
            dx = [-1, 1, 0, 0]  # 좌우
            dy = [0, 0, -1, 1]  # 상하

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<=nx<5 and 0<=ny<5 and visited[ny][nx] == 0:
                    
                    if p[ny][nx] == 'O':
                        queue.append([ny, nx])
                        visited[ny][nx] = 1
                        distance[ny][nx] = distance[y][x] + 1
                    
                    if p[ny][nx] == 'P' and distance[y][x] <= 1:
                        return 0
    return 1

def solution(places):
    answer = []
    
    for i in places:
        answer.append(bfs(i))
    
    return answer

# https://whwl.tistory.com/199
# https://hongcoding.tistory.com/m/124
# https://velog.io/@sem/프로그래머스-LEVEL2-거리두기-확인하기-Python
# https://youtu.be/hCVgKE6qwFs

print(solution(
   [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
   ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
   ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
   ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
   ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))   # [1, 0, 1, 1, 1]