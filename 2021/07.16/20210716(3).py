# 자릿수 더하기

# 문제설명 : 

# 예상풀이
# 정수를 string 형으로 변형하여
# 한 문자 씩 정수형으로 더하는 풀이다.

# 문제풀이(1)
def solution(n):
    answer = 0
    
    for i in str(n):
        answer += int(i)

    return answer


# 다른 사람의 풀이(1)
# def sum_digit(number):
#     if number < 10:
#         return number;
#     return (number % 10) + sum_digit(number // 10) 

print(solution(123))    # 6
print(solution(987))    # 24