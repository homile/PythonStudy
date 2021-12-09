# 정수 제곱근 판별

# 문제설명

# 예상풀이

# 문제풀이(1)
import math

def solution(n):
    answer = 0
    x = math.sqrt(n)          # n의 제곱근을 x에 대입한다.
    
    if x % 1 == 0:	       # 양수를 판별하기 위한코드
        answer = int((x+1)*(x+1))  # n의 제곱근에 1을 더한 후
                                                 # 제곱한다.
    else:
        answer = -1        # 양의 정수 제곱이 아니면 -1을 반환         
        
    return answer


# 다른 사람의 풀이(1)
def nextSqure(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return 'no'

# 앞서 math라이브러리의 sqrt와 같이 n **(1/2)를 하면 제곱값인 n의 제곱근을 구하는 식이며
# 제곱근을 % 1 == 0으로 양수를 판별하고, 제곱근에 1을 더해 **2로 제곱한 값을 출력한다.

# 2018년의 풀이기 때문에 양수가 아니라면 no를 출력하는 문제였다

print(solution(121))    # 144
print(solution(3))      # -1