# JadenCase 문자열 만들기

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/12951

# 문제접근
# 공백을 기준으로 문자열을 나눠주고
# 문자열을 모두 소문자로 바꾼 다음
# 문자의 첫 시작 알파벳을 대문자로 바꾼다.
# upper() = 대문자, lower() = 소문자

# 문자의 첫 글자를 대문자로 바꿔주는 함수가 있을까?

# 문제풀이(1)
def solution(s):
    answer = ''
    s = s.split(' ')	 
    
    for i in range(len(s)): 
        a = ''
        s[i] = s[i].lower()
        a = s[i]
        a = a[0].upper() + a[1:]
        s[i] = a
    
    return ' '.join(s)

# 문자열을 공백을 기준으로 끊어 줌

# 문자를 전체를 소문자로 바꿈
# a에 문자를 담고
# 문자에서 첫번쨰를 대문자로 바꾸고 뒤에 나머지 소문자를 채움

# join을 통해 리스트에 담긴 문자를 붙여서 문자열로 만듦
# 테스트 케이스는 통과하였으며 제출 시 43.8/100으로 
# 런타임 에러가 많이 남 (첫 문자를 대문자로 하는 함수 사용??)


# 문제풀이(2)
def solution(s):
    answer = ''
    s = s.lower()
    s = s.split(' ')
    
    for i in s:
        i = i.capitalize()
        answer += i + ' '
        
    return answer[:-1]

# 처음에 문자를 전부 소문자로 변경
# 공백을 기준으로 나눔

# capitalize() 함수를 이용하여 
# 단어의 첫 알파벳을 대문자로 변경

# 마지막에 추가된 공백을 제거하기위해 slicing사용


# 다른 사람의 풀이(1)
def Jaden_Case(s):
    
    return s.title()

print(solution("3people unFollowed me"))    # "3people Unfollowed Me"
print(solution("for the last week"))        # "For The Last Week"