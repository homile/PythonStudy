# 테두리 1줄은 갈색으로 칠
# brown은 8이상이기 때문에 3행이 최소행이다. row
# yellow는 1이상이기 때문에 3열이 최소열이다. col
# row >= col
# brown = 0, yellow = 1 
# [0, 0, 0, 0]
# [0, 1, 1, 0]
# [0, 0, 0, 0]

# x = 2a/ -b +- 루트 b^2-4ac

def solution(brown, yellow):
    answer = []
    s = brown + yellow          # 카펫의 전체 칸수
    for i in range(s, 2, -1):   # 가로 구하기
        if s % i == 0:
            a = s//i
            print(a, s, i)
            if yellow == (i-2)*(a-2):
                return [i,a]
    return answer

print(solution(10, 2))      # [4, 3]
print(solution(8, 1))       # [3, 3]
print(solution(24, 24))     # [8, 6]