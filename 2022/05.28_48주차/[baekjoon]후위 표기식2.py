# 후위 표기식2
# 링크: https://www.acmicpc.net/problem/1935

# [문제접근]
# 후위 계산식을 중위 계산식처럼 계산한 값을 출력
# ABCDE에 맞는 값을 입력
# ABC*+DE/- -> A+(B*C)/(D-E) =>  1+(2*3)-(4/5) = 6.20
# 연산자를 만나기전에 스택에 쌓는다
# 연산자를 만나면 뒤의 두개 값을 pop해서 계산을 한다. (반복)

# 문제풀이(1)
import re

n = int(input())  # 알파벳 개수
cal = input()     # 후위 계산식
al = []

for i in range(n):
  al.append(int(input()))
# print(al)

stack = []

for i in cal:
  if re.match('^[A-Z]',i):  # 정규표현식 대문자 알파벳 구별
    # print(i)
    stack.append(al[ord(i)-65])
  else:
    right = stack.pop()   # 마지막값
    left = stack.pop()    # 마지막 전 값

    if i == '+':
      stack.append(left + right)
    elif i == '-':
      stack.append(left - right)
    elif i == '*':
      stack.append(left * right)
    elif i == '/':
      stack.append(left / right)

print(stack)
print(format(stack[0],".2f"))



# input: 
# 5
# ABC*+DE/-
# 1
# 2
# 3
# 4
# 5

# output: 6.20