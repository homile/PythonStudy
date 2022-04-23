# Zigzag Conversion

# 링크: https://leetcode.com/problems/zigzag-conversion/

# [문제접근]
# 11개의 문자가 있고, 행이 3행이라면 
# [0,0] → [0,1] → [0,2] → [1,1] → [2,0]
# 이런식으로 y의 값이 증가하다가 numsRows와 같게되면 
# y -= 1을 하여 리스트에 넣어준다.
# 그런다음 리스트의 값을 한줄로 join 해준다.

# 문제풀이(1)
def solution(s, numRows):
   answer = 0
   stack = [['' for i in range(len(s))] for j in range(numRows)]
   # print(stack)

   for i in range(len(s)):
      for j in range(numRows):
         if i == 0:
            stack[j][i] = s[j]
         else:
            stack[j][i] = s[i]

      i += j


   print(stack)
   return answer

# 오르락 내리락 해야하는 구조상 2중 for문은 복잡하다.
# 그리고 처음을 일자로 내릴 필요는 없다. 대각선으로 움직이면 된다.


# 문제풀이(2)        # out of range 떴음
def solution(s, numRows):
   answer = ''
   stack = [['' for i in range(len(s))] for j in range(numRows)]
   # print(stack)
   j = 0
   check = True

   for i in range(len(s)):
      stack[j][i] = s[i]
      if j == 0:
         check = True
      elif j == numRows-1:
         check = False
      
      if check:
         j += 1
      else:
         j -= 1

   print(stack)
   for i in range(len(stack)):
      for j in range(len(stack[0])):
         if stack[i][j] != '':
            answer += stack[i][j]

   return answer

# out of range
# last input: "AB", 1
# 위와 같은경우 범위를 벗어난다고 함.
# 이유는 numRows가 1줄일 경우 그대로 출력하면 되지만 2중 for문을 돌기때문
# 초반에 예외 처리를 하면 될듯?
# 그리고 for문보다는 while문을 쓰는 것이 조금 더 깔끔해질 것 같았다.

# 문제풀이(3)
def solution(s, numRows):
   answer = ''
   stack = [['' for i in range(len(s))] for j in range(numRows)]
   # print(stack)
   j = 0
   check = True

   if numRows == 1: return s

   for i in range(len(s)):
      stack[j][i] = s[i]
      if j == 0:
         check = True
      elif j == numRows-1:
         check = False
      
      if check:
         j += 1
      else:
         j -= 1

   print(stack)
   for i in range(len(stack)):
      for j in range(len(stack[0])):
         if stack[i][j] != '':
            answer += stack[i][j]

   return answer

print(solution("PAYPALISHIRING", 3))   # "PAHNAPLSIIGYIR"