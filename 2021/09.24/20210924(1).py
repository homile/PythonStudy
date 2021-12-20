# 기능개발

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/42586

# 문제접근
# 앞의 것이 먼저 완료가 되어야 뒤에 것도 같이 완료됨

# first = 4, second = 3  -> 4일째 2개가 같이 됨

# 100퍼가 되는 경우를 몇개인지 파악 
# stack으로 answer에 적제

# 첫번째가 100이상 일 때 100이상인 것이 몇 개인지 파악
# 일수를 count 해줘야 함

# 문제풀이(1)
def solution(progresses, speeds):
    answer = []
    
    for i in range(len(progresses)):
        for j in range(len(speeds)):
            if progresses[i] >= 100:
                break
            else:
                progresses.append(progresses[i]+speeds[j])
    print(progresses)
            
    return answer

# 100이 될 때까지 speeds에 해당하는 만큼 + 해준다
# 하지만 이때 for j in range를 사용하면 안되는데 실수함.

# 해결 방안 while 로 progresses[i] 번째 값을 
# speeds[i]만큼 + 시켜서 100 이상이 되면 pop을 해서 
# 값을 빼고 카운트 하면 되나?


# 문제풀이(2)
def solution(progresses, speeds):
    answer = []
    
    for i in range(len(progresses)):
        day = 1
        cnt = 0
        while progresses[i] < 100:            
            if progresses[i] + (speeds[i]*day) >= 100:
                cnt += 1
                answer.append(cnt)
                break
            else:
                day += 1
                        
    print(progresses)
            
    return answer

# 몇 일 째에 100%를 달성하는지 까지 계산함

# 하지만 앞의 수와 계산을 하는 공식을 넣지 않음

# 생각 해볼 것


# 문제풀이(3)
def solution(progresses, speeds):
    answer = []
    day = 1
    cnt = 0
    
    for i in range(len(progresses)):
        
        # 먼저 100보다 큰수가 됐는지 파악 비교할 1번째 값을 지정
        if i == 0 and progresses[i] + (speeds[i]*day) >= 100:
            cnt += 1
            answer.append(cnt)
        elif i > 0 and progresses[i] + (speeds[i]*day) >= 100:
            cnt += 1
            answer[-1] += 1
            
        while progresses[i] + (speeds[i]*day) < 100:
            # progresses[i] = progresses[i]+speeds[i]
            day += 1
            if progresses[i] + (speeds[i]*day) >= 100:
                cnt = 1
                answer.append(cnt)
                break
            
            # if progresses[i] >= 100 : break
            
    print(progresses)
            
    return answer

print(solution([93, 30, 55], [1, 30, 5]))                       # [2, 1]
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))   # [1, 3, 2]