# 신규 아이디 추천

# 문제 설명 : https://programmers.co.kr/learn/courses/30/lessons/72410
# 3 <= 아이디의 길이 <= 15
# 아이디는 알파벳 소문자, 숫자, -, _, .만 사용가능
# 단, 마침표는 처음과 끝에 사용할 수 없으며 연속으로 사용할 수 없음

# 예상 풀이
# 1. 대문자 -> 소문자로 변경 (lower사용)
# 2. 마침표 중복사용 제거
# 3. 16자 이상일 경우 앞의 15자만 사용
# 4. 마침표 위치에 따른 사용유무 판단
# 5. 2자 이하일 경우 마지막 문자를 뒤에 더해서 3이상으로 만들기

# 문자열을 스택으로 바꿔서???

# 문제 풀이(1)
# def solution(new_id):
#     answer = ''
#     # 소문자로 치환
#     new_id = new_id.lower()

#     if len(new_id) == 0:
#         new_id ='a'
#     elif len(new_id) <= 2:
#         new_id += new_id[-1] 

#     answer = new_id

#     return answer



# # 문제 풀이(2)
# def solution(new_id):
#     answer = ''
    
#     # 소문자로 치환
#     new_id = new_id.lower()

#     # 소문자, 숫자, -,_,.일 경우의 문자만 answer에 추가 (isalnum()도 사용가능)
#     for i in new_id:
#         if i.islower() or i.isdigit() or i in ["-","_","."]:
#             answer += i

#     # new_id가 공백일 경우 a를 추가
#     if len(new_id) == 0:
#         answer ='a'
#     # new_id가 2이하일경우 마지막 문자를 추가
#     elif len(answer) <= 2:
#         answer += answer[-1] 
#     # new_id가 16이상일경우 15자리까지 출력
#     elif len(answer) >= 16:
#         answer = answer[:15]

#     return answer

# 추가 조건
# 마침표가 연속일 경우 하나로 변경
# 마침표의 위치가 맨 앞, 뒤 일경우 삭제

# # 문제 풀이(3)
# def solution(new_id):
#     answer = ''
    
#     # 소문자로 치환
#     new_id = new_id.lower()

#     # 소문자, 숫자, -,_,.일 경우의 문자만 answer에 추가 (isalnum()도 사용가능)
#     for i in new_id:
#         if i.islower() or i.isdigit() or i in ["-","_","."]:
#             answer += i

#     # 마침표가 연속일 경우 .으로 치환
#     while '..' in answer:
#         answer = answer.replace('..','.')

#     # 마침표가 맨 처음일 경우 2번째부터 answer에 대입
#     if answer[0] == '.':
#         answer = answer[1:]
    
#     if answer[-1] == '.':
#         answer = answer[:-1]

#     # new_id가 공백일 경우 a를 추가
#     if len(answer) == 0:
#         answer ='a'

#     # new_id가 2이하일경우 마지막 문자를 추가
#     while len(answer) <= 2:
#         answer += answer[-1] 

#     # new_id가 16이상일경우 15자리까지 출력
#     if len(answer) >= 16:
#         answer = answer[:15]
#         if answer[-1] == '.':
#             answer = answer[:-1]

#     return answer

# 서순문제

# 문제 풀이(4)
def solution(new_id):
    answer = ''
    
    # 소문자로 치환
    new_id = new_id.lower()

    # 소문자, 숫자, -,_,.일 경우의 문자만 answer에 추가 (isalnum()도 사용가능)
    for i in new_id:
        if i.islower() or i.isdigit() or i in ["-","_","."]:
            answer += i

    # 마침표가 연속일 경우 .으로 치환
    while '..' in answer:
        answer = answer.replace('..','.')

    # 마침표가 맨 처음일 경우 2번째부터 answer에 대입
    if answer[0] == '.':
        answer = answer[1:]    

    # answer가 공백일 경우 a를 추가
    if len(answer) == 0:
        answer ='a'

    # 마침표가 맨 처음일 경우 2번째부터 answer에 대입
    if answer[0] == '.':
        answer = answer[1:] 
        
    if answer[-1] == '.':
        answer = answer[:-1]

    # answer가 2이하일경우 마지막 문자를 추가
    while len(answer) <= 2:
        answer += answer[-1] 

    # answer가 16이상일경우 15자리까지 출력
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    return answer

# 다른 사람의 풀이(1)

# re(정규식 연산) 라이브러리 사용 https://docs.python.org/ko/3/library/re.html
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st

print(solution("...!@BaT#*..y.abcdefghijklm"))  # "bat.y.abcdefghi"
print(solution("z-+.^."))                       # "z--"
print(solution("=.="))                          # "aaa"
print(solution("123_.def"))                     # "123_.def"
print(solution("abcdefghijklmn.p"))             # "abcdefghijklmn"