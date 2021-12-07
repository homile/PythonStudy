# 문자열 내림차순으로 배치하기

# 문제설명 : https://programmers.co.kr/learn/courses/30/lessons/12917

# 예상풀이
# Sorted 함수를 사용해 문자열 s를 reverse = True로
# 내림차순으로 정렬한다.

# 문제풀이(1)
def solution(s):

    answer = "".join(sorted(s, reverse=True))

    return answer

print(solution("Zbcdefg"))      # "gfedcbZ"