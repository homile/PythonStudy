# 후위 표기식2
# 링크: https://www.acmicpc.net/problem/1935

# [문제접근]
# 후위 계산식을 중위 계산식처럼 계산한 값을 출력
# ABCDE에 맞는 값을 입력

# 문제풀이(1)
n = int(input())  # 알파벳 개수
cal = input()     # 후위 계산식


# input: 
# 5
# ABC*+DE/-
# 1
# 2
# 3
# 4
# 5

# output: 6.20