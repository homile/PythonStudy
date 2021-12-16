# 다음 큰 숫자

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/12911

# 문제접근
# 2진수도 변환하는 함수 bin을 사용하면 편할 듯?

# 2진수 1의 개수가 같은 다음으로 큰 수를 찾으면 됨

# 그럼 2진수의 1의 개수를 판별하는 법?
# (count 함수 사용 if문 비교)

# 문제풀이(1)
def solution(n):
    answer = n
    n = bin(n).count('1')
    
    while True:
        answer += 1
        if bin(answer).count('1') == n :
            break
        
    print(n)
    return answer

# answer에 n 값을 넣음
# n을 2진수로 바꾼 다음 1의 개수를 count함

# 얼마나 나올지 몰라 while로 무한으로 돌리고
# answer를 2진수로 바꾸고 1의 개수를 count한 값이
# n과 같으면 break 문으로 멈춤

# 2진수를 bin으로 말고 저번에 풀었던 방식으로 해보자

print(solution(78))     # 83
print(solution(15))     # 23