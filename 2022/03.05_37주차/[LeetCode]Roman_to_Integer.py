# Roman to Integer
# 링크: https://leetcode.com/problems/roman-to-integer/

# I로마 숫자는 , V, X, L, C, D의 7가지 기호로 표시됩니다  M.

# 기호         값
# I            1
# V            5
# X            10
# L            50
# C            100
# D            500
# M            1000
# 예를 들어,   로마 숫자로 쓰는데 둘만 더하면 됩니다 2. 는 로 작성됩니다. 
# 숫자 는 , 즉 로 기록됩니다 .II 12 XII X + II 27 XXVII XX + V + II

# 로마 숫자는 일반적으로 왼쪽에서 오른쪽으로 큰 것에서 작은 것 순으로 표기합니다. 
# 그러나 4의 숫자는 가 아닙니다 IIII. 대신 숫자 4는 로 기록됩니다 
# IV. 1은 5보다 앞에 있기 때문에 빼서 4가 됩니다. 
# 로 쓰여진 숫자 9에도 동일한 원칙이 적용됩니다 
# IX. 빼기가 사용되는 6가지 경우가 있습니다.

# I - V(5)와 X(10) 앞에 배치하여 4와 9를 만들 수 있습니다. 
# X - L(50)과 C(100) 앞에 배치하여 40과 90을 만들 수 있습니다. 
# C - D(500)과 M(1000) 앞에 배치하여 400과 900을 만들 수 있습니다.
# 로마 숫자가 주어지면 그것을 정수로 변환하십시오.

# [문제접근]
# 로마숫자를 딕셔너리로 배치시켜서 구한다

# 문제풀이(1)
def solution(s):
   answer = 0
   dic = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}

   for i in range(len(s)):
      num = dic[s[i]]
      answer += num

   return answer

# TC 1,2번은 통과하지만 3번은 통과하지못함
# TC 3 = 1994이 -> 2216으로 출력됨
# 앞과 뒤의 값이 합쳐지는 로마 숫자가 있음
# 예) IV, XL, CD 등
# 앞뒤를 판별해서 바꿔야할듯

# 문제풀이(2)
def solution(s):
   answer = 0
   dic = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}

   for i in range(len(s)-1):
      num = dic[s[i]]
      nextNum = dic[s[i+1]]
      # 4, 9 | 40, 90 | 400, 900을 구하기 위함.
      if num >= nextNum:
         answer += num
         print('+',num)
      else:
         answer -= num
         print('-',num)

   # 마지막 값을 추가하기 위함
   answer += dic[s[-1]]
   return answer
   

# 다른 사람의 풀이: https://daimhada.tistory.com/125

print(solution("III"))        # 3
print(solution("LVIII"))      # 58
print(solution("MCMXCIV"))    # 1994