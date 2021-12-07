# 두 정수 사이의 합

# 문제설명 : https://programmers.co.kr/learn/courses/30/lessons/12912

# 예상풀이
# a <= b 일 때, a ~ b까지의 수를 더하고
# a > b 일 때, b ~ a까지의 수를 더하는 풀이다.

# 문제풀이(1)
def solution(a, b):
    answer = 0
    
    for i in range(a, b+1):
        answer += i
    
    if a>b:
        for j in range(b, a+1):
            answer += j

    return answer

print(solution(3, 5))   # 12
print(solution(3, 3))   # 3
print(solution(5, 3))   # 12