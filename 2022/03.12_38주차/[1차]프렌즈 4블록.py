# 프렌즈 4블록
# 링크: https://programmers.co.kr/learn/courses/30/lessons/17679

# 문제접근
# 애니팡 같은 느낌이지만 4블록만 부술수 있고 따로 부수지 않고
# 한번에 4개가 되는 것을 중복이 되어도 부순다.
# 1. 4블록이 같을 때 제거하는 문항을 작성.
# 2. 제거된 블럭을 위에서 아래로 채워주는 문항 작성.
# 3. 1~2번 반복
# 4. 같은 블록이 없다면 지워진 블록개수 count return

# 문제풀이(1)
def solution(m, n, board):
  answer = 0

  # 2차원 배열로 변경
  for i in range(len(board)):
    popped = board.pop(0)
    board.append([p for p in popped])

  return answer

# board 배열을 2차원으로 변경


# 문제풀이(2)
def solution(m, n, board):
  answer = 0
  block = set()

  # 2차원 배열로 변경
  for i in range(len(board)):
    popped = board.pop(0)
    board.append([p for p in popped])

  # 4블록이 같은지 판별
  for i in range(1, m):
    for j in range(1, n):
      if board[i-1][j-1] == board[i-1][j] == board[i][j-1] == board[i][j] != ' ':
        # 중복이 있기 때문에 집합으로 해결함
        block.update([(i-1, j-1), (i-1, j), (i, j-1), (i, j)])
  
  print(block)

  # 삭제
  for i in block:
    x, y = i
    board[x][y] = ' '

  print(board)

  return answer

# 같은 4블럭을 인덱스 번호로 가져왔음
# 중복이 있기때문에 set으로 해결
# 남아있는 값들을 아래로 내리는 항목 생성해야함.
# 반복 시행해야 하기 때문에 while문 or 함수로 빼주기?


# 문제풀이(3)
def solution(m, n, board):
  answer = 0

  # 2차원 배열로 변경
  for i in range(len(board)):
    popped = board.pop(0)
    board.append([p for p in popped])

  while True:
    block = set()
    # 4블록이 같은지 판별
    for i in range(1, m):
      for j in range(1, n):
        if board[i-1][j-1] == board[i-1][j] == board[i][j-1] == board[i][j] != ' ':
          # 중복이 있기 때문에 집합으로 해결함
          block.update([(i-1, j-1), (i-1, j), (i, j-1), (i, j)])
    
    print(block)
    answer += len(block)
    if len(block) == 0: break

    # 삭제
    for i in block:
      x, y = i
      board[x][y] = ' '

    # print(board)

    # 이동
    for i in range(n):
      stack = []
      for j in range(m-1, -1, -1):
        if board[j][i] != ' ':
          stack.append(board[j][i])
      # print(stack)
      for k in range(m-1, -1, -1):
        if len(stack) != 0:
          board[k][i] = stack.pop(0)
        else:
          board[k][i] = ' '

    # print(board)

  return answer


# 다른 사람의 풀이(1)
# https://hello-i-t.tistory.com/84
# https://velog.io/@tjdud0123/프렌즈-4블록-2018-카카오-공채-python
# 파이썬
# def pop_num(b, m, n):
#     pop_set = set()
#     # search
#     for i in range(1, n):
#         for j in range(1, m):
#             if b[i][j] == b[i-1][j-1] == b[i-1][j] == b[i][j-1] != '_':
#                 pop_set |= set([(i, j), (i-1, j-1), (i-1, j), (i, j-1)])
#     # set_board
#     for i, j in pop_set:
#         b[i][j] = 0        
#     for i, row in enumerate(b):
#         empty = ['_'] * row.count(0)
#         b[i] = empty + [block for block in row if block != 0]
#     return len(pop_set)
     
# def solution(m, n, board):
#     count = 0
#     b = list(map(list,zip(*board)))
#     while True:
#         pop = pop_num(b, m, n)
#         if pop == 0: return count
#         count += pop


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))    # 14
print(solution(6, 6, 
["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])) # 15