# ROT13
# 링크: https://www.acmicpc.net/problem/11655

# ord = 문자 -> 아스키
# chr = 아스키 -> 문자
# 소문자 a ~ z : 97 ~ 122
# 대문자 A ~ Z : 65 ~ 90

# 문제풀이(1)   # vscode통과 백준x
# s = input()
# result = ''

# for i in range(len(s)):
#   if s[i] == ' ':
#     result += s[i]

#   if ord(s[i]) >= 97 and ord(s[i]) <= 122:
#     if ord(s[i])+13 > 122:
#       result += chr(ord(s[i])+13-26)
#     else:
#       result += chr(ord(s[i])+13)

#   if ord(s[i]) >= 65 and ord(s[i]) <= 90:
#     if ord(s[i])+13 > 90:
#       result += chr(ord(s[i])+13-26)
#     else:
#       result += chr(ord(s[i])+13)

# print(result)

# Input
# Baekjoon Online Judge

# output
# Onrxwbba Bayvar Whqtr


# 문제풀이(2)   # 조건문 순서만 바꿔주니 해결
s = input()
result = ''

for i in range(len(s)):
  if ord(s[i]) >= 97 and ord(s[i]) <= 122:
    asc = ord(s[i])+13
    if asc > 122:
      result += chr(asc-26)
    else:
      result += chr(asc)

  elif ord(s[i]) >= 65 and ord(s[i]) <= 90:
    asc = ord(s[i])+13
    if asc > 90:
      result += chr(asc-26)
    else:
      result += chr(ord(s[i])+13)
  else:
    result += s[i]

print(result)

# Input
# Baekjoon Online Judge

# output
# Onrxwbba Bayvar Whqtr