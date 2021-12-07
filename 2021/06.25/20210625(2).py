# 문자열을 정수로 바꾸기

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/12925

# 예상풀이
# string s를 숫자로 변환하여 판별

# 문제풀이(1)
def solution(s):
    answer = 0
    # 문자열의 길이 확인
    if len(s) >= 1 and len(s) <= 5:
        # 부호의 존재여부 확인
        if(s[0] == ('+','-')):
            answer = int(s[0:])
        else:
            answer = int(s[0:])
    return answer


# 그냥 int를 str형으로 변환시에는
# 문자열의 길이, 부호등은 생각하지 않아도 된다.

# 다른 사람의 풀이(1)
# def solution(s):
#     answer = int(s) 
            
#     return answer


# 슬라이싱으로 문자열을 거꾸로 만들어 준다.
# enumerate 함수를 사용하여 한 글자당 인덱스를 배정해서
# 각 자리에 10의 지수만큼 곱해서 더해주는 방식이다.

# 다른 사람의 풀이(2)
def solution(s) : 
    answer = 0

    for idx, number in enumerate ( s[::-1]):
        if number == '-':
            answer *= -1
        else:
            answer += int(number) * (10 ** idx)

    return answer 

print(solution("1234"))     # 1234
print(solution("-1234"))    # -1234