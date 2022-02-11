# 로또의 최고 순위와 최저 순위

# 문제 설명 : https://programmers.co.kr/learn/courses/30/lessons/77484
# 1~ 45까지의 숫자 중 6개를 찍어서 맞히는 것
# 구매한 로또의 일부 번호를 알 수 없게 되었다.
# 자신이 구매했던 로또의 최고, 최저 순위를 알아보고 싶다.
# 알 수 없는 수 = 0
# 민우가 가지고 있는 로또 번호 = 44, 1, 0, 0, 31 25
# 1등 당첨 번호 = 31, 10, 45, 1, 6, 19
# 1등 = 6개, 2등 = 5개, 3등 = 4개, 4등 = 3개, 5등 = 2개, 6등 = 그외


# 예상 풀이
# 최고는 0을 무조건 맞는 숫자로 바꿔 판단한다.
# 굳이 0을 맞는 수나 맞지 않는 수로 바꿀 필요는 없을 것 같다.
# 가려진 번호를 제외한 당첨개수 + 0의 개수 = 최고 당첨 순위
# 가려진 번호를 제외한 당첨개수 = 최저 당첨 순위

# 문제 풀이(1)
# def solution(lottos, win_nums):
#     answer = []

#     lottos_win = 0
#     hidden_number = 0

#     for i in range(len(lottos)):
#         # 가려진 번호를 제외한 당첨 개수
#         if lottos[i] in win_nums:
#             lottos_win += 1
        
#         # 가려진 번호가 0인 개수
#         if lottos[i] == 0:
#             hidden_number += 1

#     lottos_win += hidden_number
#     print(lottos_win, hidden_number)

#     return answer


# 로또의 최고, 최저 당첨 개수를 구했음
# 이제 순위를 구해야함.
# 어캐??
# 올 if or 새 배열 생성후 비교

# 문제 풀이(2)
def solution(lottos, win_nums):
    answer = []
    rank = [6,6,5,4,3,2,1]  # 6,5,4,3,2,1일 경우 범위초과

    lottos_win = 0
    hidden_number = 0

    for i in range(len(lottos)):
        # 가려진 번호를 제외한 당첨 개수 : 최저 순위
        if lottos[i] in win_nums:
            lottos_win += 1
        
        # 가려진 번호가 0인 개수
        if lottos[i] == 0:
            hidden_number += 1

    # 최고 순위
    answer.append(rank[lottos_win + hidden_number])
    # 최저 순위
    answer.append(rank[lottos_win])

    # print(lottos_win, hidden_number)

    return answer

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))  # [3, 5]
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))  # [1, 6]
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35])) # [1, 1]