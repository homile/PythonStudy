# 문자열 내 p와 y의 개수

# 문제설명 : https://programmers.co.kr/learn/courses/30/lessons/12916

# 예상풀이
# 변수 p에 소문자 p와 대문자 P의 개수를 카운트 하고,
# 변수 y에 소문자 y와 대문자 Y의 개수를 카운트 한다.
# 변수 p와 y의 개수가 같으면 True를 return 하고,
# 개수가 다르면 False를 return 한다.

# 문제풀이(1)
def solution(s):
    
    p = s.count('p') + s.count('P')
    y = s.count('y') + s.count('Y')
    
    if(p == y):
        return True
    else:
        return False


# 대문자와 소문자를 나의 풀이와 같이 따로 count 하는 것이 아닌
# 모든 문자를 소문자로 변환 시킨 뒤 p와 y의 개수를 count 하는 방식이다.
# 이와 같은 방법으로 모든 문자를 대문자(upper 사용)로 변경하여 
# count 하는 방식도 할 수 있다.

# 다른 사람의 풀이(1)
def numPY(s):
    
    return s.lower().count('p') == s.lower().count('y')

print(solution("pPoooyY"))      # true
print(solution("Pyy"))          # false