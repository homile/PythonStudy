# N개의 최소 공배수

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/12953

# 문제접근
# 1 x 2 // (1,2) -> 2 // 1 = 2
# 2 x 6 // (2,6) -> 12 // 2 =  6

# 앞의 수와 뒤의 수의 최소 공배수를 구하는 것을 반복하면
# 모든 수의 최소 공배수가 나오게 된다.

# 문제풀이(1)
import math

def solution(arr):
    answer = 1	
    
    for i in arr:
        answer = answer*i // math.gcd(answer, i)
        print(answer)

    return answer


# 다른 사람의 풀이(1)
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def nlcm(num):
    num.sort()
    max_num = num[-1]
    # print (num, max_num)
    temp = 1
    for i in range(len(num)):
        # lcm = (a*b) / gcd
        # gcd = (a*b) / lcm
        temp = (num[i] * temp) / (gcd(num[i], temp))
        # print (temp)
    return temp

print(solution([2,6,8,14])) # 168
print(solution([[1,2,3]]))  # 6