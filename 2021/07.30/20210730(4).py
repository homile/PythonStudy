# 하샤드 수

# 문제설명 : 

# 예상풀이

# 문제풀이(1)
def solution(x):
    xs = str(x)         # x를 문자열로 바꿔준다.
    xsum = 0          # 자릿수의 합의 변수
    
    for I in range(len(xs)):    # xs의 길이만큼 반복한다.
        xsum += int(xs[i])       # 좌, 우의 값을 더한다.
        if x % xsum == 0:       # x / xsum의 나머지가 0이면
            answer = True        # 하샤드 수 True
        else:
            answer = False
    
    return answer


# 다른 사람의 풀이(1)
def Harshad(n):
    
    return n % sum([int(c) for c in str(n)]) == 0

print(solution(10)) # True
print(solution(12)) # True
print(solution(11)) # False
print(solution(13)) # False