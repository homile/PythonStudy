# 타겟넘버

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/43165

# 문제접근
# dfs/bfs에 대해서 알아봄
# 이문제는 dfs/bfs 둘다 가능할듯?

# 이유 - 하나씩 바꿔가면서 하는 거라?

# BFS로 한다면?? 경우의 수로 하나씩 배열에 추가?

# 문제풀이(1)
from collections import deque

def solution(numbers, target):
    answer = 0
    
    visit = []    # 방문했던 노드들
    queue = [0]         # 다음으로 방문할 노드의 목록
    
    while queue:        # queue의 목록이 바닥 날때까지 돌린다.
        n = queue.popleft()     # queue의 맨 앞에 있는 노드를 꺼내 온다.
        if n not in queue:     # 해당 노드가 리스트에 없다면
            visit.append(n)
            queue.extend(numbers[n])
    
    return answer


# 문제풀이(2)
from collections import deque

def solution(numbers, target):
    answer = 0
    
    visit = []    # 방문했던 노드들
    queue = [0]         # 다음으로 방문할 노드의 목록
    
    while queue:        # queue의 목록이 바닥 날때까지 돌린다.
        n = queue.popleft()     # queue의 맨 앞에 있는 노드를 꺼내 온다.
        if n not in queue:     # 해당 노드가 리스트에 없다면
            visit.append(n)
            queue.extend(numbers[n])
    
    return answer


# 다른 사람의 풀이(1)
from collections import deque

def solution(numbers, target):
    answer = 0
    stack = deque([(0, 0)])
    
    while stack:
        l, n = stack.popleft()
        
        if n == len(numbers):
            if l == target:
                answer += 1
        else:
            number = numbers[n]
            stack.append((l+number, n+1))
            stack.append((l-number, n+1))
            
    return answer


# 다른 사람의 풀이(2)
answer = 0
def DFS(idx, numbers, target, value):
    global answer
    N = len(numbers)
    if(idx== N and target == value):
        answer += 1
        return
    if(idx == N):
        return

    DFS(idx+1,numbers,target,value+numbers[idx])
    DFS(idx+1,numbers,target,value-numbers[idx])

def solution(numbers, target):
    global answer
    DFS(0,numbers,target,0)
    return answer
