# 배달

# 링크: https://programmers.co.kr/learn/courses/30/lessons/12978

# [문제 설명]
# N개의 마을로 이루어진 나라가 있습니다. 
# 이 나라의 각 마을에는 1부터 N까지의 번호가 각각 하나씩 부여되어 있습니다. 
# 각 마을은 양방향으로 통행할 수 있는 도로로 연결되어 있는데, 
# 서로 다른 마을 간에 이동할 때는 이 도로를 지나야 합니다. 
# 도로를 지날 때 걸리는 시간은 도로별로 다릅니다. 
# 현재 1번 마을에 있는 음식점에서 각 마을로 음식 배달을 하려고 합니다. 
# 각 마을로부터 음식 주문을 받으려고 하는데, 
# N개의 마을 중에서 K 시간 이하로 배달이 가능한 마을에서만 주문을 받으려고 합니다. 
# 다음은 N = 5, K = 3인 경우의 예시입니다.

# 배달_1_uxun8t.png

# 위 그림에서 1번 마을에 있는 음식점은 [1, 2, 4, 5] 번 마을까지는 
# 3 이하의 시간에 배달할 수 있습니다. 
# 그러나 3번 마을까지는 3시간 이내로 배달할 수 있는 경로가 없으므로 
# 3번 마을에서는 주문을 받지 않습니다. 
# 따라서 1번 마을에 있는 음식점이 배달 주문을 받을 수 있는 마을은 4개가 됩니다.
# 마을의 개수 N, 각 마을을 연결하는 도로의 정보 road, 
# 음식 배달이 가능한 시간 K가 매개변수로 주어질 때, 
# 음식 주문을 받을 수 있는 마을의 개수를 return 하도록 solution 함수를 완성해주세요.

# [제한사항]
# 마을의 개수 N은 1 이상 50 이하의 자연수입니다.
# road의 길이(도로 정보의 개수)는 1 이상 2,000 이하입니다.
# road의 각 원소는 마을을 연결하고 있는 각 도로의 정보를 나타냅니다.
# road는 길이가 3인 배열이며, 순서대로 (a, b, c)를 나타냅니다.
# a, b(1 ≤ a, b ≤ N, a != b)는 도로가 연결하는 두 마을의 번호이며, 
# c(1 ≤ c ≤ 10,000, c는 자연수)는 도로를 지나는데 걸리는 시간입니다.
# 두 마을 a, b를 연결하는 도로는 여러 개가 있을 수 있습니다.
# 한 도로의 정보가 여러 번 중복해서 주어지지 않습니다.
# K는 음식 배달이 가능한 시간을 나타내며, 1 이상 500,000 이하입니다.
# 임의의 두 마을간에 항상 이동 가능한 경로가 존재합니다.
# 1번 마을에 있는 음식점이 K 이하의 시간에 배달이 가능한 마을의 개수를 
# return 하면 됩니다.

# [문제접근]
# 최단거리를 찾는 문제이기 때문에 BFS or 다익스트라 or 플로이드 워셜 알고리즘 사용
# 이렇게 노드끼리 연결되어 있는 문제는 다익스트라 알고리즘으로 풀 수 있다.
# 노드와 노드를 잇는 그래프를 생성해야한다.

# road[0], road[1] = 노드가 이어진 마을 번호
# road[2] = 도로를 지나는데 걸리는 시간

# 1 -> 2로 가는 시간 1 가능, 1 -> 2 -> 3으로 가는 시간 1 + 3 불가능
# 1 -> 4로 가는 시간 2 가능, 1 -> 2 -> 5로 가는 시간 1 + 2 가능
# 1 -> 4 -> 5로 가는 시간 2 + 2 불가능
# 1 -> 2 -> 5 -> 3으로 가는 시간 1 + 2 + 1 불가능

# 간선의 수를 더해서 k보다 크다면 불가능
# 시작은 1번 무조건 1번 노드에서 시작한다?
# 1은 자기 자신이기 때문에 포함
# 배달할 수 있는 지역 1번, 2번, 4번, 5번 = 총 4개의 마을

# 문제풀이(1)
import heapq  # 우선순위 큐 구현을 위함

def dijkstra(distance, graph):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, 1))
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return q

def solution(N, road, K):
    answer = 0

    INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정
    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = [INF] * (N + 1)

    graph = [[] for _ in range(N+1)]
    # a, b = 마을번호 | c = 걸리는 시간
    for a, b ,c in road:
        graph[a].append([b, c])
        graph[b].append([a, c])

    print(graph)
    print(dijkstra(distance, graph))

    return answer

# 다익스트라 알고리즘을 적용이 쉽지 않음.


# 문제풀이(2)
import heapq  # 우선순위 큐 구현을 위함

# 큐에 값이 없을때 까지 돌기위해 return을 제외
def dijkstra(distance, graph):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, 1))
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        print(dist, now, q)
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for b, c in graph[now]:
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            print(distance[b], dist+c)
            if dist+c < distance[b]:    # 간선의 값이 무한이 아닐 경우
                distance[b] = dist+c    # a마을에서 b마을로 가는 거리 계산
                heapq.heappush(q, (dist+c, b))


def solution(N, road, K):
    answer = 0

    INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정
    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = [INF] * (N + 1)
    distance[1] = 0

    graph = [[] for _ in range(N+1)]
    # a, b = 마을번호 | c = 걸리는 시간
    for a, b ,c in road:
        graph[a].append([b, c])
        graph[b].append([a, c])

    # print(graph)
    print("변경전 ", distance)
    dijkstra(distance, graph)
    print("변경후 ", distance)

    return answer

# 다익스트라 알고리즘 적용완료


# 문제풀이(3)  46.9점
import heapq  # 우선순위 큐 구현을 위함

# 큐에 값이 없을때 까지 돌기위해 return을 제외
def dijkstra(distance, graph):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    # 0 = 시작노드로 가기 위한 최단 경로, 1 = 시작 노드
    heapq.heappush(q, (0, 1))
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for b, c in graph[now]:
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            # print(distance[b], dist+c)
            if dist+c < distance[b]:    # 간선의 값이 무한이 아닐 경우
                distance[b] = dist+c    # a마을에서 b마을로 가는 거리 계산
                heapq.heappush(q, (dist+c, b))


def solution(N, road, K):
    answer = 1

    INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정
    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = [INF] * (N + 1)
    distance[1] = 0

    graph = [[] for _ in range(N+1)]
    # a, b = 마을번호 | c = 걸리는 시간
    for a, b ,c in road:
        graph[a].append([b, c])
        graph[b].append([a, c])

    # print(graph)
    # print("변경전 ", distance)
    dijkstra(distance, graph)
    print("변경후 ", distance)

    for i in distance:
        if i != INF and i < K:
            answer += 1

    return answer

# 깔끔하게 정리해서 다시 한번 볼것 어딘가에 코드가 길어지는 듯


# 문제풀이(4)  
import heapq  # 우선순위 큐 구현을 위함

# 큐에 값이 없을때 까지 돌기위해 return을 제외
def dijkstra(distance, graph):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    # 0 = 시작노드로 가기 위한 최단 경로, 1 = 시작 노드
    heapq.heappush(q, (0, 1))
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for b, c in graph[now]:
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist+c < distance[b]:    # 간선의 값이 무한이 아닐 경우
                distance[b] = dist+c    # a마을에서 b마을로 가는 거리 계산
                heapq.heappush(q, (dist+c, b))

def solution(N, road, K):
    answer = 0

    INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정
    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = [INF] * (N + 1)
    distance[1] = 0

    graph = [[] for _ in range(N+1)]
    # a, b = 마을번호 | c = 걸리는 시간
    for a, b ,c in road:
        graph[a].append([b, c])
        graph[b].append([a, c])

    dijkstra(distance, graph)

    for i in distance:
        if i <= K:
            answer += 1

    return answer

# 가장 쉬운 에러를 발생했다.
# 방문할 수 있는 집의 개수를 카운트 하는 부분에서 
# 무한이하를 가르켜야 비교했기 때문이다.
# 사실 무한이하는 i <=K로 하면 비교를 1번만 하면 되기 때문이다.
# 그래서 처음 시작노드를 합하여 계산하기위해 answer = 1을 0으로 변경했다.

# 4
print(solution(5, 
[[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))

# 4
print(solution(6, 
[[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4))   