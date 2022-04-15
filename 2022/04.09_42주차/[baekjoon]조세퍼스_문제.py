# 조세퍼스 문제 (1158번)
# 링크: https://www.acmicpc.net/problem/1158

# 문제풀이(1)
# import sys 

# N, K = map(int, input().split())
# print(N, K)
# answer = []

# # 앉아 있는 순서
# people = [i for i in range(1, N+1)]
# print(people, 4 % 3)

# i = 0
# while (people):
#    print(people,i)
#    if i + K - 1 <= len(people):
#       i += K - 1
#       answer.append(people.pop(i))
#    elif (K-1) % len(people)-1 < len(people):
#       i = (K-1) % len(people) -1
#       answer.append(people.pop(i))
#    else:
#       answer.append(people.pop())


# print(answer)


# 남아 있는 사람의 범위를 초과한다면 
# 현재 있는 사람의 수 % k = 다음 죽을 사람을 구할 수 있다.
# 3 -> 6 # 남은 순서 1 2 4 5 7
# 2 -> 7 # 남은 순서 1 4 5
# 5 -> 1 -> 4

# 마지막 3개가 남았을 경우 정상 출려되지 않음.
# 조건문을 수정하면 될 듯?


# 문제풀이(2)
import sys 

N, K = map(int, input().split())
print(N, K)
answer = []

# 앉아 있는 순서
people = [i for i in range(1, N+1)]
print(people, 4 % 3)

i = K - 1
while (people):
   print(people,i)
   if i >= len(people):
      i = i % len(people)
   else:
      answer.append(str(people.pop(i)))
      i += K - 1

print('<', ', '.join(answer),'>', sep='')


# while문과 for문의 시간은 88ms로 같지만 코드 길이는 for문이 26줄 짧다.


# 다른 사람의 풀이(1)
N,K = map(int,input().split())
arr = [i for i in range(1,N+1)]    # 맨 처음에 원에 앉아있는 사람들

answer = []   # 제거된 사람들을 넣을 배열
num = 0  # 제거될 사람의 인덱스 번호

for t in range(N):
    num += K-1  
    if num >= len(arr):   # 한바퀴를 돌고 그다음으로 돌아올때를 대비해 값을 나머지로 바꿈  
        num = num%len(arr)
 
    answer.append(str(arr.pop(num)))
print("<",", ".join(answer)[:],">", sep='')


# 7 3    # <3, 6, 2, 7, 5, 1, 4>