# Excel Sheet Column Title
# 링크: https://leetcode.com/problems/excel-sheet-column-title/

# 문제풀이(1)
def solution(columnNumber):
    # A ~ ZZ까지
  answer = ''

  while columnNumber != 0:
    temp = chr(ord("A") + (columnNumber - 1) % 26)
    columnNumber = (columnNumber - 1) // 26
    answer = temp + answer
  return answer

print(solution(701))    # "ZY"
