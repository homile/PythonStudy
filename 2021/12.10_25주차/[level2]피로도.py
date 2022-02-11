# 피로도

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/87946
# 탐험을 시작하기 위해 필요한 "최소 필요 피로도"
# 던전 탐험을 마쳤을 때 소모되는 "소모 피로도"
# 최소 필요 피로도 = 80, 소모 피로도 = 20인 던전을 탐험하기 위해서는
# 유저의 현재 남은 피로도 >= 80 -> 유저의 현재 남은 피로도 - 20
# 유저가 탐험할 수 있는 최대 던전 수를 구해야함.

# 문제접근
# 최소 직사각형 문제와 매우 흡사하다.
# 최소 필요 피로도를 기준으로 내림차순으로 정렬한 다음
# 남은 피로도에서 소모 피로도를 뺀 값이 
# 0 미만이 아닐경우의 개수를 count하면된다.

# 문제풀이(1)
# def solution(k, dungeons):
#     answer = 0
#     cnt = 0
#     dungeons = sorted(dungeons, reverse=True)

#     for i in range(len(dungeons)):
#         if k >= dungeons[i][0]:
#             print(dungeons[i][0],dungeons[i][1],k)
#             if k >= dungeons[i][1] and k-dungeons[i][1] >= 0:
#                 cnt += 1
#                 k -= dungeons[i][1]
#                 print(k)
    
#     answer = cnt

#     return answer


# [80,20], k=60 -> [30,10] k=50 -> [50,40] k=0
# 던전 최소 피로도에 맞춘다고 해결되지 않았다.
# 순열, 조합으로 풀어야 할 것 같다.

# 문제풀이(2)
from itertools import permutations

def solution(k, dungeons):
    answer = 0
    cnt = 0
    dungeons_len = len(dungeons)    # 소모한 피로도를 알기위함
    clear = []  # 각 순열별로 던전을 최대로 클리어한 횟수

    # 던전의 개수만큼 permutations를 통해 여러가지 순열 구함
    for dungeons_p in permutations(dungeons, dungeons_len):
        fatigue = k     # 다른 경우의 수를 구하기위해 피로도를 초기화
        cnt = 0         # 던전 클리어 횟수
        print(dungeons_p)
        for num in range(len(dungeons_p)):
            # 현재 피로도가 던전의 최소 요구 피로도보다 크거나 같다면 실행
            if fatigue >= dungeons_p[num][0]: 
                # 현재 피로도가 소모피로도보다 크거나 같고 현재 피로도-소모피리도가 0과 크거나 같다면 실행
                if fatigue >= dungeons_p[num][1] and fatigue-dungeons_p[num][1] >= 0:
                    cnt += 1
                    fatigue -= dungeons_p[num][1]
        
        clear.append(cnt)   # 경우의 수만큼 클리어한 값
        print(clear)
    answer = max(clear)     # 클리어한 값들중 가장 큰값

    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))  # 3