# 같은 알파벳이 2개 붙어 있는 짝을 찾아서 pop을 한다.
# : 알파벳을 판별한다.
# 문자열 s가 빈배열이 된다면 1, 아니라면 0을 return

# 몇 번을 해야 할 지 모르니 while을 써야하나?
# 풀이(1)
# 바뀌었는지 판별하는 풀이가 없음 추가
# 바뀌지 않았을 경우의 풀이도 없음 추가 

# def solution(s):
#     answer = 0
#     s = list(s)     # 문자열을 리스트로 변환 (pop하기 위함)

#     while len(s) > 0:
#         front = s.pop(0)
#         if front == s[0]:
#             s.pop(0)
#         else:
#             s.append(front)

#     return answer

# print(solution("baabaa"))   # 1
# print(solution("cdcd"))     # 0


# 풀이(2)
# 다 바뀌었을 경우 len(s)가 0이면 1을 return하는 식 추가

# 하지만 다 바뀌지 않았을 경우 내부에서
# 계속 실행하는 상황 발생

# 예상 해결 방안
# 1. while의 조건을 바꾼다.
# 2. 또 다른 조건식을 추가한다.
# 3. while 대신 for을 사용한다.

# def solution(s):
#     answer = 0
#     s = list(s)     # 문자열을 리스트로 변환 (pop하기 위함)

#     while len(s) > 0:
#         front = s.pop(0)
#         if front == s[0]:
#             s.pop(0)
#         else:
#             s.append(front)
    
#     if len(s) == 0:
#         answer = 1

#     return answer

# print(solution("baabaa"))   # 1
# print(solution("cdcd"))     # 0

# 풀이(3)

def solution(s):
    answer = 0
    stack = []
    i = 0
    while i < len(s):
        front = s[i]
        if not stack:
            stack.append(front)
        elif front == stack[-1]:
            stack.pop()
        else:
            stack.append(front)
        # print(stack, front)
        i += 1
    
    if stack:
        answer = 0
    else:
        answer = 1

    return answer


print(solution("baabaa"))   # 1
print(solution("cdcd"))     # 0