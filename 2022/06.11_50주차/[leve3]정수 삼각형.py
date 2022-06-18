# 정수 삼각형
# 링크: https://programmers.co.kr/learn/courses/30/lessons/43105

# 문제풀이(1)
def solution(triangle):  
  for i in range(1, len(triangle)):
    for j in range(len(triangle[i])):
      # 왼쪽 라인은 1개 밖에 없음
      if j == 0:
        triangle[i][j] += triangle[i-1][j]
        # print(len(triangle[i]))
      # 오른쪽 라인은 1개 밖에 없음
      elif j == len(triangle[i])-1:
        triangle[i][j] += triangle[i-1][j-1]
      else:
        triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

  return max(triangle[len(triangle)-1])

# 30
print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))