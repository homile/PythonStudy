# 제일 작은 수 제거하기

# 문제설명 : https://programmers.co.kr/learn/courses/30/lessons/12935

# 예상풀이
# Min 함수를 사용하여 리스트 arr의 가장 작은 값을 찾아낸 뒤
# Remove 함수로 리스트 arr에서 가장 작은 값을 뺀다.
# 그리고 리스트가 0개가 된다면 -1를 리스트 arr에 넣어준다.

# 문제풀이(1)
def solution(arr):          
    
    arr.remove(min(arr))
    
    if len(arr) == 0:
        arr += [-1]
    
    return arr

print(solution([4,3,2,1]))  # [4,3,2]
print(solution([10]))       # [-1]