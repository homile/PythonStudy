# 숫자 문자열과 영단어

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/81301

# 문제접근
# 숫자 리스트와 문자열 리스트를 만들어야 할 것 같다.
# 문자와 숫자를 구분할 수 있는 함수 isdigt, alpha 함수 사용?
# 문자열을 추출한 후 숫자로 변환
# 순차적으로 숫자를 문자열로 붙인 후 정수형으로 변환?

# 문제풀이(1)
def solution(s):
    answer = 0
    s_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    a = ''			# 문자와 숫자 구분
    answer_s = ''	
    
    for i in range(len(s)):
        if s[i].isdigit() == False:
            a += s[i]
        else:
            answer_s += s[i]
        if a == 'one':
            answer_s += '1'
            a = ''
        elif a == 'seven':
            answer_s += '7'
            a = ''
        elif a == 'eight':
            answer_s += '8'
    
    print(a, answer_s)
        
    return int(answer_s)

# Testcase 1번만 통과


# 문제풀이(2)
def solution(s):
    answer = 0
    s_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    a = ''
    answer_s = ''
    
    for i in range(len(s)):
        if s[i].isdigit() == True:
            answer_s += s[i]
        else:
            a += s[i]
        
        if a == s_list[0]:
            answer_s += '0'
            a = ''
        elif a == s_list[1]:
            answer_s += '1'
            a = ''
        elif a == s_list[2]:
            answer_s += '2'
            a = ''
        elif a == s_list[3]:
            answer_s += '3'
            a = ''
        elif a == s_list[4]:
            answer_s += '4'
            a = ''
        elif a == s_list[5]:
            answer_s += '5'
            a = ''
        elif a == s_list[6]:
            answer_s += '6'
            a = ''
        elif a == s_list[7]:
            answer_s += '7'
            a = ''
        elif a == s_list[8]:
            answer_s += '8'
            a = ''
        elif a == s_list[9]:
            answer_s += '9'
            a = ''
    
    print(a, answer_s)
        
    return int(answer_s)

# 재귀 함수만으로 풀이를 하였다
# 이 방법으로 제출이 되지만
# 조금 더 좋은 방법을 찾아본 결과
# dictionary를 사용하면 될 것 같다는 생각이 들었다.

# 다음 풀이는 dictionary를 사용하여 풀어볼 것


# 문제풀이(3)
def solution(s):
    answer = s
    s_dic = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 
              'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    
    for key, value in s_dic.items():
        answer = answer.replace(key, value)
        
    return int(answer)

# list를 dictionary로 변경 후
# replace함수를 사용하여 
# key의 값이 나온다면 value의 값으로 변환한다.

# dictionary 사용법과 
# replace 함수 사용법을 다시 한번 정리해본다.


print(solution("one4seveneight"))   # 1478
print(solution("23four5six7"))      # 234567
print(solution("2three45sixseven")) # 234567
print(solution("123"))              # 123

