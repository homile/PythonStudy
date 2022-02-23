# 전력망 둘로 나누기

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/86971
# n개의 송전탑이 전선을 통해 하나의 트리 형태로 연결되어 있습니다. 
# 당신은 이 전선들 중 하나를 끊어서 현재의 전력망 네트워크를 2개로 분할하려고 합니다. 
# 이때, 두 전력망이 갖게 되는 송전탑의 개수를 최대한 비슷하게 맞추고자 합니다.

# 송전탑의 개수 n, 그리고 전선 정보 wires가 매개변수로 주어집니다. 
# 전선들 중 하나를 끊어서 송전탑 개수가 가능한 비슷하도록 두 전력망으로 나누었을 때, 
# 두 전력망이 가지고 있는 송전탑 개수의 차이(절대값)를 
# return 하도록 solution 함수를 완성해주세요.

# 제한사항
# n은 2 이상 100 이하인 자연수입니다.
# wires는 길이가 n-1인 정수형 2차원 배열입니다.
# wires의 각 원소는 [v1, v2] 2개의 자연수로 이루어져 있으며, 
# 이는 전력망의 v1번 송전탑과 v2번 송전탑이 전선으로 연결되어 있다는 것을 의미합니다.
# 1 ≤ v1 < v2 ≤ n 입니다.
# 전력망 네트워크가 하나의 트리 형태가 아닌 경우는 입력으로 주어지지 않습니다.

# 문제접근
# 트리형식의 문제는 BFS/DFS로 풀이하면 될 것 같다.
# 이중 넓이 탐색 방법인 BFS로 연결된 송전탑들의 개수를 계산할 수 있다.
# BFS에 사용할 그래프를 생성한다.
# 전력을 하나씩 끊어가며 탐색하여 연결된 송전탑과 연결되지 않은 송전탑의 차이를 계산한다.

# 문제풀이(1)
from collections import deque
# BFS 메서드 정의
def bfs(graph, start, visited):
	queue = deque([start])
	# 현재 노드를 방문 거리
	visited[start] = True
	# 큐가 빌 때 까지 반복
	while queue:
		# 큐에서 하나의 원소를 뽑아 출력
		v = queue.popleft()
		# 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
		for i in graph[v]:
			if not visited[i]:
				queue.append(i)
				visited[i] = True

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

def solution(n, wires):
    answer = 0
    graph = [[] for _ in range(n+1)]    # 처음 시작 = ''이기 때문에 + 1

    for v1, v2 in wires:        # v1과 v2가 연결된 망을 찾기 위함.
        graph[v1].append(v2)
        graph[v2].append(v1)
        print(v1, v2 ,graph)
    
    # print(bfs(graph, 1, visited))

    return answer

# 연결된 노드끼리의 graph 생성완료
# bfs와 graph를 연결해야함
# 연결을 위해서 visited = 방문을 구해야함.


# 문제풀이(2)
from collections import deque
def bfs(graph, start, visited):
    queue = deque([start])
    cnt = 1
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                cnt += 1
                queue.append(i)
                visited[i] = True

    return cnt

def solution(n, wires):
    answer = 0
    graph = [[] for _ in range(n+1)]    # 처음 시작 = ''이기 때문에 + 1

    for v1, v2 in wires:        # v1과 v2가 연결된 망을 찾기 위함.
        graph[v1].append(v2)
        graph[v2].append(v1)
        print(v1, v2 ,graph)

    for first, second in wires:
        # 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
        visited = [False] * (n+1)
        print(bfs(graph, first, visited))

    return answer

# 방문할 수 있는 총 노드의 길이를 출력함.
# 이제 노드를 하나씩 차단해가면서 나눠진 송전탑의 개수가 가장 비슷하도록 해야함.


# 문제풀이(3)
from collections import deque
# BFS 구현
def bfs(graph, start, visited):
    queue = deque([start])
    cnt = 1
    # 현재 노드를 방문한 거리
    visited[start] = True

    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                cnt += 1
                queue.append(i)
                visited[i] = True

    return cnt

def solution(n, wires):
    answer = []
    graph = [[] for _ in range(n+1)]    # 처음 시작 = ''이기 때문에 + 1

    for v1, v2 in wires:        # v1과 v2가 연결된 망을 찾기 위함.
        graph[v1].append(v2)
        graph[v2].append(v1)
        # print(v1, v2 ,graph)

    for first, second in wires:
        # 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
        visited = [False] * (n+1)
        visited[second] = True  # 전력망 자르기
        result = bfs(graph, first, visited)
        num = abs(result - (n-result))  # 연결된 전력망- (연결되지 않은 전력망)
        answer.append(num)
        # print(first, result, result-(n- result))
        # print(visited)

    return min(answer)

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))   # 3
print(solution(4, [[1,2],[2,3],[3,4]]))     # 0
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))   # 1