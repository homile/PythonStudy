# 쇠막대기
# 링크: https://www.acmicpc.net/problem/10799

# [문제접근]
# ()는 레이저 (막대기(레이저)막대기)

# 문제풀이(1)
stick = input()
answer = 0
stack = []

for i in range(len(stick)):
   if stick[i] == '(':
      stack.append(stick[i])
   else:
      if stick[i-1] == '(':
         stack.pop()
         answer += len(stack)
      else:
         stack.pop()
         answer += 1
         
   # print(stack, answer)

print(answer)


# '()(((()())(())()))(())'        # 17
# '(((()(()()))(())()))(()())'    # 24