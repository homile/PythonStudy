# 서울에서 김서방 찾기

# 문제설명 : https://programmers.co.kr/learn/courses/30/lessons/12919

# 예상풀이
# 리스트 seoul의 길이를 찾은 뒤
# Seoul의 i번째 문자가 Kim일 경우
# 김서방은 i에 있다 라고 출력


# 문제풀이(1)
def solution(seoul):
    answer = ''
    
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            answer = "김서방은 %d에 있다" % i
    
    return answer

print(solution(["Jane", "Kim"]))    # "김서방은 1에 있다"