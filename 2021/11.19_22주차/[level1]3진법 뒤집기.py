# 3진법 뒤집기

# 문제 설명 : https://programmers.co.kr/learn/courses/30/lessons/68935

# 예상 풀이
# 10진수를 3진법으로 변경후 그 값을 reverse 시키고
# reverse한 값을 10진수로 다시 바꿔준다.

# 3진법으로 변환

# 문제 풀이(1)
def solution(n):
    answer = ''

    while n > 0:
        n, jin3 = divmod(n, 3)
        answer += str(jin3)

    return int(answer, 3)

# def solution(n):
#     answer = 0    
#     jin3 = ''
    
#     while n > 0:
#         n, mod = divmod(n, 3)
#         jin3 += str(mod)
        
#     answer = jin3[::-1]
    
        
#     return answer

print(solution(45))     # 45 -> 1200 -> 0021 -> 7
print(solution(125))    # 125 -> 11122 -> 22111 -> 229