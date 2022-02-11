# 가장 큰 정사각형 찾기

# 문제 설명 : https://programmers.co.kr/learn/courses/30/lessons/12905

# 예상 풀이
# 세로와 가로의 길이가 맞지 않으면 안됨
# 2차원 배열이기 때문에 2중 for문 사용??
# 정사각형의 전체 면적은 가로 or 세로의 제곱이다.
# 0111
# 1111
# 0111   <-과 같은 3x3의 정사각형일 경우
# 전체 면적은 3**2 = 9이다.

# 사각형을 구하려면 왼쪽과 위쪽이 
# 0이 아닌 수를 찾아야한다.

# 문제 풀이(1)
# def solution(board):
#     answer = 0
    
#     for i in range(len(board)):
#         for j in range(len(board[0])):
#             print(board[i][j])
#         print('')
        
#     return answer

# board[i][j]의 값이 1일 때 어떻게 해야함????

# # 문제 풀이(2)
# def solution(board):
#     answer = 0
    
#     for i in range(len(board)):         # 행
#         for j in range(len(board[0])):  # 열
#             if board[i][j] == 1:
#                 print(board[i][j])
#         print('')
        
#     return answer


# 문제 풀이(3)
# def solution(board):
#     answer = 0
#     stack = []
#     for i in range(1, len(board)):         # 행
#         for j in range(1, len(board[0])):  # 열
#             if board[i][j] == 1:
#                 stack.append([board[i-1][j-1]])
#                 stack.append(board[i-1][j])
#                 stack.append([board[i][j-1]])
#         print('')
        
#     print(stack)
#     return answer

# 모든 행과 열을 비교하기 위해 stack에 쌓아봄..
# 그런데도 해결방안이 떠오르지 않는다...

# # 문제 풀이(4)
# def solution(board):
#     answer = 0
#     for i in range(1, len(board)):         # 행
#         for j in range(1, len(board[0])):  # 열
#             if board[i][j] == 1:
#                 board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1])+1
#                 answer = max(answer, board[i][j])
#         print('')
        
#     print(board)
#     return answer**2

# 제출시 1번 문항 실패
# 1이 하나만 존재할 경우?
# 1이 하나도 존재하지 않을 경우?

# 문제 풀이(5)
def solution(board):
    answer = 0
    
    if len(board) < 2 and 1 in sum(board,[]):
        return 1
    
    for i in range(1, len(board)):         # 행
        for j in range(1, len(board[0])):  # 열
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1])+1
                answer = max(answer, board[i][j])
#         print('')
        
#     print(board)
    return answer**2

# 다른 사람의 풀이(1) # DP
# def findLargestSquare(board):
#     answer = 1
#     res = [[1 if x=='O' else 0 for x in y] for y in board]
#     for y in range(len(board)):
#         for x in range(len(board[y])):
#             if board[y][x] == 'O':
#                 res[y][x] = min(res[y-1][x], res[y-1][x-1], res[y][x-1]) + 1
#                 if res[y][x] > answer: answer = res[y][x]

#     return answer ** 2

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))  # 9
print(solution([[0,0,1,1],[1,1,1,1]]))                      # 4