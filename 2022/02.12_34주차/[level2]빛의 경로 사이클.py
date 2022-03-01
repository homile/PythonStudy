# 빛의 경로 사이클

# 링크: https://programmers.co.kr/learn/courses/30/lessons/86052

# [문제 설명]
# 각 칸마다 S, L, 또는 R가 써져 있는 격자가 있습니다. 
# 당신은 이 격자에서 빛을 쏘고자 합니다. 
# 이 격자의 각 칸에는 다음과 같은 특이한 성질이 있습니다.

# 빛이 "S"가 써진 칸에 도달한 경우, 직진합니다.
# 빛이 "L"이 써진 칸에 도달한 경우, 좌회전을 합니다.
# 빛이 "R"이 써진 칸에 도달한 경우, 우회전을 합니다.
# 빛이 격자의 끝을 넘어갈 경우, 반대쪽 끝으로 다시 돌아옵니다. 
# 예를 들어, 빛이 1행에서 행이 줄어드는 방향으로 이동할 경우, 
# 같은 열의 반대쪽 끝 행으로 다시 돌아옵니다.
# 당신은 이 격자 내에서 빛이 이동할 수 있는 경로 사이클이 몇 개 있고, 
# 각 사이클의 길이가 얼마인지 알고 싶습니다. 
# 경로 사이클이란, 빛이 이동하는 순환 경로를 의미합니다.

# 예를 들어, 다음 그림은 격자 ["SL","LR"]에서 1행 1열에서 2행 1열 방향으로 빛을 쏠 경우,
#  해당 빛이 이동하는 경로 사이클을 표현한 것입니다.

# ex1.png

# 이 격자에는 길이가 16인 사이클 1개가 있으며, 다른 사이클은 존재하지 않습니다.

# 격자의 정보를 나타내는 1차원 문자열 배열 grid가 매개변수로 주어집니다. 
# 주어진 격자를 통해 만들어지는 빛의 경로 사이클의 모든 길이들을 배열에 담아 
# 오름차순으로 정렬하여 return 하도록 solution 함수를 완성해주세요.

# [제한사항]
# 1 ≤ grid의 길이 ≤ 500
# 1 ≤ grid의 각 문자열의 길이 ≤ 500
# grid의 모든 문자열의 길이는 서로 같습니다.
# grid의 모든 문자열은 'L', 'R', 'S'로 이루어져 있습니다.

# [문제접근]
# 경로를 탐색하는 문제이기 때문에 BFS/DFS를 사용한 문제일 듯 하다.
# 적에게로 향하는 방식의 문제(게임맵 최단거리)와 비슷하게 풀면될듯?
# https://westmino.tistory.com/86

# 문제풀이(1)
dx = [1,0,-1,0]
dy = [0,-1,0,1]

def solution(grid):
    global visited,n,m
    n = len(grid)
    m = len(grid[0])
    answer = []
    visited = [[[False]*4 for _ in range(m)] for _ in range(n)]
    for sx in range(n):
        for sy in range(m):
            for d in range(4):
                if not visited[sx][sy][d]:
                    rst = simul(sx,sy,d,grid)
                    if rst != 0:
                        answer.append(rst)
    answer.sort()
    return answer

def simul(sx,sy,sd,grid):
    global visited
    x,y,d=sx,sy,sd
    cnt = 0
    visited[sx][sy][sd] = True
    while True:
        x = (x + dx[d]) % n
        y = (y + dy[d]) % m
        cnt += 1

        if grid[x][y] == 'R':
            d = (d+1)%4
        elif grid[x][y] == 'L':
            d = (d-1)%4
        if visited[x][y][d]:
            if (x,y,d) == (sx,sy,sd):
                return cnt
            else:
                return 0
        visited[x][y][d] = True

print(solution(["SL","LR"]))    # [16]
print(solution(["S"]))          # [1,1,1,1]
print(solution(["R","R"]))      # [4,4]