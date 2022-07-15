# 접미사 배열
# 링크: https://www.acmicpc.net/problem/11656

# 문제풀이(1)
word = list(input())
result = []
wordLen = len(word)

for i in range(wordLen):
  result.append(''.join(word))
  word.pop(0)  

print('\n'.join(sorted(result)))

# input
# baekjoon

# output
# aekjoon
# baekjoon
# ekjoon
# joon
# kjoon
# n
# on
# oon