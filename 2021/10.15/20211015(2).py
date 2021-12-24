# 올바른 괄호

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/12909

# 문제접근
# 괄호의 개수가 맞는지 판별

# 괄호의 시작이 ( 맞는지 판별

# 괄호의 개수가 같다고 올바른 괄호가 아니다.

# 그럼 스택 형식으로 하나씩 빼서 괄호의 시작과
# 괄호의 방향 등이 맞는지 판별하면 될 것 같다.

# 문제풀이(1)
def solution(s):
    answer = True
    
    if s[0] == ")" : 
        answer = False
    
    print(s[0])

    return answer

# 가장 처음으로 (가 나올 경우 false를 return 해주는 것을 구현

# 1 ~ 3번 TC는 통과함

# 이제 해야 할 것
# 괄호가 정확한지 문자를 하나씩 쪼개서
# 리스트에 넣어서 스택 형식으로 확인 해보면 될 듯???


# 문제풀이(2)
def solution(s):
    answer = True
    a = []
    
    if s[0] == ')' or s.count('(') != s.count(')') : 
        return False
        
    for i in s:
        if i == '(':
            a.append(i)
        if i == ')':
            a.pop()
            if len(a) > 0:
                return False

    return answer

# )로 시작하거나 (와 )의 개수가 다를 경우 바로 False를 return 한다.


# 문자열 s에서 하나씩 판별해서 (이면 a리스트에 넣어주고
# )이면 a리스트에 넣은 (를 pop해주면 됐다.

# 위와 같이 하면 (가 들어가고 )가 만날 때 짝이 맞아서 
# len으로 리스트 a의 길이를 판별 할 경우 0보다 많다면
# 위치가 맞지 않다는 것을 알 수 있을 것 같았다.

# 위의 테스트 2 결과와 같이 (가 하나가 남아있는 경우가 있었다.
# 생각해 볼 수 있는 것은 조건을 다시 지정해야 할 것 같다.


# 문제풀이(3) 통과
def solution(s):
    answer = True
    a = []
    
    if s[0] == ')' or s.count('(') != s.count(')'):
        return False
        
    for i in s:		
        if i == '(':
            a.append(i)
        elif len(a) == 0 :
            return False
        elif i == ')':
            a.pop()
    if len(a) > 0:
        return False

    return answer

#  if i == ')':
#             a.pop()
#             if len(a) > 0:
#                 return False

# 위 부분을 제거했다. For 안에서 돌리면 바로 if len(a)를 실행해버려서
# 마지막 (을 제거하지 못했기 때문이다.
# 그래서 for문을 다 돌고 나서 조건문을 달아서 해결했다.
# 위의 코드를 볼 경우 다소 잡다한 코드가 있다. 조금 더 줄여 보자


# 문제풀이(4)
def solution(s):
    a = []
            
    for i in s:
        if i == '(':
            a.append(i)
        elif len(a) == 0 :
            return False
        elif i == ')':
            a.pop()
    
    if len(a) > 0:
        return False

    return True
# 나의 풀이 3번보다 많이 간결해 졌다.
# 초반에 count를 이용한 부분은 결국 for문을 돌리게 되면 해결 될 수 있다.

# 하지만 시간을 아낄 수 있을 거라는 생각에 처음에 비교를 했었다.

# 또한, answer를 쓰지 않고 바로 return 값을 True로 해줬다.
# 어차피 False와 True만 사용한다면 조금 더 줄일 수 있을 거라 생각했다.

# 하지만 아래와 같이 효율성 테스트에서 1번은 1초 정도 빨라졌지만
# 테스트 2번에서는 10초 정도 느려진 것을 볼 수 있다. For문을 돌리기 전에 
# 조건문으로 값을 내주었기 때문에 나의 풀이 3이 조금 더 빠른 실행 결과를 준 것 같다.


# 다른 사람의 풀이(1)
def is_pair(s):
    # 함수를 완성하세요
    x = 0
    for w in s:
        if x < 0:
            break
        x = x+1 if w=="(" else x-1 if w==")" else x
    return x==0

# ternary operator


# 다른 사람의 풀이(2)
def is_pair(s):
    st = list()
    for c in s:
        if c == '(':
            st.append(c)

        if c == ')':
            try:
                st.pop()
            except IndexError:
                return False

    return len(st) == 0

# 지난 주와 같이 try except을 사용하여
# 오류가 나올 경우 False를 return 해주는 풀이

# try except를 사용하는 방법도 후에는 많이 쓰게 될 것 같다.

print(solution("()()"))     # True
print(solution("(())()"))   # True
print(solution(")()("))     # False
print(solution("(()("))     # False