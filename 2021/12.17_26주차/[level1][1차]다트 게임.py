# [1차]다트 게임

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/17682
# s = 1제곱, d = 2제곱, t = 3제곱
# * = 스타상 -> 당첨 시 해당 점수와 바로 전에 얻은 점수를 각 2배로 만든다.
# # = 아차상 -> 당첨 시 해당 점수는 마이너스 된다.

# 문제접근
# 숫자와 문자를 구분한다.
# 구분한 숫자를 다른 배열에 담는다. (스타상 조건에 맞추기 위해)
# 문자를 확인하여 조건에 맞게 계산한다.

# 문제풀이(1)       81.3/100.0
def solution(dartResult):
    answer = 0
    num = 0
    score = []

    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            num += int(dartResult[i])
        else:
            if dartResult[i] == 'S':
                num = int(num) ** 1
                score.append(num)
                num = 0
            elif dartResult[i] == 'D':
                num = int(num) ** 2
                score.append(num)
                num = 0
            elif dartResult[i] == 'T':
                num = int(num) ** 3
                score.append(num)
                num = 0
            elif dartResult[i] == '*':
                if len(score) > 1:
                    score[-2] = score[-2] * 2
                    score[-1] = score[-1] * 2
                else:
                    score[-1] = score[-1] * 2
            elif dartResult[i] == '#':
                score[-1] = score[-1] * -1

        # print(num, score)

    answer = sum(score)

    return answer

# TC2번 통과하지 못함. 제출 점수: 81.3/100.0
# 내가 추출한 값 = 1, -2, 1 = 0
# 정답 = 9
# 10의 1승인데 1+0으로 계산함
# num을 str로 받은 다음에 계산시 int로 형변환해야 할 듯


# 문제풀이(2)   통과
def solution(dartResult):
    answer = 0
    num = ''
    score = []

    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            num += dartResult[i]
        else:
            if dartResult[i] == 'S':
                num = int(num) ** 1
                score.append(num)
                num = ''
            elif dartResult[i] == 'D':
                num = int(num) ** 2
                score.append(num)
                num = ''
            elif dartResult[i] == 'T':
                num = int(num) ** 3
                score.append(num)
                num = ''
            elif dartResult[i] == '*':
                if len(score) > 1:
                    score[-2] = score[-2] * 2
                    score[-1] = score[-1] * 2
                else:
                    score[-1] = score[-1] * 2
            elif dartResult[i] == '#':
                score[-1] = score[-1] * -1

        # print(num, score)

    answer = sum(score)

    return answer

# 통과
# 하지만 코드의 중복이 상당히 많아보임


# 문제풀이(3)
def solution(dartResult):
    answer = 0
    num = ''
    score = []

    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            num += dartResult[i]
        elif dartResult[i] == 'S':
            score.append(int(num) ** 1)
            num = ''
        elif dartResult[i] == 'D':
            score.append(int(num) ** 2)
            num = ''
        elif dartResult[i] == 'T':
            score.append(int(num) ** 3)
            num = ''
        elif dartResult[i] == '*':
            if len(score) > 1:
                score[-2] *= 2
                score[-1] *= 2
            else:
                score[-1] *= 2
        elif dartResult[i] == '#':
            score[-1] *= -1

        # print(num, score)

    answer = sum(score)

    return answer


# 다른 사람의 풀이(1)
import re

def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    s = re.compile('(\d+)([SDT])([*#]?)')   # complie -> 객체변환 ?는 빈칸 
    print(s)
    print(s.findall(dartResult))            # findall ->
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer

# re 라이브러리를 사용 (정규표현식)
# bonus, option을 딕셔너리로 표현
# 키값과 일치하면 속성 값을 출력하여 표현
# https://brownbears.tistory.com/506 // findall

print(solution("1S2D*3T"))      # 37
print(solution("1D2S#10S"))     # 9	
print(solution("1D2S0T"))       # 3	
print(solution("1S*2T*3S"))     # 23	
print(solution("1D#2S*3S"))     # 5	
print(solution("1T2D3D#"))      # -4	
print(solution("1D2S3T*"))      # 59	