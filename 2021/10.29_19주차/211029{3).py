# "aabbaccc" -> "2a2ba3c" 문자가 반복되지 않아 
# 한번만 나타난 경우 1은 생략

# 1, 2, 3, ... 의 자릿수로 잘랐을 경우를 판별해야함
# 슬라이싱으로  1, 2, 3, ...의 자릿수를 자르고
# 맞는지 판별하면 된다.
# 문제 풀이(1)
# def solution(s):
#     answer = 0
#     stack = []

#     for i in range(1, len(s)//2+1):
#         stack.append(s[:i])
#     print(stack)

#     return answer


# 문자열을 list에 슬라이싱해서 넣어봄.

# 해야 할 것
# 1. 슬라이싱 한 값을 비교하여 2a2b3c로 변경
# 2. 굳이 리스트에 넣어야 하나??
# 3. 슬라이싱 한 값 뒤에랑 비교해야함


# # 문제 풀이(2)
# def solution(s):
#     answer = 0

#     for i in range(1, len(s)//2+1):
#         temp = s[:i]
#         cnt = 1
#         for j in range(i, len(s),i):
#             if s[j: j+i] == temp:
#                 print(temp)
#                 cnt += 1
#             else:
#                 cnt = 1

#     print(temp, cnt)

#     return answer


# # 문제 풀이(3)
# def solution(s):
#     answer = 0
#     a_list = []     # 슬라이싱 한 값을 비교하여 2a2b3c로 변경

#     for i in range(1, len(s)//2+1):
#         temp = s[:i]
#         cnt = 1
#         for j in range(i, len(s),i):
#             if s[j: j+i] == temp:
#                 # print(temp)
#                 cnt += 1
#             else:
#                 if cnt == 1:    # 숫자가 1이면 1을 삭제
#                     cnt = ""
#                 answer += str(cnt)+temp    # 숫자와 문자열 합성
#                 # print(answer)
#                 cnt = 1
#         if cnt == 1:
#             cnt = ""
#         answer += str(cnt)+temp
#         a_list.append(len(temp))
#         temp=""
        

#     # print(temp, cnt)
#     print(a_list)

#     return answer

# # 문제 풀이(4)
# def solution(s):
#     answer = 0
#     a_list = []     # 슬라이싱 한 값을 비교하여 2a2b3c로 변경

#     for i in range(1, len(s)//2+1):
#         result = ''
#         temp = s[:i]
#         cnt = 1
#         for j in range(i, len(s),i):
#             if s[j:j+i] == temp:
#                 # print(temp)
#                 cnt += 1
#             else:
#                 if cnt == 1:    # 숫자가 1이면 1을 삭제
#                     result += temp
#                 else:
#                     result += str(cnt)+temp    # 숫자와 문자열 합성
#                     cnt = 1
#                 # print(answer)
#         if len(s[j:j+i])==1:
#             if cnt == 1:
#                 result += temp
#             else:
#                 result += str(cnt)+temp
#                 cnt = 1
#         else:
#             result += s[j:j+i]
#         a_list.append(len(result))
        

#     # print(temp, cnt)
#     print(a_list)

#     return min(a_list)


# 문제 풀이(5)
def solution(s):
    answer = s
    minLen = len(s)

    # 문자열을 1개~len(s)/2개씩 각 단위만큼 잘라서 압축
    for unit in range(1, len(s) // 2 + 1):
        tempAnswer = ""
        temp = s[:unit]
        cnt = 1
        for i in range(unit, len(s), unit):
            if temp == s[i:i+unit]:
                cnt += 1
            else:
                if cnt == 1:
                    tempAnswer += temp
                else:
                    tempAnswer += str(cnt) + temp
                cnt = 1
                temp = s[i:i+unit]

        # 마지막 문자 넣어주기
        if cnt == 1:
            tempAnswer += temp
        else:
            tempAnswer += str(cnt) + temp

        if len(tempAnswer) < minLen:
            answer = tempAnswer
            minLen = len(answer)

    return len(answer)

print(solution("aabbaccc"))                 # 7 | 2a2ba3c
print(solution("ababcdcdababcdcd"))         # 9 
print(solution("abcabcdede"))               # 8
print(solution("abcabcabcabcdededededede")) # 14
print(solution("xababcdcdababcdcd"))        # 17