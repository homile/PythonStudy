# 멀쩡한 사각형

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/62048

# 문제접근
# 대각선으로 잘린 정사각형들을 제외한 나머지를 계산하면된다.
# 2차원 배열문제이다.
# 큰 직사각형으로 패턴을 찾으면 힘들지 않을까?
# 그림만 봤을때는 ㄴㄱ형식으로 보인다.

# 그래도 패턴이 보이지 않는다.

# 공부하는 식으로 문제풀이의 공약수라는 힌트를 찾았다.
# 공약수? 왜지? 하고 풀어봄
# x : y -> 8:12 
# 8의 약수: 1, 2, 4, 8
# 12의 약수: 1, 2, 3, 4, 6, 12
# 둘의 공약수: 1, 2, 4
# 8 + 12 - 공약수? -> 8 + 12 - 1 = 19 | 8 + 12 - 2 = 18 | 8 + 12 - 4 = 16
# x + y - 최대공약수라는 것이 나왔다.

# 그럼 두수의 약수를 찾고 최대공약수를 풀면되는 간단한 문제였다.

# 문제풀이(1)
def gcd(w, h):
    x = max(w,h)
    y = min(w,h)
    while y:
        x, y = y, x % y
    return x

def solution(w,h):
    answer = 0

    answer = w + h - gcd(w,h)

    return answer

# 최대 공약수를 풀고 값을 찾았지만 실수했다.
# 최대 공약수를 찾는데에만 집중해서 결과값을 제대로 출력하지 않았다.
# 결과값은 w + h - (w+h-gcd) 였다.


# 문제풀이(2)
def gcd(w, h):
    x = max(w,h)
    y = min(w,h)
    while y:
        x, y = y, x % y
    return x

def solution(w,h):
    answer = 0

    gcd_result = w + h - gcd(w,h)
    answer = w * h - gcd_result

    return answer

print(solution(8, 12))  # 80


# 다른 사람의 풀이(1)
from math import gcd
def solution(w,h):
    return w * h - (w + h - gcd(w, h))

# math 라이브러리의 gcd함수를 사용할 수 있다.

print(solution(8, 12))  # 80