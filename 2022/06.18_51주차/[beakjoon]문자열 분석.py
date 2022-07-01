# 문자열 분석 
# 링크: https://www.acmicpc.net/problem/10820

# 문제풀이(1)  # 답은 나오지만 무한루프 (EOFError)
while True:
  n  = list(input())
  if n in "": break
  # 소문자, 대문자, 숫자, 공백
  lo, up, nu, sp = 0, 0, 0, 0 

  for i in n:
    if i.islower():
      lo += 1
    elif i.isupper():
      up += 1
    elif i.isdigit():
      nu += 1
    else:
      sp += 1
  
  print(lo, up, nu, sp)


# 문제풀이(2)
while True:
  try:
    n  = list(input())

    # 소문자, 대문자, 숫자, 공백
    lo, up, nu, sp = 0, 0, 0, 0 

    for i in n:
      if i.islower():
        lo += 1
      elif i.isupper():
        up += 1
      elif i.isdigit():
        nu += 1
      else:
        sp += 1
    
    print(lo, up, nu, sp)
  except EOFError:
    break

# input
# This is String
# SPACE    1    SPACE
#  S a M p L e I n P u T     
# 0L1A2S3T4L5I6N7E8

# output
# 10 2 0 2
# 0 10 1 8
# 5 6 0 16
# 0 8 9 0