# 수박수박수박수박수박수? 

# 문제설명 : https://programmers.co.kr/learn/courses/30/lessons/12922

# 예상풀이
# 문자열 n의 i번째를 2로 나눈 나머지가 0이면, 
# i번째에 ‘수’를 반환하고, 0이 아니면 ‘박’을 반환한다

# 문제풀이(1)
def solution(n):
    answer = ''
    
    for i in range(n):
        if i % 2 == 0:
            answer += '수'
        else:
            answer += '박'
            
    return answer

# ‘수박’ 이란 문자를 n만큼 곱한 뒤
# 나열해서 문자를 n만큼 잘라서 사용한 것이다.
# 이 방법은 간단하게 풀고 넘어 갈 수 있기는 하나
# 메모리를 많이 사용하게 되어 효율성은 떨어진다고 한다.

# 다른 사람의 풀이(1)
def water_melon(n):
    s = "수박" * n
    return s[:n]

print(solution(3))      # "수박수"
print(solution(4))      # "수박수박"