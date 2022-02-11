# 게임 맵 최단거리

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/1844
# 적진으로 가는 최단거리를 구하는 문제
# maps는 n x m 크기의 게임 맵의 상태가 들어가 있는 2차원 배열
# 0은 벽이 있는 자리, 1은 벽이 없는 자리
# 적진 -> n x m 의 우측하단 끝자리

# 백준 온라인 저지 2178번과 똑같은 문제

# 문제접근
# 경로 탐색 방법중 하나인 BFS를 사용해야 하는가?
# 2차원 배열을 구체적으로 풀어서 해봐야 할 듯
# 동,서,남,북으로 이동을 어떻게 하지?
# 갈림길을 어떻게 가지?

# 문제풀이(1)
from collections import deque

def solution(maps):
    answer = 0

    n = len(maps)
    m = len(maps[0])

    queue = deque([[0,0]])    # 시작노드 설정

    print(queue)

    # for i in range(n):
    #     for j in range(m):
            # print(maps[j][i])

    # BFS 공식?
    # while queue:
	# 	# 큐에서 하나의 원소를 뽑아 출력
	# 	v = queue.popleft()
	# 	print(v, end=' ')
	# 	# 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
	# 	for i in graph[v]:
	# 		if not visited[i]:
	# 			queue.append(i)
	# 			visited[i] = True
            
    return answer

# BFS로 풀어야 한다는 것 까지는 생각했지만
# 공식을 적용하지 못했다.
# 동, 서, 남, 북으로 갈 수 있는 경우는 어떻게 알아내는가?
# 위의 문제가 가장 시급했다.


# 문제풀이(2)
from collections import deque

def solution(maps):
    answer = 0

    n = len(maps)       # y축
    m = len(maps[0])    # x축

    graph = [[-1 for _ in range(m)] for _ in range(n)]  # n x m 크기의 -1로 채워진 리스트
    graph[0][0] = 1     # 시작지점 표시
    print(graph)

    queue = deque([[0,0]])    # 시작노드 설정
    # print(queue)

    dx,dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상, 하, 좌, 우 이동하기 위한 리스트

    # BFS 공식
    while queue:    # queue가 빌 때까지 반복
        y, x = queue.popleft()

        # 현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # print(i, nx, x, dx[i])
            # print(i, ny, y, dy[i])
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] == 1:   # 행과 열의 길이를 벗어나지 않으면서 상하좌우의 값이 1인경우 실행
                if graph[ny][nx] == -1:                 # 임의로 만들어둔 그래프의 [ny][nx]의 값이 -1이면 실행
                    graph[ny][nx] = graph[y][x] + 1     # 지나간 자리에 +1
                    # print(ny, nx)
                    queue.append([ny, nx])
                    # print(i, queue, graph)
                    # print(graph)
                    # print(queue)
    answer = graph[-1][-1]
            
    return answer

# 참고사이트: https://jokerldg.github.io/algorithm/2021/05/23/game-map.html
# 참고노션: https://www.notion.so/DFS-BFS-fce1f228d83f407a98c67ca9a6768dbe 

# 11
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
# -1
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))


# 다른 사람의 풀이(1)
def solution(maps):
    pos_stack = [(0,0,1)] # (x,y,d)

    maps[0][0] = -1
    n = len(maps) # x
    m = len(maps[0]) # y

    while pos_stack:
        x,y,d = pos_stack.pop(0)
        if y-1 >=0:
            # go to top
            if maps[x][y-1] ==1 or maps[x][y-1] > d+1:
                maps[x][y-1] = d+1
                if x==n-1 and y-1==m-1:
                    return d+1
                pos_stack.append((x,y-1,d+1))
        if x-1 >=0:
            # go to left
            if maps[x-1][y] ==1 or maps[x-1][y] > d+1:
                maps[x-1][y] = d+1
                if x-1==n-1 and y==m-1:
                    return d+1
                pos_stack.append((x-1,y,d+1))
        if x+1<n:
            # go to right
            if maps[x+1][y] ==1 or maps[x+1][y] > d+1:
                maps[x+1][y] = d+1
                if x+1==n-1 and y==m-1:
                    return d+1
                pos_stack.append((x+1,y,d+1))
        if y+1<m:
            # go to bottom
            if maps[x][y+1] ==1 or maps[x][y+1] > d+1:
                maps[x][y+1] = d+1
                if x==n-1 and y+1==m-1:
                    return d+1
                pos_stack.append((x,y+1,d+1))


    result = maps[n-1][m-1]
    if result ==1:
        return -1
    else:
        return result

# 상, 하, 좌, 우의 비교법을 for문이 아닌 if문으로 나열해둠 이해하기 편함

# 11
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
# -1
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))