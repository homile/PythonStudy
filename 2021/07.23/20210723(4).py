# x만큼 간격이 있는 n개의 숫자

# 문제설명 : https://programmers.co.kr/learn/courses/30/lessons/12954

# 예상풀이

# 문제풀이(1)
# 1부터 n까지 for문으로 반복하여
# Answer배열에 x*i값을 넣어준다.
def solution(x, n):
    answer = []
    
    for i in range(1, n+1):
        answer.append(x * i)

    return answer

print(solution(2, 5))   # [2,4,6,8,10]
print(solution(4, 3))   # [4,8,12]
print(solution(-4, 2))  # [-4, -8]