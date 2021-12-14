# 행렬의 곱셈

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/12949

# 문제접근

# 문제풀이(1)
def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            answer.append(arr1[i][j]*arr2[j][i])
            
    # print((arr1[0][0]*arr2[0][0])+(arr1[0][1]*arr2[1][0]))
    return answer

# IndexError: list index out of range
# arr1과 arr2의 길이가 달라서 생기는 문제?
# 1. answer list의 길이를 미리 지정해주는 방법
# 2. for문의 len의 길이 지정 실패


# 문제풀이(2)
def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                answer[i][j] += (arr1[i][k] * arr2[k][j])
                
    # print(arr2[0])
    # print((arr1[0][0]*arr2[0][0])+(arr1[0][1]*arr2[1][0]))
    return answer

# answer에 arr2의 행과 arr1의 열로 빈행렬을 # 만들어 준다. (2차원 배열)

# arr1의 행의 길이만큼 반복    (3)
# arr2의 행의 길이만큼 반복    (2)
# arr1의 열의 길이만큼 반복    (2)
# answer[i][j]에 arr1의 행 x arr2의 열 
# Ex1)의 arr1 = (3x2) 행렬, arr2 = (2x2)행렬


# 다른 사람의 풀이(1)
def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        temp_list = []
        for j in range(len(arr2[0])):
            temp = 0
            for k in range(len(arr2)):
                temp += arr1[i][k]*arr2[k][j]
            temp_list.append(temp)
        answer.append(temp_list)
            
    return answer

# [[15, 15], [15, 15], [15, 15]
print(solution([[1, 4], [3, 2], [4, 1]],[[3, 3], [3, 3]]))
# [[22, 22, 11], [36, 28, 18], [29, 20, 14]]
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], 
[[5, 4, 3], [2, 4, 1], [3, 1, 1]]))