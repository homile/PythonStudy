# 짝수와 홀수

# 문제설명 : https://programmers.co.kr/learn/courses/30/lessons/12937

# 예상풀이
# 정수 n의 i번째를 2로 나눈 나머지가 0이면, 
# Even를 반환하고, 0이 아니면 Odd를 반환한다.
# Answer 변수에 값을 지정하지 않고 바로 반환하는 방법을 
# 사용해도 됐다.

# 문제풀이(1)
def solution(num):

    if (num % 2 == 0):
        answer = "Even"
    else:
        answer = "Odd"
        
    return answer

print(solution(3))      # "Odd"
print(solution(4))      # "Even"