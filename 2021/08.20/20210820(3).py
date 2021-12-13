# 124 나라의 숫자

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/12899

# 문제접근
# 11 일 경우 처음 생각은10에 1이 붙어 
# 411일 것으로 예상했으나
# 1에 1이 붙어 11인 것을 인지 한 후 다시 시행

# 문제풀이(1)
# def solution(n):
#     answer = ''
#     a = [1,2,4]
#     answer = str(a[n%3]-1)
#     return answer

# 삼진법으로 해보려 했으나 정확히 확인하지 못함


# 문제풀이(2)
def solution(n):
    answer = ''
    a = ['1','2','4']
    
    while n > 0:
        n -= 1
        answer = a[n%3] + answer
        print(a[n%3], answer, n)
        n //= 3
        print(n)
        
    return answer


# 다른 사람의 풀이(1)
def change124(n):
    if n<=3:
        return '124'[n-1]
    else:
        q, r = divmod(n-1, 3) 
        return change124(q) + '124'[r]


print(solution(1))  # 1
print(solution(2))  # 2
print(solution(3))  # 4
print(solution(4))  # 11