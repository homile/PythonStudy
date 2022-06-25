# 후위 표기식
# 링크: https://www.acmicpc.net/problem/1918

# [문제접근]
# 중위 표기식을 후위 표기식으로 변환.
# 변환 할 때 연산자의 우선순위를 파악해야 함.


# 문제풀이(1)
# 중위 표기식
postfix = list(input())

print(postfix)



# input: A*(B+C)
# output: ABC+*