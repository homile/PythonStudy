# 폰켓몬

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/1845

# 문제접근
# 1. [3번, 1번, 2번, 3번] 3번 = 2마리, 1번 = 1마리, 2번 = 1마리
# 2. 4마리의 폰켓몬을 경우의 수로 고르는 방법 = 6가지
# 3. 다른 종류의 폰켓몬을 몇 마리를 가져갈 수 있는가에 대한 문제
# 4. 몇 마리의 폰켓몬을 구해야 하는가? 
# 5. len(nums)/2 -> ex1) 4/2 = 2마리, ex2) 6/2 = 3마리, ex3) 6/2 = 3마리


# 문제풀이(1)
def solution(nums):
    answer = 0
    n = int(len(nums)/2)
    nums_list = list(set(nums))
    
    if n < len(nums_list):
        answer = n
    else:
        answer = len(nums_list)

    return answer


# 폰켓몬을 가져갈 수 있는 마릿수= len(ls)/2와
# 폰켓몬의 종류 = 중복제거 = len(set(ls))) 중
# Min으로 둘 중 작은 수를 return하면 답이 나온다.

# 다른 사람의 풀이(1)
def solution(ls):
    return min(len(ls)/2, len(set(ls)))


print(solution([3,1,2,3]))      # 2
print(solution([3,3,3,2,2,4]))  # 3
print(solution([3,3,3,2,2,2]))  # 2