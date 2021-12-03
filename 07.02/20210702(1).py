# 최대공약수와 최소공배수

# 문제설명 : https://programmers.co.kr/learn/courses/30/lessons/12940

# 예상풀이
# 두 정수 중 작은 값을 먼저 구한 후 1부터 작은 값에 1을 더한 수 만큼 
# n과 m의 나머지가 0인 값을 구해서 GCD를 구하고
# n * m / gcd를 하여 LCM을 구하는 방식이다.

# 문제풀이(1)
# def solution(n, m):
    
#     if n > m:
#         small = m
#     else:
#         small = n
        
#     for i in range(1, small+1):
#         if((n % i == 0) and (m % i ==0)):
#             gcd = i
            
#     return gcd, n * m / gcd


# Math 라이브러리의 내장함수 gcd를 사용하여 최대공약수를 구하고 
# 그 값을 사용하여 최소공배수까지 구하는 방법이다.
# 라이브러리를 사용하는 방식은 현업에서 사용하기 적합하나
# 코딩 테스트를 하는 과정에는 좋지 않다고 생각한다.

# 문제풀이(2)
import math

def solution(n, m):
    answer = [math.gcd(n, m), int(n*m/math.gcd(n,m))]    
    return answer


# 유클리드 호제법을 사용함.

# 다른 사람의 풀이(1)
def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    while d :
        c, d = d, c % d
    answer = [c, int(a*b/c)]

    return answer


print(solution(3, 12))      # [3, 12]
print(solution(2, 5))       # [1, 10]