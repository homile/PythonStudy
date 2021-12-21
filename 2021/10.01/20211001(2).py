# 주식가격

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/42584
# p = 1원 -> 1초 = 2원, 2초 = 3원, 3초 = 2원, 4초 = 3원
# 이므로 첫 가격인 1원보다 후에 가격은 높기 때문에
# 4초 뒤에도 가격이 떨어지지 않는다.

# p = 2원 -> 1초 = 3원, 2초 = 2원, 3초 = 3원
# 이므로 첫 가격인 2원보다 후에 가격은 높기 때문에
# 3초 뒤에도 가격이 떨어지지 않는다.

# p = 3원 -> 1초 = 2원 이므로 첫 가격인 3원보다
# 후에 가격이 1원 떨어졌기 때문에 1초 만에 가격이 떨어진다.

# p = 2원 -> 1초 = 3원 이므로 첫 가격인 2원보다
# 1초 뒤에도 가격이 떨어지지 않는다.

# p = 3원 -> 후에 가격이 나와있지 않으므로
# 0초 동안 가격이 떨어지지 않는다.

# 문제접근
# prices list에서 첫 번째 가격과 그 뒤에 가격을 비교해서 앞의 가격이 뒤의 가격보다 작다면
# 가격이 떨어지지 않은 것이기 때문에 계속해서 비교를 해준다.

# 만약 앞의 가격이 뒤의 가격보다 크다면 가격이 떨어진 것으로 판단하여 몇 초 만에 가격이 떨어졌는지 판별한다.

# for문을 사용하고 스택/큐 문제인 만큼 큐를 사용해서 풀어보자
# 앞의 가격을 전부다 비교하고 나서 pop(0)으로 빼 주는 방식으로 하면 될 것이다.

# 나의 풀이 1에서의 풀이는 효율성 검사에서 통과하지 못했다.
# 스택/큐의 공부를 했기에 deque를 사용하면 효율성이 좋아진다는 것을 알 수 있었다.

# 문제풀이(1)
def solution(prices):
    answer = []
    
    while len(prices) > 0:
        front = prices.pop(0)
        cnt = 0
        for i in range(len(prices)):
            if front > prices[i]:
                cnt += 1
                break
            elif front <= prices[i]:
                cnt += 1
        answer.append(cnt)
    
    return answer

# 테스트케이스와 제출에는 성공했다.
# 하지만 효율성 검사에서 실패했다.

# 이유??
# 효율성 검사에서 통과하기 위해서는
# while문안에 for문을 삭제 하거나
# collection 라이브러리에서 deque를 사용해야 할 것 같다.


# 문제풀이(2)   통과
from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    
    # print(prices, queue)
    
    while queue:
        front = queue.popleft()
        # print(front, queue)
        cnt = 0
        for i in queue:
            if front > i:
                cnt += 1
                break
            elif front <= i:
                cnt +=1
        
        answer.append(cnt)
    
    return answer

# deque를 사용하니 효율성문제에서
# 통과를 하였다.

# 코드를 조금 더 분석해서
# 효율성을 높일 수 있는지 확인해보자


# 문제풀이(3)   통과
from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    
    # print(prices, queue)
    
    while queue:
        front = queue.popleft()
        # print(front, queue)
        cnt = 0
        for i in queue:
            cnt += 1
            if front > i:
                break        
        answer.append(cnt)
        
    return answer

# 조건문을 조금 줄여줬더니
# 속도가 평균 15초 정도 빨라진 것을
# 확인할 수 있다.


# 다른 사람의 풀이(1)
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer

# 스택을 활용한 방법보다 속도가 약 2배정도 느리다
#prices값과 동일한 길이의 리스트로 초기화 하기 위해서 초기화 작업

print(solution([1, 2, 3, 2, 3]))    # [4, 3, 1, 1, 0]