# 소수 만들기

# 문제 설명 : https://programmers.co.kr/learn/courses/30/lessons/12977
# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 
# 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, 
# nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 
# solution 함수를 완성해주세요.

# 1,2,3,4 -> 1+2+3=6, 1+2+4=7, 2+3+4=9

# 예상 풀이
# itertools 라이브러리를 사용하여 순열, 조합으로 해결할 수 있을듯??
# 에레토스테네스의 체??? 그거 사용??


# 문제 풀이(1)
import itertools
def PrimeNumber(n):
    if n < 2:
        return 0    
    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1

def solution(nums):
    answer = 0

    com = list(itertools.combinations(nums,3))
    result = []

    for i in com:
        result.append(sum(i))

    for j in result:
        if PrimeNumber(j):
            answer += 1

    # print(com, result)

    return answer

print(solution([1,2,3,4]))      # 1
print(solution([1,2,7,6,4]))    # 4