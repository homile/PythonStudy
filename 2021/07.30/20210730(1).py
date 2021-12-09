# 소수 찾기

# 문제설명

# 예상풀이
# n이 i로 나누어 떨어지면 소수가 아니다.
# 이 풀이는 문제를 잘못이해한 것이다.
# 찾아본 결과 에라토스테네스의 체의 공식을 사용한다.

# 문제풀이(1)
def solution(n):
    answer = 0

    for i in range(2, n+1):
        if n % i != 0 :  # n이 i로 나누어 떨어지면 소수가 아니다.
            answer += i

    return answer


# math 라이브러리를 사용하여 소수를 판별하는 식을 구했다.
# 하지만 이는 소수를 판별하기만 하고 개수를 구하지는 못했다.

# 문제풀이(2)
# import math
# def solution(n):
#     arr = [True] * (n + 1)
#     m = int(math.sqrt(n))

#     for i in range(2, m + 1) :
#         if arr[i] == True:
#             for j in range(i+i, n, i):
#                 arr[i] = False

#     return [i for i in range(2, n) if arr[i] == True]


# 에라토스테네스의 체를 이용하여 소수를 찾는다.
# 에라토스테네스의 체
# 2부터 n까지의 숫자를 배열로 만든다.
# 2를 제외하고 2의배수를 만든 배열에서 제거한다.
# 1씩 커지면서 그 숫자의 배수를 제거한다.

# 문제풀이(3)
def solution(n):
    num_set = set(range(2, n+1))        	# 2부터 n까지의 값을 넣어준다. 
    
    for i in range(2, n+1):		
        if i in num_set:
            num_set -= set(range(i*2, n+1, i))
            
    answer = len(num_set)
    return answer

print(solution(10))     # 4
print(solution(5))      # 3