# 이진 변환 반복하기

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/70129
# 문제 설명
# 0과 1로 이루어진 어떤 문자열 x에 대한 이진 변환을 다음과 같이 정의합니다.

# x의 모든 0을 제거합니다.
# x의 길이를 c라고 하면, x를 "c를 2진법으로 표현한 문자열"로 바꿉니다.
# 예를 들어, x = "0111010"이라면, x에 이진 변환을 가하면 
# x = "0111010" -> "1111" -> "100" 이 됩니다.

# 0과 1로 이루어진 문자열 s가 매개변수로 주어집니다. 
# s가 "1"이 될 때까지 계속해서 s에 이진 변환을 가했을 때, 
# 이진 변환의 횟수와 변환 과정에서 제거된 모든 0의 개수를 각각 배열에 담아 
# return 하도록 solution 함수를 완성해주세요.

# 제한사항
# s의 길이는 1 이상 150,000 이하입니다.
# s에는 '1'이 최소 하나 이상 포함되어 있습니다.

# 문제접근
# 1. 변환 이전의 이진수에서 0을 제거한다.
# 2. 0을 제거후 남은 문자의 길이를 계산한다.
# 3. 계산한 값을 이진수로 변환한다.
# 위의 1~3번을 남은 문자의 길이가 1이 될때까지 반복한다.

# 이진수를 계산하는 공식을 써야한다.

# 문제풀이(1)
def zeroDel(s):     # 0제거
    one = ''
    for i in range(len(s)):
        if s[i] != '0':
            one += s[i]

    return one

def solution(s):
    answer = [0,0]
    cnt, zero = 0, 0

    while s != '1':             # s가 '1'이 아닐때 loop
        zero += s.count("0")    # 제거할 0의 개수
        cnt += 1                # 2진수 변환 횟수
        s = zeroDel(s)          # 0제거
        s = bin(len(s))[2:]     # 0을 제거한 s의 길이를 2진수로 변환
    
    answer[0] = cnt
    answer[1] = zero

    return answer

# 0을 제거하는 함수를 추가하여 실행하였지만
# python에서는 replace라는 함수가 존재한다.

# 이것을 사용하여 한번더 풀어보자.


# 문제풀이(2)
def solution(s):
    answer = [0,0]
    cnt, zero = 0, 0

    while s != '1':             # s가 '1'이 아닐때 loop
        zero += s.count("0")    # 제거할 0의 개수
        cnt += 1                # 2진수 변환 횟수
        s = s.replace('0', '')
        s = bin(len(s))[2:]     # 0을 제거한 s의 길이를 2진수로 변환
    
    answer[0] = cnt
    answer[1] = zero

    return answer

# replace를 사용한 결과 함수를 호출하여 풀이한 문제보다
# 속도가 빨라졌다.

print(solution("110010101001"))     # [3,8]
print(solution("01110"))            # [3,3]
print(solution("1111111"))          # [4,1]