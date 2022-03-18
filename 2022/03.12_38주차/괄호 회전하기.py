# 괄호 회전하기
# 링크: https://programmers.co.kr/learn/courses/30/lessons/76502

# 문제접근
# 짝이 맞는 괄호인지 check하는 함수를 하나 생성한다.
# 괄호의 개수만큼 for문을 돌려서 몇번 짝이 맞는지 판별한다.

# 문제풀이(1)
def check(s_list):
  stack = []

  for i in s_list:
    # i가 열린 괄호인지 판별
    print(i)
    if i in ['[', '(', '{']:
      stack.append(i)
    else:
      # stack이 비어있을 경우 맞지 않음
      if len(stack) == 0: 
        return False

      c = stack.pop()
      if i == ']' and c != '[':
        return False
      elif i == ')' and c != '(':
        return False
      elif i == '}' and c != '{':
        return False

def solution(s):
  answer = 0
  s_list = list(s)

  # 맨 앞의 괄호를 뒤로 넘긴다. (어차피 한바퀴 돌면 처음배열도 체크됨.)
  for i in range(len(s)):
    front_pop = s_list.pop(0)
    s_list.append(front_pop)
    print(s_list)
    print(answer)

    if check(s_list) == True:
      answer += 1

  return answer

# 왜 0만 나오는지 의문을 가지고 작성한 코드를 자세히 봤음
# 생성한 check 함수에 True를 return 해주는 부분이 없음.
# 그러면 모든 for문이 끝나고 stack이 비어있다면 True를 return?


# 문제풀이(2)
def check(s_list):
  stack = []

  for i in s_list:
    # i가 열린 괄호인지 판별
    if i in ['[', '(', '{']:
      stack.append(i)
    else:
      # stack이 비어있을 경우 맞지 않음
      if len(stack) == 0: 
        return False

      # 열린 괄호
      c = stack.pop()
      # 현재 닫힌 괄호가 열린괄호와 맞지 않은 경우 짝이 틀림
      if i == ']' and c != '[':
        return False
      elif i == ')' and c != '(':
        return False
      elif i == '}' and c != '{':
        return False

  # for문을 정상적으로 돌았을 경우 stack이 비어있다면 짝이 맞음
  if len(stack) == 0:
    return True
  else:
    return False

def solution(s):
  answer = 0
  s_list = list(s)

  # 맨 앞의 괄호를 뒤로 넘긴다. (어차피 한바퀴 돌면 처음배열도 체크됨.)
  for i in range(len(s)):
    front_pop = s_list.pop(0)
    s_list.append(front_pop)
    # print(s_list)
    # print(answer)

    if check(s_list) == True:
      answer += 1

  return answer


# 다른 사람의 풀이(1)
# 슬라이싱을 이용해서 끊어줌
def is_valid(s):
    stack = []
    for ch in s:
        if not stack:
            stack.append(ch)
        elif stack[-1] == '(':
            if ch==')': stack.pop()
            else: stack.append(ch)
        elif stack[-1] == '{':
            if ch=='}': stack.pop()
            else: stack.append(ch)
        elif stack[-1] == '[':
            if ch==']': stack.pop()
            else: stack.append(ch)

    return False if stack else True

def solution(s):
    answer = 0
    for i in range(len(s)):
        answer += is_valid(s[i:]+s[:i])
    return answer

print(solution("[](){}"))     # 3
print(solution("}]()[{"))     # 2
print(solution("[)(]"))       # 0
print(solution("}}}"))        # 0