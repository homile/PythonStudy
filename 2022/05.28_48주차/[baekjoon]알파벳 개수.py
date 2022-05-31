# 알파벳 개수
# 링크: https://www.acmicpc.net/problem/10808

# 알파벳 개수 26개
# 소문자로만 이루어짐
# ord 쓰면될듯 ascii code = 97부터

# 문제풀이(1)
arr = input()

alphabet = [0] * 26
# print(alphabet)

for i in arr:
  alphabet[ord(i)-97] += 1

print(alphabet)


# 1 1 0 0 1 0 0 0 0 1 1 0 0 1 2 0 0 0 0 0 0 0 0 0 0 0
# input: 'baekjoon'
