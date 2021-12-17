# from collections import deque

# def solution(numbers, target):
#     answer = 0
    
#     visit = list()      # 방문했던 노드들
#     queue = [0]         # 다음으로 방문할 노드의 목록
    
#     while queue:        # queue의 목록이 바닥날때까지 돌린다.
#         n = queue.pop(0)     # queue의 맨 앞에 있는 노드를 꺼내온다.
#         if n not in queue:     # 해당 노드가 리스트에 없다면
#             visit.append(n)
#             queue += numbers[n]
    
#     return answer
import heapq

tmp = [7, 5, 8, 3]
heapq.heapify(tmp)
print(tmp)