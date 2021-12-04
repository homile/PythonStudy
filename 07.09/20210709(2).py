# 직사각형 별찍기

# 문제설명 : https://programmers.co.kr/learn/courses/30/lessons/12969

# 예상풀이
# 첫번째 for 문은 행을 구현하고,
# 두번째 for 문은 열을 구현하는 풀이이다.

# 문제풀이(1)
a, b = map(int, input().strip().split(' '))

for i in range(b):
    for j in range(a):
        print('*', end='') 
    print('')


# Answer에 ‘*’을 a 번만큼 곱해서 출력하고, 
# \n 줄 바꿈 연산자를 사용하여 행을 바꾼 뒤 
# b만큼 앞의 내용을 실행한다.

# 다른 사람의 풀이(1)
a, b = map(int, input().strip().split(' '))

answer = ('*'*a +'\n')*b

print(answer)