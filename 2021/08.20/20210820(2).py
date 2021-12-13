# 피보나치 수

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/12945

# 문제접근

# 문제풀이(1)
# def solution(n):
#     answer = 0
#     f = []
#     if n == 1 :
#         return 1
#     for i in range(n):
#         if i == 0:
#             f[i] = 0
#         elif i == 1:
#             f[i] = 1
#         else:
#             f[i] = f[i-1] + f[i-2]
#     print(f)
#         		# 피보나치 수를 대략적으로 풀어 봄
#     return answer	# 하지만 테스트는 통과하지 못함


# 문제풀이(2)
# def solution(n):
#     answer = []
    
#     for i in range(n+1):
#         if i == 0 or i == 1 :
#             answer.append(i)
#         else:
#             # 코드를 %1234567을 하는 것을 몰랐다.
#             answer.append((answer[i-1]+answer[i-2]))		
#     return answer[-1]

# 테스트케이스는 통과하고 제출은 통과하지 못했다.


# 문제풀이(3)
def solution(n):
    answer = []
    
    for i in range(n+1):
        if i == 0 or i == 1 :
            answer.append(i)
        else:
            answer.append((answer[i-1]+answer[i-2])%1234567)
    
    return answer[-1]


# 다른 사람의 풀이(1)
def fibonacci(num): 	    # a = 0, b = 1로 둔다 
    a,b = 0,1		        # (피보나치 수열은 0, 1로 시작)
    for i in range(num):	# num 만큼 실행하고
        a,b = b,a+b		    # a = b로 b = a + b로 바꾸는 연산
    return a		        # 왼쪽과 같이 사용하게 되면 동시에
			                # 연산을 하기 때문에 한 줄 씩 작성하는 것과 값이 다르다.
			                # %1234567을 하지 않은 것은 결국 n번째 피보나치 수와
			                # %1234567을 한 값이 같기 때문이다.

print(solution(3))      # 2
print(solution(5))      # 5