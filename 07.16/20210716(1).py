# 정수형 내림차순으로 배치하기

# 문제설명 : https://programmers.co.kr/learn/courses/30/lessons/12933

# 예상풀이
# 정수를 문자형으로 변환후 join으로 붙이기

# 문제풀이(1)
def solution(n):
    n = str(n)
    return int(''.join(sorted(n, reverse = True)))

print(solution(118372))     # 873211