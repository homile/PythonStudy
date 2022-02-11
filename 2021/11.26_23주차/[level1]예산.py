# 예산

# 문제 설명 : https://programmers.co.kr/learn/courses/30/lessons/12982
# 최대한 많은 부서의 물품을 구매하기 위함.
# 각 부서가 신청한 금액만큼을 모두 지원해야 함.
# ex) 1000원을 신청한 부서에는 정확히 1000원을 지원해야하며
#     1000원보다 적은 금액을 지원할 수 없음.
# 부서별 신청한 금액이 들어있는 배열 d, 예산 budget

# 예상 풀이
# 배열 d를 오름차순으로 정렬후 하나씩 더한값이
# 배열 budget을 넘지않는 부서의 개수를 구하면 됨.

# 문제 풀이(1)

def solution(d, budget):
    answer = 0
    hap = 0

    d.sort()

    for i in d:
        hap += i
        if hap > budget:
            break
        else:
            answer += 1

    return answer

print(solution([1,3,2,5,4], 9))     # 3
print(solution([2,2,3,3], 10))      # 4