# [카카오 인턴] 키패드 누르기

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/67256

# 문제접근
# 1,4,7 = 왼손
# 3,6,9 = 오른손

# left, right 배열을 넣어서 확정적으로
# 왼손과 오른손이 정해져 있는 배열을 지정
# hand 배열은 어느 손이 먼저 시작하는 지 알려주는 배열?

# 왼손과 가깝다면 왼손이
# 오른손과 가깝다면 오른손이
# 두 손의 거리가 똑같다면 hand 배열을 통해 구분하여 클릭

# 문제풀이(1)
def solution(numbers, hand):
    answer = ''
    left_numbers = [1,4,7]
    right_numbers = [3,6,9]
    
    for i in numbers:
        if i in left_numbers :
            answer += 'L'
        elif i in right_numbers :
            answer += 'R'
        else:
            answer += 'X'
    # print(hand)
    return answer

# 현재 X라는 값을 2,5,8에 대신 넣어 둠
# 다음 번호와 가까운 손가락을 판별해야 함


# 문제풀이(2)
def solution(numbers, hand):
    answer = ''
    left_numbers = [1,4,7]
    right_numbers = [3,6,9]
    
    left_s = 10
    right_s = 12
    
    for i in numbers:
        if i in left_numbers : # 1,4,7은 무조건 왼손
            answer += 'L'
            left_s = i
        elif i in right_numbers : # 3,6,9는 무조건 오른손
            answer += 'R'
            right_s = i
        else:                   # 2,5,8,0을 누르는 경우
            now_l = abs(i - left_s)
            now_r = abs(i - right_s)

            if now_l < now_r :
                answer += 'L'
            elif now_r < now_l:
                answer += 'R'
            elif now_l == now_r and hand == 'right':
                answer += 'R'
            elif now_l == now_r and hand == 'left':
                answer += 'L'
            # answer += 'X'
            
    # print(hand)
    return answer

# 테스트케이스 3번만 통과를 했다.

# 테스트1 LRLLLRLLRRL     왼손 = 4, 오른손 = 2 일 때,
# LRLLLRLLLRL      5를 찾아야함

# 테스트2 LRLLRRLLLRR     0일 때를 찾아야함 0 == 11
# LLLLLRLRLRR


# 문제풀이(3)
def solution(numbers, hand):
    answer = ''
    left_numbers = [1,4,7]
    right_numbers = [3,6,9]
    
    left_s = 10
    right_s = 12
    
    for i in numbers:
        if i in left_numbers : # 1,4,7은 무조건 왼손
            answer += 'L'
            left_s = i
        elif i in right_numbers : # 3,6,9는 무조건 오른손
            answer += 'R'
            right_s = i
        else:                   # 2,5,8,0을 누르는 경우
            if i == 0:
                i = 11
            now_l = abs(left_s - i) // 3 + abs(left_s - i) % 3
            now_r = abs(right_s - i) // 3 + abs(right_s - i) % 3

            # print(i, left_s, now_l, right_s, now_r)

            if now_l < now_r :
                answer += 'L'
                left_s = i
            elif now_r < now_l:
                answer += 'R'
                right_s = i
            else:
                if hand == 'right':
                    answer += 'R'
                    right_s = i
                else:
                    answer += 'L'
                    left_s = i
            # answer += 'X'
            
    # print(hand)
    return answer

# 카카오 인턴 문제는 2주 뒤 한번 더 풀어봐라

# 거리를 구할 방법이 생각나지 않아 검색 해본결과
# 2가지 방법이 있었다.
# 1. 나와 같은 방법으로 풀지만 거리를 3으로 나누며 구하는 방법
# 2. 딕셔너리 형식을 사용하여 좌표를 구하고 좌표의 거리를
#     유클리드 거리, 멘하탄 거리 공식을 사용한 방법


# 다른 사람의 풀이(1)
def solution(numbers, hand):
    answer = ''
    key_dict = {1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)}

    left = [1,4,7]
    right = [3,6,9]
    lhand = '*'
    rhand = '#'
    for i in numbers:
        if i in left:
            answer += 'L'
            lhand = i
        elif i in right:
            answer += 'R'
            rhand = i 
        else:
            curPos = key_dict[i]
            lPos = key_dict[lhand]
            rPos = key_dict[rhand]
            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])
            if ldist < rdist:
                answer += 'L'
                lhand = i
            elif ldist > rdist:
                answer += 'R'
                rhand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i

    return answer

# 딕셔너리를 사용하여 좌표를 만들고
# 좌표와 유클리드 거리, 맨하탄 거리 공식으로
# 해결한 풀이

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))     # "LRLLLRLLRRL"
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))      # "LRLLRRLLLRR"
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))        # "LLRLLRLLRL"