# 문자열 다루기 기본

# 문제설명 : https://programmers.co.kr/learn/courses/30/lessons/12918

# 예상풀이
# len으로 길이를 비교하여 return하면된다.

# 제출 시 5,6번에서 실패하는 경우 발생
# 문자열의 길이를 판별??
# -,+를 구분??

# 문제풀이(1)
# def solution(s):
#     answer = s.isdigit()
#     return answer

# 문자열의 길이를 판독
# -와 +에 대한 제한 사항이 존재하지 않았음

# 문제풀이(2)
def solution(s):
    #초기값 지정
    answer = True  
    
    #문자열의 길이가 4 or 6 확인
    if((len(s) == 4) or len(s) == 6):
        if(s.isdigit() != answer):
            answer = False
    else:
        answer = False
    return answer

# 다른 사람의 풀이(1)
# def solution(s):
#     return s.isdigit() and len(s) in (4,6)

print(solution("a234"))    # false
print(solution("1234"))    # true