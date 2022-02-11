# 내적

# 문제 설명 : https://programmers.co.kr/learn/courses/30/lessons/70128

# 예상 풀이
# a, b의 i번째 값들을 곱하고 그 값을 전체 더한다.

# 문제 풀이(1)
# def solution(a, b):
#     answer = 0
    
#     for i in range(len(a)):
#         answer += a[i]*b[i]
    
#     return answer

# 내부적 오류 발생 
# 단순한 오류인줄 알았으나
# len(a) == 0 일 경우의 오류 발생

# 문제 풀이(2)
def solution(a, b):
    answer = 0
    
    if len(a) == 0 : return answer
    
    for i in range(len(a)):
        answer += a[i]*b[i]
    
    return answer

print(solution([1,2,3,4], [-3,-1,0,2]))     # 3
print(solution([-1,0,1], [1,0,-1]))         # -2