# 삼각 달팽이

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/68645
# 정수 n이 매개변수로 주어집니다. 
# 다음 그림과 같이 밑변의 길이와 높이가 n인 삼각형에서 맨 위 꼭짓점부터 반시계 방향으로 
# 달팽이 채우기를 진행한 후, 첫 행부터 마지막 행까지 모두 순서대로 합친 새로운 배열을 
# return 하도록 solution 함수를 완성해주세요.

# 문제접근
# 예시에 나오는 빈 2차원 배열을 만들어준다.
# 빈 2차원 배열에 값을 저장한다.
# 어떻게? 

# 문제풀이(1)
def solution(n):
    answer = [[0 for col in range(n)] for row in range(n)] # 빈 2차원 배열
    num = 1

    for i in range(n):
        for j in range(i, n):
            answer[i][j] = num
            num += 1

    return answer

# 값을 삼각형으로 만들어서 저장해야한다.
# x, y값을 range로 돌리지 말고 지정해서 +해야한다.


# 문제풀이(2)
def solution(n):
    answer = []
    result = [[0 for col in range(n)] for row in range(n)] # 빈 2차원 배열
    # list1  = [[0 for j in range(1, i+1)] for i  in range(1, n+1)]     # 삼각형으로 빈 2차원 배열 생성
    # print(list1)
    num = 1
    x, y = -1, 0

    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1

            result[x][y] = num
            num += 1
    # print(result)

    for i in range(len(result)):
        for j in range(len(result[0])):
            if result[i][j] != 0:
                answer.append(result[i][j])

    return answer

print(solution(4))      # [1,2,9,3,10,8,4,5,6,7]
print(solution(5))      # [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
print(solution(6))      # [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]