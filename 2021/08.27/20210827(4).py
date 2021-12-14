# 최솟값 만들기

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/12941

# 문제접근
# A = [1, 4, 2], B = [5, 4, 4]
# 1 x 5 = 5, 4 x 4 = 16, 2 x 4 = 8   sum = 29
# 1 x 4 = 4, 4 x 5 = 20, 2 x 4 = 8   sum = 32

# A = [1, 2], B = [3, 4]
# 1 x 3 = 3, 2 x 4 = 8    sum = 11
# 1 x 4 = 4, 2 x 3 = 6    sum = 10

# 경우의 수로 곱하고 더한 값 중 가장 작은 값을 return 한다.
# 가장 작은 값과 가장 큰 값을 더하는 식으로 하면 
# 더했을 때 가장 작은 수가 나오게 된다.
# 그렇다면 A는 작은 수부터, B는 큰 수부터 정렬 하면 될듯?


# 문제풀이(1)
def solution(A,B):
    answer = 0
    
    A = sorted(A)  # 123
    B = sorted(B, reverse = True)  # 654
    
    for i in range(len(A)):
        answer += (A[i]*B[i])
    
    print(A,B)

    return answer

# list A는 작은 값부터 정렬
# list B는 큰 값부터 정렬
# 가장 작은 값과 가장 큰 값을 곱한 후
# 곱한 값을 더한 풀이


# 다른 사람의 풀이(1)
def getMinSum(A,B):
    return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))
