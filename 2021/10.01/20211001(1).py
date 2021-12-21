# 다리를 지나는 트럭

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/42583

# 문제접근
# bridge_length = 다리의 길이?
# weight = 다리가 견딜 수 있는 무게
# truck_weights = 대기중인 트럭
# 큐 형식으로 FIFO를 사용하여 하면 될거같다.
# 0초부터는 대기중이고 1초부터 건너기 시작한다.
# 다리를 건너는 속력? = 1초당 bridge_length 1이다.
# 트럭 무게 = 10kg, 다리길이 = 100 이면 통과하는데 
# 걸리는 시간은 101초다.
# 100초 동안 지나가고 101초에는 통과하는 시간이다.
# truck_weights에서 pop(0)을 사용하여 큐 형식으로
# 빼면서 트럭을 다리위에 올리면 될 것이다.

# 문제풀이(1)
def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck = 0
    
    while len(truck_weights):
        answer += 1
        truck = truck_weights.pop(0)
            
        print(truck)
    return answer

# 처음으로 대기중인 트럭을 pop(0)으로 빼내는 것을 했다.

# 다리를 건너고 있는 트럭에 대한 list를 생성?
# on_bridge = [0] * bridge_length?
# on_bridge = [0] * len(truck_weights)?
# 다리를 지난 후의 시간?


# 문제풀이(2)
def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck = 0
    on_bridge = [0] * bridge_length
    
    while len(truck_weights):
        answer += 1
        if truck_weights:
            if truck_weights[0] <= weight:
                truck = truck_weights.pop(0)            
            else:
                truck = truck_weights.pop(0)
        on_bridge.append(truck)
        
        print(truck, on_bridge)
    return answer

# while의 조건이 truck_weigths의 길이 만큼 하는데
# 다빼고 마지막 트럭이 올라 갔을 경우 시간이 흐르는 
# 것을 표현할 수 없다.

# if문에 weigth와 구분하는 부분이 
# 현재 올라가 있는 트럭의 무게도 생각해야 한다.
# on_bridge에 pop으로 넣어주고
# truck_weights[0]과 같이 비교하면 되나?


# 문제풀이(3)
def solution(bridge_length, weight, truck_weights):
    answer = 0
    # truck = 0
    on_bridge = [0] * bridge_length
    
    while len(truck_weights):
        answer += 1
        if truck_weights:
            if truck_weights[0]+sum(on_bridge) <= weight:
                on_bridge.append(truck_weights.pop(0))    
            else:
                on_bridge.pop(0)
        # on_bridge.append(truck)
        
        print(on_bridge)
    return answer

# 기댓값 보다 1이 더 많이 나온다

# 이유?
# on_bridge 다리위에 올라간 트럭에
# 0, 0, 7로 시작하지만 다리의 길이는 2이므로 
# 처음에 앞에 있는 0 을 pop(0)으로 빼주면 될듯?


# 문제풀이(4)
def solution(bridge_length, weight, truck_weights):
    answer = 0
    on_bridge = [0] * bridge_length
    
    while on_bridge:
        answer += 1
        on_bridge.pop(0)
        if truck_weights:
            if truck_weights[0] + sum(on_bridge) <= weight:
                on_bridge.append(truck_weights.pop(0))    
            else:
                on_bridge.append(0)
                
    return answer

# 제출 시 테스트 5번이 오류가 난다.
# 찾아보니 sum으로 찾으면 O(N)으로 시간이 길다고 한다.
# 무게의 값을 따로 비교하자

# sum을 사용해도 된다 하지만 변수 명이 길어지면 안된다.
# (주현이 코드로 알게됨)


# 문제풀이(5)
def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck = 0
    on_bridge = [0] * bridge_length
    on_bridge_weights = 0
    while on_bridge:
        answer += 1
        truck = on_bridge.pop(0)
        on_bridge_weights -= truck
        if truck_weights:
            if truck_weights[0] + on_bridge_weights <= weight:
                s_truck = truck_weights.pop(0)
                on_bridge_weights += s_truck
                on_bridge.append(s_truck)
            else:
                on_bridge.append(0)
    return answer

# on_bridge_weights로 무게를 넣어주고
# truck에 올라가 있던 트럭을 빼주고
# s_truck에 새로 올라가는 트럭을 넣어줘서 해결함
# sum보다 확실히 시간이 빨라짐

print(solution(2, 10, [7,4,5,6]))   # 8
print(solution(100, 100, [10]))     # 101
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))  # 110