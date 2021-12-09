
# 첫번째 풀이
# n = int(input())

# for i in range(2, n+1):
#     if n % i != 0 :  # n이 i로 나누어 떨어지면 소수가 아니다.
#         print(i)

# 두번째 풀이
# import math
# n = int(input())
# m = int(math.sqrt(n))
# arr = [True] * (n + 1)

# for i in range(2, m + 1) :
#     if arr[i] == True:
#         for j in range(i+i, n, i):
#             arr[i] = False

# print( [i for i in range(2, n) if arr[i] == True])

# 세번째 풀이
# 에라토스테네스의 체를 이용하여 소수를 찾는다.
# 에라토스테네스의 체
# 2부터 n까지의 숫자를 배열로 만든다.
# 2를 제외하고 2의배수를 만든 배열에서 제거한다.
# 1씩 커지면서 그숫자의 배수를 제거한다.
def solution(n):
    num_set = set(range(2, n+1))
    
    for i in range(2, n+1):
        if i in num_set:
            num_set -= set(range(i*2, n+1, i))
            
    answer = len(num_set)
    return answer
