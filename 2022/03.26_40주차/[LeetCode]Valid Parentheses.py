# Valid Parentheses

# 링크: https://leetcode.com/problems/valid-parentheses/

# [문제접근]
# 괄호가 알맞는지 맞추면 되는 문제
# 프로그래머스 괄호 변환과 비슷한 문제

# 문제풀이(1)
def solution(s):
   answer = True
   stack = []

   for i in s:
      # 열린괄호 stack에 담기
      if i in ['(', '[', '{']:
         stack.append(i)
      else:
         if len(stack) == 0:
            return False
         
         # 스택 끝의 열린괄호가 현재 닫힌괄호랑 맞는지 비교
         c = stack.pop()
         if i == ')' and c != '(':
            return False
         elif i == ']' and c !='[':
            return False
         elif i == '}' and c != '{':
            return False
 
   return answer

# 괄호가 하나만 있을 경우와 열린괄호만 있을 경우를 생각해야함.


# 문제풀이(2)
def solution(s):
   answer = True
   stack = []

   for i in s:
      # 열린괄호 stack에 담기
      if i in ['(', '[', '{']:
         stack.append(i)
      else:
         if len(stack) == 0:
            return False
         
         # 스택 끝의 열린괄호가 현재 닫힌괄호랑 맞는지 비교
         c = stack.pop()
         if i == ')' and c != '(':
            return False
         elif i == ']' and c !='[':
            return False
         elif i == '}' and c != '{':
            return False
   
   if stack:
      return False
 
   return answer

print(solution("()"))   # true
print(solution("()[]{}"))   # true
print(solution("(]"))   # false