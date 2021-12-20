# 프린터

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/42587

# 문제접근
# 프린터가 인쇄하는 형식 = stack
# 하지만 중요 문서가 나중에 인쇄 해결방안 찾는 문제
# 1.가장 앞에 있는 문서(J)를 대기목록에서 꺼낸다 
#   (popleft() or pop()??)
# 2.중요도가 높은 문서가 존재하면 가장 마지막에 J를 탑재
# 3.그렇지 않으면 J를 인쇄

# location = 내가 요청한 문서가 몇 번째 인지 알려주는 수
# 출력할 값 = 내가 요청한 문서가 몇 번째로 출력되는지 알려주는 수

# 문제풀이(1)
def solution(priorities, location):
    answer = 0
    
    arr1 = []
    arr2 = []
    
    while len(priorities) != 0:
        if priorities[0] == max(priorities):
            arr1.append(priorities.pop(0))
        else:
            arr2.append(priorities.pop(0))

    arr1.extend(arr2)        
    print(arr1, arr2)
            
    return answer

# 두개의 리스트를 생성한다 
# arr1 = 우선순위가 높은 출력 순
# arr2 = 우선순위가 낮은 앞의 출력 물

# 후에 arr1과 arr2를 합치는 함수 extend를 사용.

# 이제 해야 하는 것은 나의 출력물의 위치를 찾는 것
# 인덱스 번호를 부여 할 것인가??

# 2, 1 3 2
# Arr1 3, 2 , 2 ,1 
# Arr1 += arr2 = 2차원 배열  extend(arr2)


# 문제풀이(2)
def solution(priorities, location):
    answer = 0
    loc = priorities[location]
    arr1 = []
    arr2 = []
    
    while len(priorities) != 0:
        if priorities[0] == max(priorities):
            arr1.append(priorities.pop(0))
        else:
            arr2.append(priorities.pop(0))
    
    arr1.extend(arr2)
    answer = arr1.index(loc) + 1
    print(arr1, arr2, arr1.index(loc))
            
    return answer

# 테스트케이스 1은 통과하지만 2는 통과하지 못함

# 이유?  테스트케이스는 911111로 1이 같이 반복되는 경우 있음
# 이것을 해결하면 될 듯?
# dictionary를 사용해야 하나?


# 문제풀이(3)
def solution(priorities, location):
    answer = 0
    
    priorities = [(i, j) for j, i in enumerate(priorities)]
    loc = priorities[location]
    arr1 = []
    arr2 = []
    
    print(priorities)
    while len(priorities) != 0:
        if priorities[0] == max(priorities):
            arr1.append(priorities.pop(0))
        else:
            arr2.append(priorities.pop(0))
    
    arr1.extend(arr2)
    answer = arr1.index(loc) + 1
    print(arr1, arr1.index(loc))
            
    return answer

# priorities를 enumerate를 사용하여 dictionary 
# 형식으로 바꾸었다.


# 문제풀이(4)
def solution(priorities, location):
    answer = 0
    
    priorities = [(i, j) for j, i in enumerate(priorities)]
    
    print(priorities)
    while len(priorities) != 0:
        front = priorities.pop(0)
        if front[0] < max(priorities)[0]:
            priorities.append(front)
        else:
            answer +=1
            if front[1] == location:
                break
            
    return answer

# 제출 시 3, 5, 18번에 에러가 났다
# 검색 결과 원소가 하나인 경우 
# ValueError: max() arg is an empty sequence
# 라는 에러가 난다


# 문제풀이(5) 통과
def solution(priorities, location):
    answer = 0
    
    priorities = [(i, j) for j, i in enumerate(priorities)]
    
    print(priorities)
    while len(priorities) != 0:
        front = priorities.pop(0)
        if len(priorities) == 0:
            answer += 1
            break
        if front[0] < max(priorities)[0]:
            priorities.append(front)
        else:
            answer +=1
            if front[1] == location:
                break
    return answer


# 다른 사람의 풀이(1)
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

# any 함수를 사용하여 한번에 표현했다.


# 다른 사람의 풀이(2)
def solution(priorities, location):
    answer = 0
    from collections import deque

    d = deque([(v,i) for i,v in enumerate(priorities)])

    while len(d):
        item = d.popleft()
        if d and max(d)[0] > item[0]:
            d.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer

# 스택에서 pop(0) 하는 것보다(시간 복잡도 O(N)) deque 자료형으로 
# popleft()하는 게 훨씬 효율적이다.(시간 복잡도 O(1))

print(solution([2, 1, 3, 2], 2))        # 1
print(solution([1, 1, 9, 1, 1, 1], 0))  # 5