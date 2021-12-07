# 약수의 개수와 덧셈

# 문제설명 : https://programmers.co.kr/learn/courses/30/lessons/77884

# 예상풀이


# 문제풀이(1)
def solution(left, right):
    answer = 0

    for i in range(left, right+1):
        count = 0
        for j in range(i):
            if (j == 0 or i % j == 0):
                count += 1

        if (count % 2 != 0):
            answer -= i           # 약수의  개수가 짝수가 아닐 때       
        else:
            answer += i          # 약수의  개수가 짝수 일 때 

    return answer


# 제곱수는 약수의 개수가 홀수인 것을 활용한 풀이이다.

# 다른 사람의 풀이(1)
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer

print(solution(13, 17))     # 43
print(solution(24, 27))     # 52 