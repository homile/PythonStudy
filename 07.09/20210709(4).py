# 가운데 글자 가져오기

# 문제설명 : https://programmers.co.kr/learn/courses/30/lessons/12903

# 예상풀이
# 문자열의 길이를 2로 나눈 나머지 값이 0 일 때,
# 문자열 길이 / 2 -1 : 문자열 길이 / 2 + 1를 해서
# 중간 값에서 2개의 문자를 가져올 수 있다.

# 문제풀이(1)
def solution(s):
    answer = ''
    if len(s) % 2 == 0:
        answer = s[len(s) // 2 - 1 : len(s) // 2 + 1]
    else:
        answer = s[len(s) // 2]
        
    return answer


# 다른 사람의 풀이(1)
# If문을 사용하지 않고 푸는 방법이다.
def string_middle(str):

    return str[(len(str)-1)//2:len(str)//2+1]

print(solution("abcde"))        # "c"
print(solution("qwer"))         # "we"