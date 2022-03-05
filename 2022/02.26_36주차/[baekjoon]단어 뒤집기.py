# 단어 뒤집기
# 링크: https://www.acmicpc.net/problem/9093

# [문제]
# 문장이 주어졌을 때, 단어를 모두 뒤집어서 출력하는 프로그램을 작성하시오. 
# 단, 단어의 순서는 바꿀 수 없다. 단어는 영어 알파벳으로만 이루어져 있다.

# [입력]
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 문장이 하나 주어진다. 
# 단어의 길이는 최대 20, 문장의 길이는 최대 1000이다. 
# 단어와 단어 사이에는 공백이 하나 있다.

# [출력]
# 각 테스트 케이스에 대해서, 입력으로 주어진 문장의 단어를 모두 뒤집어 출력한다.

# [문제접근]
# 테스트의 줄 수를 입력받고 for문을 사용해 반복한다.
# 리스트로 명령어를 받고 한 인덱스당 reverse를 해주고 
# join으로 이어붙여 출력하면 될 것 같다.

# 사실 슬라이싱으로 뒤집어서 출력?

# 문제풀이(1)
import sys
N = int(sys.stdin.readline())

for i in range(N):
    testCase = list(map(str, sys.stdin.readline().split()))

    for j in range(len(testCase)):
        testCase[j] = testCase[j][::-1]

    print(' '.join(testCase))
        

# 입력
# 2
# I am happy today
# We want to win the first prize