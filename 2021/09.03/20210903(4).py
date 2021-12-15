# 숫자의 표현

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/12924

# 문제접근

# 문제풀이(1)
def solution(n):
    answer = 0
    for i in range(1, n+1):
        # print(i)
        cnt = 0
        for j in range(i, n+1):
            # print(j)
            cnt += j
            
            if cnt == n:
                answer += 1
                break
            elif cnt > n:
                break
    return answer


# 다른 사람의 풀이(1)
def expressions(num):
    return len([i  for i in range(1,num+1,2) if num % i is 0])

# 자기보다 작은 홀수로 나누어 떨어지는 값의 개수가 이 답의 개수와 같음

print(solution(15))     # 4