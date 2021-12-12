# 부족한 금액 계산하기

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/82612

# 문제접근
# 제출 결과 : 테스트 4번만 통과하지 못함
# 오류 예상 : 금액이 부족하지 않은 경우를 생각하지 않음.

# 문제풀이(1)
# def solution(price, money, count):
#     answer = -1
#     total_price = 0
    
#     for i in range(1, count+1):
#         total_price += price*i
    
#     answer = total_price - money
#     print(total_price, price, i)

#     return answer


# 문제풀이(2)
def solution(price, money, count):
    total_price = 0
    
    for i in range(1, count+1):
        total_price += price*i
    
    if total_price < money:		# money가 total_price보다 크다면 
        answer = 0				# 금액이 부족하지 않은 경우이기 때문에 
    else:						# answer = 0을 return 한다.
        answer = total_price - money

    return answer


# 다른 사람의 풀이(1)
def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)


print(solution(3,20,4))     # 10
