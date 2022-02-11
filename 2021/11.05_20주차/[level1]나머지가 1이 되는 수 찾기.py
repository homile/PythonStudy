# 나머지가 1이 되는 수 찾기

# 문제 설명
# 자연수 n이 매개변수로 주어집니다. 
# n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 
# return 하도록 solution 함수를 완성해주세요. 
# 답이 항상 존재함은 증명될 수 있습니다.

# 제한사항
# 3 ≤ n ≤ 1,000,000


# 예상 풀이
# n % i를 하면됨

# 문제 풀이(1)
# def solution(n):
#     answer = 0
    
#     for i in range(1, n):
#         if n % i == 1:
#             answer = i
#     return answer

# 실패 요인 = 나머지가 1이되는 자연수 중 
# 작은 값을 출력해야하는 것을 잊음
# 1. n%i == 1이면 i 값을 return
# 2. n%i를 한 값을 배열에 쌓은 뒤 min으로 가장 작은 값을 추출

# 문제 풀이(2)
def solution(n):
    answer = 0

    
    for i in range(1, n):
        if n % i == 1:
            answer = i
            break
    return answer
    
print(solution(10))     # 3
print(solution(12))     # 11

# # 다른 사람의 풀이(1)
# def solution(n):
#     answer = min([x for x in range(1, n+1) if n % x == 1])
#     return answer