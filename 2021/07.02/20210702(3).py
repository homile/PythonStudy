# 이상한 문자 만들기

# 문제설명 : https://programmers.co.kr/learn/courses/30/lessons/12930

# 예상풀이

# 문제풀이(1)
def solution(s):
    s = s.split(' ')          #문자열을 공백을 기준으로 나눔
    result = []
    
    for j in s:
        answer = ''
        for i in range(len(j)):
            if (i % 2 == 0):              # i번째 문자를 2로 나눠서
                answer += j[i].upper()    # 나머지가 0이면 대문자
            else:  
                answer += j[i].lower()
        result.append(answer)  # 변경한 문자를 result에 반환

    return ' '.join(result)       # 문자들을 공백으로 연결


# 푸는 방식은 나의 풀이와 비슷하지만 map, lamda, enumerate 함수를 사용하여
# 각 문자에 index를 생성한 뒤 열거형으로 푼 것이다. 


# 다른 사람의 풀이(1)
def toWeirdCase(s):

    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))

print(solution("try hello world"))      # "TrY HeLlO WoRlD"