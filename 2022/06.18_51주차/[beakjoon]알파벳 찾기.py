# 알파벳 찾기
# 링크: https://www.acmicpc.net/problem/10809

# 문제풀이(1)
n  = input()
alphabet = ['-1'] * 26

count = 0

for i in range(len(n)):
  if str(alphabet[ord(n[i])-97]) == '-1':
    alphabet[ord(n[i])-97] = str(count)
  count += 1

answer = ' '.join(alphabet)

print(answer)
