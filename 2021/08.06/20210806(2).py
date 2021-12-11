# 콜라츠 추측

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/12943

# 문제접근

# 문제풀이(1)
def solution(num):
    answer = 0
    while True:
        if num == 1 :          # num이 1이면 반복할 이유가 없음
            break
        if answer > 500 :  # 500이상 반복하면 -1 return
            answer = -1
            break
        elif num % 2 == 0:  # 짝수일 때
            num = num / 2
        else:
            num = (num * 3) + 1  # 홀수일 때
        
        answer += 1
        
    return answer


# 다른 사람의 풀이(1)
def collatz(num):
    for i in range(500):
        num = num / 2 if num % 2 == 0 else num*3 + 1
        if num == 1:
            return i + 1
    return -1

print(solution(6))      # 8
print(solution(16))     # 4
print(solution(626331)) # -1