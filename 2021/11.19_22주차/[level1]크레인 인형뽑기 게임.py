# 크레인 인형뽑기 게임

# 문제 설명 : https://programmers.co.kr/learn/courses/30/lessons/64061

# 예상 풀이
# moves의 i번째값이 1이면
# board의 세로 1-1번째(0)에서 0이 아닌 수를 가져온다.
# 가져온 값을 result에 쌓아준뒤
# 마지막에 앞뒤를 비교해서 같은 숫자가 2연속 나오면 제거해서
# 제거한 갯수를 answer로 넘겨준다.

# 문제 풀이(1)
# def solution(board, moves):
#     answer = 0
#     result = []

#     for i in moves:
#         for j in board:
#             # moves의 i번째가 0이 아닌값 가져오기
#             if j[i-1] != 0:
#                 result.append(j[i-1])
#                 j[i-1] = 0
#                 break
#                 # print(i, j[i-1])
#     print(result)


#     return answer

# 움직인 자리의 숫자를 가져와서
# list(result)에 넣어주고
# board의 i번째 값은 0으로 바꿔줬다.

# 해야 할 것
# 앞뒤를 비교해서 2개 연속 같은 숫자 일 경우 
# 숫자를 제거 한뒤 몇개를 제거했는지를 알아내면됨.

# 문제 풀이(2)
# def solution(board, moves):
#     answer = 0
#     result = []

#     for i in moves:
#         for j in board:
#             # moves의 i번째가 0이 아닌값 가져오기
#             if j[i-1] != 0:
#                 result.append(j[i-1])
#                 j[i-1] = 0
#                 break
#                 # print(j, j[i-1])
#     print(result)

#     for i in range(len(result)):
#         if result[i] == result[i-1]:
#             result.pop(i)
#             result.pop(i-1)

#     return answer


# 문제 풀이(3)
# def solution(board, moves):
#     answer = 0
#     result = []

#     for i in moves:
#         for j in board:
#             # moves의 i번째가 0이 아닌값 가져오기
#             if j[i-1] != 0:
#                 result.append(j[i-1])
#                 j[i-1] = 0
#                 break
#                 # print(j, j[i-1])
#     print(result)

#     while True:
#         if result[i-1] == result[i]:
#             result.pop(i-i)
#             result.pop(i)
#             answer += 1

#     return answer

# 문제 풀이(4)
# def solution(board, moves):
#     answer = 0
#     result = []
#     num = 0

#     for i in moves:
#         for j in board:
#             # moves의 i번째가 0이 아닌값 가져오기
#             if j[i-1] != 0:
#                 result.append(j[i-1])
#                 j[i-1] = 0
#                 break
#                 # print(i, j[i-1])

#         if len(result) >= 2 and result[num-1] == result[num]:
#             result.pop(num)
#             result.pop(num-1)
#             answer += 2

#         num += 1
            
#     print(result)

#     return answer

# 좌우 비교할 num이 초과하는 경우 발생
# 그럼 맨 마지막값과 마지막의 바로 앞의 값을 비교

# 문제 풀이(5)
# def solution(board, moves):
#     answer = 0
#     result = []

#     for i in moves:
#         for j in board:
#             # moves의 i번째가 0이 아닌값 가져오기
#             if j[i-1] != 0:
#                 result.append(j[i-1])
#                 j[i-1] = 0
#                 break
#                 # print(i, j[i-1])

#         if len(result) >= 2 and result[-1] == result[-2]:
#             result.pop(-2)
#             result.pop(-1)
#             answer += 2
            
#     print(result)

#     return answer


# 다른 사람의 풀이(1)
def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break

    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],
[1,5,3,5,1,2,1,4]))