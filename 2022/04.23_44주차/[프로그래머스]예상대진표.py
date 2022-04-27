# 예상 대진표
# 링크: https://programmers.co.kr/learn/courses/30/lessons/12985

# [문제접근]
# 부전승은 발생하지 않도록 무조건 참가자의 수는 짝수이다.
# 그림판으로 그려본 결과 2로 나눠서 몫을 구하면 다음 순번이 나온다.
# 하지만 b = 7일경우 4번째가 나와야 하는데 3이 나온다.
# 그렇다면? 
# 1. //로 선택해서 소숫점을 제외한다
# 2. a나 b가 홀수일 경우 +1을 해줘서 나누면 다음번째수를 구할 수 있다.

# 문제풀이(1)
def solution(n,a,b):
   answer = 1

   if a % 2 == 0:
      a += 1
   if b % 2 == 0:
      b += 1

   while(a!=b):
      a = a//2
      b = b//2
      answer += 1

   return answer

# 처음에 짝수로 바꿔도 상관없다는 것을 알았다.
# while문 내에서 돌릴때 짝수로 바꾼 값이 홀수로 바뀌는 경우가 발생한다.
# 그러면 while에서 계속 +1을 해주면 될 것이다.


# 문제풀이(2)
def solution(n,a,b):
   answer = 0

   while(a!=b):
      a = (a+1)//2
      b = (b+1)//2
      answer += 1

   return answer

print(solution(8, 4, 7))   # 3