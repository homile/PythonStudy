# [1차] 뉴스 클러스터링

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/17677
# 자카드 유사도: 집한 간의 유사도를 검사하는 여러 방법 중의 하나이며,
# 두 집합 A, B 사이의 자카드 유사도 J(A, B)는 두 집합의 교집합 크기를 
# 두 집합의 합집합 크기로 나누 값으로 정의된다.

# ex) A = {1,2,3}, B = {2,3,4}일 때, 교집합 AnB={2,3}, 합집합 AuB = {1,2,3,4}
# A, B 사이의 자카드 유사도 J(A, B) = 2/4 = 0.5가 된다.
# 집합 A와 집합 B가 모두 공집합일 경우에는 나눗셈이 정의되지 않으니 따로
# J(A, B) = 1로 정의한다.

# 교집합 = 공통으로 들어간 문자들, 합집합 = 중복없이 A, B를 합친 것

# 문제접근
# 집합문제는 python의 set함수를 사용할 수 있다.
# 교집합 = A & B, 합집합 =  A | B, 차집합 = A - B

# 대문자와 소문자를 구분할 필요는 없으니 소문자로 전부 치환한다.
# 예시와 같이 2문자씩 끊어줘야한다. 
# set함수를 사용하기 위해서 str1, str2를 리스트로 변경한다.

# 문제풀이(1)
from curses import A_ALTCHARSET


def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()

    str1_list = []
    str2_list = []

    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():   # 앞뒤가 모두 문자일 경우
            str1_list.append(str1[i:i+2])   # 2문자씩 끊어서 더해주기 위함

    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():   # 앞뒤가 모두 문자일 경우
            str2_list.append(str2[i:i+2])   # 2문자씩 끊어서 더해주기 위함

    # print(str1_list)
    # print(str2_list)

    intersection = set(str1_list) & set(str2_list)  # 교집합
    union = set(str1_list) | set(str2_list)         # 합집합

    print(intersection, union)

    return answer

# 2문자씩 끊은 문자열을 리스트에 넣었고
# 그 리스트 2개를 가지고 교집합과 합집합을 찾았다.
# 이제 찾은 값을 가지고 결과를 출력해야 한다.
# J("FRANCE", "FRENCH") = 2/8 = 0.25   -> 교집합/합집합


# 문제풀이(2)
def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()

    str1_list = []
    str2_list = []

    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():   # 앞뒤가 모두 문자일 경우
            str1_list.append(str1[i:i+2])   # 2문자씩 끊어서 더해주기 위함

    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():   # 앞뒤가 모두 문자일 경우
            str2_list.append(str2[i:i+2])   # 2문자씩 끊어서 더해주기 위함

    # print(str1_list)
    # print(str2_list)

    intersection = set(str1_list) & set(str2_list)  # 교집합
    union = set(str1_list) | set(str2_list)         # 합집합

    print(intersection, union)
    print(len(intersection), len(union))
    
    if len(intersection) == 0 or len(union) == 0:   # 공집합 일 경우
        answer = 65536
        return answer

    answer = int(len(intersection) / len(union) * 65536) # ZeroDivisionError: division by zero

    return answer

# TC3번이 풀리지 않음
# 합집합 = aa, 교집합 = aa로 값이 1 /1 *66536이 나왔음
# 해당 문제는 다중집합이 허용이된다.
# 그렇기 때문에 합집합 = aa,aa,aa 교집합 = aa,aa가 되어야한다.
# 그렇다면 어떻게 찾을 수 있을까?
# set함수를 사용하여 합집합과 교집합의 값을 가지고
# 주어진 문자열에서 비교하면 된다?


# 문제풀이(3)       # 84.6/100.0   2문제 틀림
def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()

    str1_list = []
    str2_list = []

    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():   # 앞뒤가 모두 문자일 경우
            str1_list.append(str1[i:i+2])   # 2문자씩 끊어서 더해주기 위함

    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():   # 앞뒤가 모두 문자일 경우
            str2_list.append(str2[i:i+2])   # 2문자씩 끊어서 더해주기 위함

    # print(str1_list)
    # print(str2_list)

    intersection = set(str1_list) & set(str2_list)  # 교집합
    union = set(str1_list) | set(str2_list)         # 합집합

    # print(intersection, union)
    # print(len(intersection), len(union))

    inter, uni = 0, 0
    for i in intersection:      # set 함수를 사용하여 중복 제거한 값을 찾아오기 위함.
        # print('count: ',min(str1_list.count(i),str2_list.count(i)))
        inter += min(str1_list.count(i),str2_list.count(i))

    for i in union:
        uni += max(str1_list.count(i), str2_list.count(i))

    if inter == 0 or uni == 0:   # 공집합 일 경우
        answer = 65536
        return answer
    
    print('count: ',inter, uni)

    answer = int(inter / uni * 65536) # ZeroDivisionError: division by zero

    return answer

# 5, 13번 틀리는 사람을 찾아보니
# 교집합이 0은 0이고, 합집합이 0인 것의 65536을 return 해야한다.
# 교집합 == 0 일때는 출력이 되고
# 합집합 == 0 일때는 ZeroDivisionError: division by zero에러가 난다


# 문제풀이(4)       통과
def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()

    str1_list = []
    str2_list = []

    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():   # 앞뒤가 모두 문자일 경우
            str1_list.append(str1[i:i+2])   # 2문자씩 끊어서 더해주기 위함

    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():   # 앞뒤가 모두 문자일 경우
            str2_list.append(str2[i:i+2])   # 2문자씩 끊어서 더해주기 위함

    # print(str1_list)
    # print(str2_list)

    intersection = set(str1_list) & set(str2_list)  # 교집합
    union = set(str1_list) | set(str2_list)         # 합집합

    # print(intersection, union)
    # print(len(intersection), len(union))

    if len(intersection) == 0 and len(union) == 0:   # 두 집합 모두 공집합 일 경우
        return 65536

    inter, uni = 0, 0
    for i in intersection:      # set 함수를 사용하여 중복 제거한 값을 찾아오기 위함.
        # print('count: ',min(str1_list.count(i),str2_list.count(i)))
        inter += min(str1_list.count(i),str2_list.count(i))

    for i in union:
        uni += max(str1_list.count(i), str2_list.count(i))
    
    print('count: ',inter, uni)

    answer = int(inter / uni * 65536) # ZeroDivisionError: division by zero

    return answer

print(solution('FRANCE', 'french'))             # 16384
print(solution('handshake', 'shake hands'))     # 65536
print(solution('aa1+aa2', 'AAAA12'))            # 43690
print(solution('E=M*C^2', 'e=m*c^2'))           # 65536


# 다른 사람의 풀이(1)
import re
import math

def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)

# 정규표현식과 math함수를 사용했다.
# floor 함수는 반올림,내림을 할 수 있는 함수이다.

print(solution('FRANCE', 'french'))             # 16384
print(solution('handshake', 'shake hands'))     # 65536
print(solution('aa1+aa2', 'AAAA12'))            # 43690
print(solution('E=M*C^2', 'e=m*c^2'))           # 65536