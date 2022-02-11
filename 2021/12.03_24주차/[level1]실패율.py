# 실패율

# 문제설명 : https://programmers.co.kr/learn/courses/30/lessons/42889
# 실패율 
# 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
# 전체 스테이지의 수 = N
# 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages
# 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return

# 참고사이트 : https://blockdmask.tistory.com/566

# 예상풀이
# stages를 오름차순으로 정렬
# 1스테이지에 멈춰있을 경우 1/len(stages)
# len(stages)의 객체 생성 : 실패율 따질때 사용

# 문제풀이(1)
# def solution(N, stages):
#     answer = []
#     stages.sort()
#     print(stages)
#     k = len(stages)

#     for i in range(1, N+1):
#         cnt = 0
#         for j in range(len(stages)):
#             if i == stages[j]:
#                 cnt += 1
        
#         answer.append(cnt/k)
#         k -= cnt
#         print(i, cnt, k)

#     return answer


# 문제풀이(2)
# 실패율까진 구하여 answr배열에 담았다.
# 각 스테이지별로 실패율을 비교하여 내림차순으로 정렬하면 될듯??
# 실패율을 스테이지 별로 구분할 방법??
# 1. 인덱스 넘버 부여
# 2. 딕셔너리 형식으로 부여
# def solution(N, stages):
#     answer = []
#     s_list = []
#     stages.sort()
#     k = len(stages)

#     for i in range(1, N+1):
#         cnt = 0
#         for j in range(len(stages)):
#             if i == stages[j]:
#                 cnt += 1
        
#         s_list.append(cnt/k)
#         k -= cnt
#         print(i, cnt, k)

#     s_reverse = sorted(s_list,reverse=True)
#     print(s_list,s_reverse)

#     for i in range(len(s_reverse)):
#         answer.append(s_list.index(s_reverse[i])+1)

#     return answer


# 문제풀이(3)
# 실패율이 같을 경우 같은 스테이지로 인식함.
# 리스트로 하는 것보다 딕셔너리 형식을 사용하면 될듯

# 딕셔너리로 값을 받는 것까지 하였으나 내림차순으로 만드는 법을 모름
# def solution(N, stages):
#     answer = []
#     s_dict = {}
#     stages.sort()
#     k = len(stages)

#     for i in range(1, N+1):
#         cnt = 0
#         for j in range(len(stages)):
#             if i == stages[j]:
#                 cnt += 1
        
#         s_dict[i] = cnt/k
#         k -= cnt
#         print(i, cnt, k)

#     # s_reverse = sorted(s_dict.items(), reverse=True)
#     # print(s_reverse)
#     return answer


# 문제풀이(4)
# 제출시 런타임 에러 다수 발생 70.4/100.0
# 딕셔너리로 해서 오래 걸리나?
# for문을 너무 많이 사용??
# def solution(N, stages):
#     answer = []
#     s_dict = {}
#     stages.sort()
#     k = len(stages)

#     for i in range(1, N+1):
#         cnt = 0
#         for j in range(len(stages)):
#             if i == stages[j]:
#                 cnt += 1
        
#         s_dict[i] = cnt/k
#         k -= cnt
#         print(i, cnt, k)

#     s_reverse = sorted(s_dict.items(), key=lambda x: x[1], reverse=True)
#     print(s_reverse)

#     for i in s_reverse:
#         answer.append(i[0])

#     return answer


# 문제풀이(5)
# for문을 하나 줄여도 70.4점 나옴
# 그러면 이유는 2중 for문을 사용한 부분이 
# 런타임 에러를 발생하는 것 같음.
# from typing import Counter


# def solution(N, stages):
#     answer = {}
#     k = len(stages)

#     for i in range(1, N+1):
#         cnt = 0
#         for j in range(len(stages)):
#             if i == stages[j]:
#                 cnt += 1
        
#         answer[i] = cnt/k
#         k -= cnt

#     answer = sorted(answer, key=lambda x: answer[x], reverse=True)

#     return answer


# 문제풀이(6)
def solution(N, stages):
    answer = {}
    k = len(stages)

    for i in range(1, N+1):
        if k != 0:
            fail = stages.count(i)
            answer[i] = fail/k
            k -= fail
        else:
            answer[i] = 0

    answer = sorted(answer, key=lambda x: answer[x], reverse=True)

    return answer


# 다른 사람의 풀이(1)
# 하고 싶었던 풀이
# def solution(N, stages):
#     answer = []
#     fail = []
#     info = [0] * (N + 2)
#     for stage in stages:
#         info[stage] += 1
#     for i in range(N):
#         be = sum(info[(i + 1):])
#         yet = info[i + 1]
#         if be == 0:
#             fail.append((str(i + 1), 0))
#         else:
#             fail.append((str(i + 1), yet / be))
#     for item in sorted(fail, key=lambda x: x[1], reverse=True):
#         answer.append(int(item[0]))
#     return answer

print(solution(5, [2,1,2,6,2,4,3,3]))       # [3,4,2,1,5]
print(solution(4, [4,4,4,4,4]))             # [4,1,2,3]