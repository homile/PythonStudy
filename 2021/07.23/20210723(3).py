# 나누어 떨어지는 숫자 배열

# 문제설명 : https://programmers.co.kr/learn/courses/30/lessons/12910

# 예상풀이

# 문제풀이(1)
# 테스트는 통과하지만 채점에서
# 5,6,7,8,13만 통과하였다.
# def solution(arr, divisor):
#     answer = []
    
#     for i in range(len(arr)):
#         if arr[i] % divisor == 0:
#             answer.append(arr[i])
#         elif len(answer) == 0:
#             answer.append(-1)
            
#     return sorted(answer)


# 문제풀이(2)
# for 문에 if랑 elif로 answer=0일 때를 구하면 첫번째 배열이 0일 수도 있다는 것을 
# 생각하지 못해서 첫번째 풀이에서 오류가 났다.
# 그렇기 때문에 for문이 끝난 후 if로 answer=0일 때를 구해서 오류를 해결 했다.
def solution(arr, divisor):
    answer = []
    
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])
    if len(answer) == 0:
        answer.append(-1)
            
    return sorted(answer)

print(solution([5, 9, 7, 10], 5))   # [5, 10]
print(solution([2, 36, 1, 3], 1))   # [1, 2, 3, 36]
print(solution([3,2,6], 10))        # [-1]