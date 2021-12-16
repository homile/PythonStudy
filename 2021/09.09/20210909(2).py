# 땅따먹기

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/12913

# 문제접근
# 1,2,3,5
# 5,6,7,8
# 4,3,2,1

# 같은 열이 아닌 값 중 제일 큰 값을 찾아서 더하면 됨
# 만약 첫 번째 행에서 (0,0) = 1 을 밟았다면
# max([1,1], [1,2], [1,3])을 사용 0번째 열을 제외한
# 나머지 열들 중 제일 큰 값을 찾으면 됨
# 그 값을 더해주면 됨

# max 함수 사용?

# DP(Dynamic Programming)?

# 문제풀이(1)
def solution(land):
    answer = 0
    dp = [[0 for _ in range(len(land[0]))] for _ in range(len(land))]
    
    for i in range(len(land)):
        for j in range(len(land[0])):
            dp[i][j] = max(land[i])
            
    print(dp)
    
    return answer

# 어떻게 열이 겹치지 않게 최대값을 구함?

# 각 열의 최대값을 구해서 가져옴… 그 뒤?


# 문제풀이(2)
def solution(land):
    answer = 0
    dp = [[0 for _ in range(len(land[0]))] for _ in range(len(land))]
    
    for i in range(len(land)):
        for j in range(len(land[0])):
            if i == 0 :
                dp[i][j] = land[i][j]
            else :
                dp[i][j] = max(dp[i][j], dp[i-1][j]+land[i][j])           
    
    print(dp)
    answer = max(dp[-1])
    
    return answer

# 같은 열끼리 더해버리는 상황 발생
# 어떻게 해결할 지 찾아야 함

# for문을 하나 더 써야 하나?

# 굳이 새로운 리스트를 만들 필요가 있었나?


# 문제풀이(3) 성공
def solution(land):
    answer = 0
    dp = [[0 for _ in range(len(land[0]))] for _ in range(len(land))]
    
    for i in range(len(land)):
        for j in range(len(land[0])):
            if i == 0 :
                dp[i][j] = land[i][j]
                continue
            for k in range(len(land[0])) :
                if k != j :
                    dp[i][j] = max(dp[i][j], dp[i-1][k]+land[i][j])           
    
    # print(dp)
    answer = max(dp[-1])
    
    return answer

# 열이 겹치지 않게 하려고 for문을 하나 더 생성
# dp리스트의 첫번째 행에 값을 삽입
# j는 지나쳐온 열의 번호
# k는 밟을 열의 번호

# 열 번호 j와 k가 같지 않을 경우
# dp[i][j] 방에 계속 비교해가며 더했을 때
# 가장 큰 값을 갱신

# 마지막 행에서 가장 큰 값을 출력


# 문제풀이(4)
def solution(land):
    answer = 0
    
    for i in range(1, len(land)):
        land[i][0] += max(land[i-1][1], land[i-1][2], land[i-1][3])
        land[i][1] += max(land[i-1][0], land[i-1][2], land[i-1][3])
        land[i][2] += max(land[i-1][0], land[i-1][1], land[i-1][3])
        land[i][3] += max(land[i-1][0], land[i-1][1], land[i-1][2])

    answer = max(land[-1])
    
    return answer

# 새로운 리스트를 만들지 않고 하니
# 코드가 간결해짐

# 하나하나 겹치지 않게 함
# 테스트는 통과하나 다음에 해결할 때
# 열과 행의 개수가 다른 테스트 케이스가
# 생길 시 오류가 발생할 확률 100%


# 다른 사람의 풀이(1)
def solution(land):

    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] = max(land[i -1][: j] + land[i - 1][j + 1:]) + land[i][j]

    return max(land[-1])

# 슬라이싱 기법을 사용하여 
# 열이 겹치지 않게 한 풀이

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))    # 16