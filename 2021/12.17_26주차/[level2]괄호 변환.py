# 괄호 변환

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/60058
# 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
# 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 
#    단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, 
#    v는 빈 문자열이 될 수 있습니다. 
# 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
#   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
# 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
#   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
#   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
#   4-3. ')'를 다시 붙입니다. 
#   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
#   4-5. 생성된 문자열을 반환합니다.

# 문제접근
# 위에 나와있는 조건에 맞게 구현하면 될 것 같음
# 균형잡힌 괄호 문자열? -> ()   /  ))((  이런식으로 괄호의 개수가 맞는 것

# 참고사이트: https://kdgt-programmer.tistory.com/51

# 문제풀이(1)
def solution(p):
    answer = ''

    if p == '' : return answer      # 1. 빈 문자열인 경우

    left = 0
    right = 0
    for i in range(len(p)): # 2
        if p[i] == '(':
            left += 1       # 열린괄호의 개수 카운트
        else:
            right += 1      # 닫힌괄호의 개수 카운트
    
        if left == right:   # 열린괄호와 닫힌괄호의 개수가 같은 균형잡인 괄호 문자열일 경우
            u = p[:i+1]     # 두 균형잡힌 문자열 u, v를 생성
            v = p[i+1:]
            print(i, u, v)
            break

    return answer

# 문제의 조건 1,2 해결
# 3,4를 해결하면 된다. 
# 어떻게?  조건대로 ~!


# 문제풀이(2)
def check(s):
    count = 0
    for i in s:
        if i == '(':
            count += 1
        else: 
            count -=1
        if count < 0:
            return False
    return True

def reverse(s):
    ans = ''
    for i in s:
        if i == '(':
            ans += ')'
        else:
            ans += '('
    return ans

def solution(p):
    answer = ''

    if p == '' : return answer      # 1. 빈 문자열인 경우

    left = 0
    right = 0
    for i in range(len(p)):
        if p[i] == '(':
            left += 1       # 열린괄호의 개수 카운트
        else:
            right += 1      # 닫힌괄호의 개수 카운트
    
        if left == right:   # 열린괄호와 닫힌괄호의 개수가 같은 균형잡인 괄호 문자열일 경우
            u = p[:i+1]     # 두 균형잡힌 문자열 u, v를 생성
            v = p[i+1:]
            # print(i, u, v)
            break


    if check(u):
        print(check(u))
        return u + solution(v)
    else:
        return '(' + solution(v) + ')' + reverse(u[1:-1])

print(solution("(()())()"))     # "(()())()"
print(solution(")("))           # "()"
print(solution("()))((()"))     # "()(())()"