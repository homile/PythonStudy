# 평균 구하기

# 문제설명 : https://programmers.co.kr/learn/courses/30/lessons/12944

# 예상풀이
# List arr안의 내용을 다 더한 후 arr의 길이 만큼 나눠서 평균을 구한다.
# sum 함수 사용

# 문제풀이(1)
# def solution(arr):

#     answer = sum(arr,0) / len(arr)
    
#     return answer


# 문제풀이(2)
# 함수를 사용하지 않고 풀어야 할 경우 list arr의 값을 
# 하나하나 더해서 arr의 길이만큼 나눠 준다
# def solution(arr):
#     a = 0
#     for i in range(len(arr)):
#         a += arr[i]
        
#     return a / len(arr)


# 문제풀이(3)
# Numpy라는 라이브러리를 np라는 변수명으로 지정하여 사용했다.
# Numpy는 주로 ML, AI에서 다차원 배열을 쉽게 처리하기 위한 라이브러리이며,
# List와 매우 흡사한 구조를 이루고 있다.
# Mean은 numpy의 산술연산자 중 평균 값을 구해주는 함수이다.
import numpy as np
def solution(arr):
    
    return np.mean(arr)

print(solution([1,2,3,4]))      # 2.5
print(solution([5,5]))          # 5