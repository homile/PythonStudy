# 자연수 뒤집어 배열로 만들기

# 문제설명 : https://programmers.co.kr/learn/courses/30/lessons/12932

# 예상풀이
# 정수형을 문자로 바꿔준 다음 map함수를 사용하여 다시 
# 정수형으로 바꿔주는 풀이.

# 문제풀이(1)
# Testcase는 통과하지만 제출에서 3,13번만 통과한다.
# def solution(n):
    
#     n = str(n)
   
#     return  sorted(map(int, n), reverse=True)


# 문제풀이(2)
# Sorted 함수를 사용하지 않고, 문자열로 바꾼 n값을 
# answer에 하나씩 정수형으로 넣은 뒤 reverse함수로 문자열을 뒤집었다.
# 첫번째 풀이가 틀렸던 이유는 sorted를 하게 되면 1453를 5431로 정렬하기 때문에 
# 값을 먼저 하나씩 뒤집에서 넣어주는 방법으로 풀어야 했다.
def solution(n):
    answer = []
    n = str(n)
    
    for i in n:
        answer.append(int(i))
    answer.reverse()
    
    return answer


# 다른 사람의 풀이(1)
# def digit_reverse(n):
#     return list(map(int, reversed(str(n))))

print(solution(12345))  # [5,4,3,2,1]