# 더 맵게

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/42626

# 문제접근
# 모든 음식의 스코빌 지수 > k
# 만드는 방법 = 스코빌 지수가 가장 낮은 두 개의 음식을
# 가장 맵지 않은 음식 + (두 번째로 맵지 않은 음식 * 2)
# [1, 2, 3, 9, 10, 12] -> 1 + (2 * 2) = 5
# [5, 3, 9, 10, 12] -> 3 + (5 * 2) = 13
# [13, 9, 10, 12] = 모든 음식이 7보다 높다.

# 최소힙?  최대힙?
# heapq를 import한다.

# scoville 지수를 heap으로 바꿔준다?
# heapify? 를 사용하면 자동으로 min heap으로 바꿔준다
# min heap이 아닌 max heap이었다. *(주현)


# 문제풀이(1)
import heapq

def solution(scoville, K):
    answer = 0
    
    while True:
        heapq.heapify(scoville)
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        heapq.heappush(scoville, first + (second * 2))
        answer += 1
        if scoville[0] > K : break
    print(scoville)
        
    return answer

# 테스트 케이스는 통과하지만
# 제출 시 1,3,8,14가 통과하지
# 않는다.

# 예상 이유
# 효율성에서 통과하지 못한
# 것으로 보아 코드에 
# 불필요한 부분이 존재한다.


# 문제풀이(2)
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        answer += 1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        heapq.heappush(scoville, first + (second * 2))
        
    print(scoville)
        
    return answer

# 효율성에서는 통과했다.
# 전에 통과하지 못한 이유는
# heapify로 매번 정렬을 했기
# 때문이었다.

# 모든 음식의 스코빌 지수를 K # 이상으로 만들 수 없는 
# 경우에는 -1을 return 합니다. 

# 위의 지문을 생각하지 못함.


# 문제풀이(3)
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:	# 가장 낮은 노드의 값이 k보다 작을 경우 while을 실행
        if len(scoville) > 1:	# scoville의 길이가 1보다 클 때 실행 아닐 경우 answer = -1을 return
            answer += 1
            first = heapq.heappop(scoville)			# 제일 낮은 스코빌 지수
            second = heapq.heappop(scoville)		# 두 번째로 낮은 스코빌 지수
            heapq.heappush(scoville, first + (second * 2))	# 스코빌 리스트에 공식의 값을 추가
        else :
            answer = -1
            break
        
    return answer

# 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 
# 경우에는 -1을 return 합니다.

# 위의 지문을 해결하기 위해 조건문을 추가하였다.


# 다른 사람의 풀이(1)
import heapq as hq

def solution(scoville, K):

    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1  

    return answer

# 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 
# 경우에는 -1을 return 합니다.

# 위의 지문을 해결하기 위해 조건문을 추가하였다.

print(solution([1, 2, 3, 9, 10, 12], 7))        # 2