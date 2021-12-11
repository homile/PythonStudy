# 체육복 (탐욕법, Greedy)

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/42862

# 문제접근
# 학생들 n - 체육복이 없는 학생들 len(lost)
# 5 - 2 = 3, 여벌 체육복이 있는지 판별해야 함.


# 테스트 케이스 1번, 테스트는 7, 11, 13번 통과

# 문제풀이(1)
# def solution(n, lost, reserve):
#     answer = 0
                            
#     for i in range(n):
#         if i-1 in lost:
#             lost.remove(i-1)
#         elif i+1 in lost:
#             lost.remove(i+1)
    
#     answer = n-len(lost)

#     return answer


# 다른 사람의 풀이(1)
def solution(n, lost, reserve):
    
    set_r = set(reserve) - set(lost)	# 여벌이 있던 학생 중 잃어버린 학생 빼고 빌려줄 수 있는 학생
    set_l = set(lost) - set(reserve)	# 잃어버린 학생 중 여벌이 없는 학생
    
    for i in set_r:			# 좌우를 판별해야 하는 경우는 
        if i-1 in set_l :			# 좌측을 먼저 판별해야 한다.(i-1, 같은 숫자는 싫어 문제와 같음)
            set_l.remove(i-1)		# 좌측에 여벌 체육복이 없을 경우 여벌이 없는 학생의 값을 제외
        elif i+1 in set_l :		
            set_l.remove(i+1)		# 우측에 여벌 체육복이 없을 경우 여벌이 없는 학생의 값을 제외
        
    return n-len(set_l)		# 전체 인원 n 중 여벌 체육복이 없는 인원의 수 제외


print(solution(5, [2, 4], [1, 3, 5]))   # 5
print(solution(5, [2, 4], [3]))         # 4
print(solution(3, [3], [1]))            # 2