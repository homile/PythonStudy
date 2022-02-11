# 점프와 순간이동

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/12980 
# 한 번에 K 칸을 앞으로 점프하거나,
# (현재까지 온 거리) x 2에 해당하는 위치로 순간이동을 할 수 있음.
# 순간이동을 하면 건전지 사용량이 줄어들지 않음
# 앞으로 K 칸을 점프하면 K 만큼의 건전지 사용량이 줄어듬.
# 건전지 사용량의 최솟값을 return

# 문제접근
# 이문제 상당히 이상하다고 생각됨
# 이유는 1칸을 이동하고 마지막 위치까지 x2로 순간이동만 해도 되지 않나?
# 가야하는 거리 N에 반으로 나눈다음
# 반을 가고 x2를 하면 가장 적게 나올 것 같다.
# 위의 접근은 잘못됐다는 것을 ex3을 통해 알았다.
# 5000 //2 -> 2500 //2 -> 1250 //2 -> 625 //2 -> 312//2
# 위와 같이 계속 2로 나눈 나머지 값이 0이면 점프하고
# 나머지 값이 0이 아니면 +1를 진행하면 될듯?

# 문제풀이(1)
def solution(n):
    answer = 0
    # word = ''
    while n > 0:
        q, r = divmod(n, 2)
        # word += str(r)
        # print(word)
        n = q
        print(q, r)
        if r != 0:
            answer += 1
    
    return answer


# 다른 사람의 풀이(1)
def solution(n):
    return bin(n).count('1')

# bin함수를 사용하여 2로 나누고 그 나머지 값이 1이면 count해주는 식

print(solution(5))      # 2
print(solution(6))      # 2
print(solution(5000))   # 5