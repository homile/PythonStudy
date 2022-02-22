# 행렬 테두리 회전하기

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/77485
# rows x columns 크기인 행렬이 있습니다. 
# 행렬에는 1부터 rows x columns까지의 숫자가 한 줄씩 순서대로 적혀있습니다. 
# 이 행렬에서 직사각형 모양의 범위를 여러 번 선택해, 
# 테두리 부분에 있는 숫자들을 시계방향으로 회전시키려 합니다. 
# 각 회전은 (x1, y1, x2, y2)인 정수 4개로 표현하며, 그 의미는 다음과 같습니다.

# x1 행 y1 열부터 x2 행 y2 열까지의 영역에 해당하는 직사각형에서 
# 테두리에 있는 숫자들을 한 칸씩 시계방향으로 회전합니다.
# 다음은 6 x 6 크기 행렬의 예시입니다.

# 이 행렬에 (2, 2, 5, 4) 회전을 적용하면, 
# 아래 그림과 같이 2행 2열부터 5행 4열까지 영역의 테두리가 시계방향으로 회전합니다. 
# 이때, 중앙의 15와 21이 있는 영역은 회전하지 않는 것을 주의하세요.

# 행렬의 세로 길이(행 개수) rows, 가로 길이(열 개수) columns,   
# 그리고 회전들의 목록 queries가 주어질 때, 각 회전들을 배열에 적용한 뒤, 
# 그 회전에 의해 위치가 바뀐 숫자들 중 가장 작은 숫자들을 순서대로 배열에 담아 
# return 하도록 solution 함수를 완성해주세요.

# 문제접근
# 사각형의 가운데는 회전하지 않는다.
# 회전은 시계방향으로 한다.

# 1. 행렬 크기를 지정한다.
# 2. 지정한 행렬에 초기값을 지정한다.
# 상하좌우로 움직여야한다.
# 왼쪽상단을 기준으로 돌려야한다.
# 겹치는 번호가 생길경우를 대비하여 왼쪽상단 번호는 따로 빼고 회전한다.

# 왼쪽 값들을 위로 이동
# 하단 값을 왼쪽으로 이동
# 오른쪽 값들을 하단으로 이동
# 상단 값들을 우측으로 이동

# 문제풀이(1)
def solution(rows, columns, queries):
    answer = []
    matrix = [[0 for _ in range(rows)] for _ in range(columns)]     # 행렬 크기 지정
    num = 1

    for i in range(rows):       # 행렬에 초기값 지정
        for j in range(columns):
            matrix[i][j] = num
            num += 1
    # print(matrix)

    for x1, y1, x2, y2 in queries:
        # print(x1-1, y1-1, x2-1, y2-1)   # 인덱스 번호는 0부터 시작
        temp = matrix[x1-1][y1-1]
        num_min = temp

        for y in range(x1-1, x2-1):     # 왼쪽라인 위로 이동
            # print(matrix[y+1][y1-1])
            matrix[y][y1-1] = matrix[y+1][y1-1]

        for x in range(y1-1, y2-1):     # 아랫라인 왼쪽으로 이동
            # print(matrix[x2-1][x+1])
            matrix[x2-1][x] = matrix[x2-1][x+1]

        for y in range(x1-1, x2-1):     # 오른쪽 라인 아래로 이동
            # print(matrix[y+1][y2-1], matrix[y][y2-1])
            matrix[y+1][y2-1] = matrix[y][y2-1]
        print(matrix)

    return answer

# 정방향으로 이동하는 것은 쉽게 해결했으나
# 역방향으로 이동하는 것이 쉽지 않았음.


# 문제풀이(2)
def solution(rows, columns, queries):
    answer = []
    matrix = [[0 for _ in range(rows)] for _ in range(columns)]     # 행렬 크기 지정
    num = 1

    for i in range(rows):       # 행렬에 초기값 지정
        for j in range(columns):
            matrix[i][j] = num
            num += 1
    # print(matrix)

    for x1, y1, x2, y2 in queries:
        # print(x1-1, y1-1, x2-1, y2-1)   # 인덱스 번호는 0부터 시작
        temp = matrix[x1-1][y1-1]
        num_min = temp

        for y in range(x1-1, x2-1):     # 왼쪽라인 위로 이동
            # print(matrix[y+1][y1-1])
            matrix[y][y1-1] = matrix[y+1][y1-1]

        for x in range(y1-1, y2-1):     # 아랫라인 왼쪽으로 이동
            # print(matrix[x2-1][x+1])
            matrix[x2-1][x] = matrix[x2-1][x+1]

        for y in range(x2-1, x1-1, -1):     # 오른쪽라인 아래로 이동
            # print(matrix[y][y2-1], matrix[y-1][y2-1])
            matrix[y][y2-1] = matrix[y-1][y2-1]

        for x in range(y2-1, y1-1, -1):     # 윗쪽라인 오른쪽으로 이동
            # print(matrix[x1-1][x], matrix[x1-1][x-1])
            matrix[x1-1][x] = matrix[x1-1][x-1]

        print(matrix)

    return answer

# 모든 방향으로 이동하는 것을 끝냈다.
# 이제는 temp에 들어있는 값을 위쪽라인을 오른쪽으로 보낼때 
# 마지막에 적용을 시켜야한다.
# 그리고 값들을 비교해서 최저값(min)을 찾아야한다.


# 문제풀이(3)
def solution(rows, columns, queries):
    answer = []
    matrix = [[0 for _ in range(rows)] for _ in range(columns)]     # 행렬 크기 지정
    num = 1

    for i in range(rows):       # 행렬에 초기값 지정
        for j in range(columns):
            matrix[i][j] = num
            num += 1
    # print(matrix)

    for x1, y1, x2, y2 in queries:
        # print(x1-1, y1-1, x2-1, y2-1)   # 인덱스 번호는 0부터 시작
        temp = matrix[x1-1][y1-1]
        num_min = temp

        for y in range(x1-1, x2-1):         # 왼쪽라인 위로 이동
            # print(matrix[y+1][y1-1])
            matrix[y][y1-1] = matrix[y+1][y1-1]
            num_min = min(num_min, matrix[y][y1-1])

        for x in range(y1-1, y2-1):         # 아랫라인 왼쪽으로 이동
            # print(matrix[x2-1][x+1])
            matrix[x2-1][x] = matrix[x2-1][x+1]
            num_min = min(num_min, matrix[x2-1][x])

        for y in range(x2-1, x1-1, -1):     # 오른쪽라인 아래로 이동
            # print(matrix[y][y2-1], matrix[y-1][y2-1])
            matrix[y][y2-1] = matrix[y-1][y2-1]
            num_min = min(num_min, matrix[y][y2-1])

        for x in range(y2-1, y1-1, -1):     # 윗쪽라인 오른쪽으로 이동
            # print(matrix[x1-1][x], matrix[x1-1][x-1])
            matrix[x1-1][x] = matrix[x1-1][x-1]
            num_min = min(num_min, matrix[x1-1][x])

        # print(matrix)
        matrix[x1-1][y1] = temp     # 왼쪽위에 첫번째 값을 오른쪽으로 한칸 이동
        answer.append(num_min)

    return answer

# IndexError: list index out of range
# 125번째 줄에서 에러발생

# 이유 초기 값을 생성할 때 행과 열이 같다는 전재하에 빈 배열을 만들었으나
# 100, 97로 이루어진 배열을 생성할 때 오류 발생
# 초기 배열 생성 시 columns와 rows를 변경하면 해결될 듯.


# 문제풀이(4)   # 통과
def solution(rows, columns, queries):
    answer = []
    matrix = [[0 for _ in range(columns)] for _ in range(rows)]     # 행렬 크기 지정
    num = 1

    for i in range(rows):       # 행렬에 초기값 지정
        for j in range(columns):
            matrix[i][j] = num
            num += 1
    # print(matrix)

    for x1, y1, x2, y2 in queries:
        # print(x1-1, y1-1, x2-1, y2-1)   # 인덱스 번호는 0부터 시작
        temp = matrix[x1-1][y1-1]
        num_min = temp

        for y in range(x1-1, x2-1):         # 왼쪽라인 위로 이동
            # print(matrix[y+1][y1-1])
            matrix[y][y1-1] = matrix[y+1][y1-1]
            num_min = min(num_min, matrix[y][y1-1])

        for x in range(y1-1, y2-1):         # 아랫라인 왼쪽으로 이동
            # print(matrix[x2-1][x+1])
            matrix[x2-1][x] = matrix[x2-1][x+1]
            num_min = min(num_min, matrix[x2-1][x])

        for y in range(x2-1, x1-1, -1):     # 오른쪽라인 아래로 이동
            # print(matrix[y][y2-1], matrix[y-1][y2-1])
            matrix[y][y2-1] = matrix[y-1][y2-1]
            num_min = min(num_min, matrix[y][y2-1])

        for x in range(y2-1, y1-1, -1):     # 윗쪽라인 오른쪽으로 이동
            # print(matrix[x1-1][x], matrix[x1-1][x-1])
            matrix[x1-1][x] = matrix[x1-1][x-1]
            num_min = min(num_min, matrix[x1-1][x])

        # print(matrix)
        matrix[x1-1][y1] = temp     # 왼쪽위에 첫번째 값을 오른쪽으로 한칸 이동
        answer.append(num_min)

    return answer

# 행과 열을 할때 자세히 보고 해야한다.

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))    # [8, 10, 25]
print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))    # [1, 1, 5, 3]
print(solution(100, 97, [[1,1,100,97]]))    # [1]