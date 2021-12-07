# 약수의 합

# 문제설명 : https://programmers.co.kr/learn/courses/30/lessons/12928

# 예상풀이
# N의 수를 1부터 시작하는 i로 나눈 나머지가 0 이면
# 약수이기 때문에 answer에 약수를 더해준다.

# 문제풀이(1)
def solution(n):
    answer = 0
    
    for i in range(1, n+1):
        if n % i == 0:
            answer += i
            
    return answer


# 다른 사람의 풀이(1)
# def sumDivisor(num):

#     # num / 2 의 수들만 검사하면 성능 약 2배 향상
#     return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])

print(solution(12))     # 28
print(solution(5))      # 6