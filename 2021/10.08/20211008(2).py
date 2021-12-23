# 가장 큰 수

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/42746

# 문제접근
# 배열에 담겨있는 숫자들 중 앞자리가 큰 값이 앞으로 오게 함
# 만약 3, 30, 34처럼 앞자리가 같은 값이 올 경우
# 어캐 비교 해야함?
# 6, 10, 2 -> 6666, 1010, 2222 -> 6210 ????
# 3, 30, 34, 5, 9 -> 9 5 34 3 30

# 1000 이하이기 때문에 4번 비교?

# 마지막으로 return 시 문자열로 바꾼다.


# 문제풀이(1)
def solution(numbers):
    answer = 0
    numbers1 = list(map(str, numbers))
    
    numbers1.sort(reverse = True)

    print(numbers1)
    
    return ''.join(numbers1)

# list(map)으로 숫자형을 문자형으로 바꿔서 sort로 정렬

# 3, 30, 34, 5, 9 일 경우 9, 5, 34, 3, 30 으로 정렬이 되어야 함.

# 어캐 하지??????????
# 1. 리스트에 있는 문자형으로 바꾼 숫자를 한 자리 씩 비교한다.
# 1번과 같이 할 경우 코드가 굉장히 길어져 효율성이 떨어질 듯

# 2. enumerate를 사용하여 인덱스 값을 넣어서
# 각 문자의 *3을 해서 정렬을 하면 되나?


# 문제풀이(2)
def solution(numbers):
    answer = 0
    numbers = list(map(str,numbers))
    a_list = []
    
    for i in numbers:
        a_list.append(i * 3)
        # print(a_list)
    
    a_list.sort(reverse = True)

    # print(a_list)
    
    return ''.join(numbers)

# 원하는 순서대로 정렬은 했으나
# 원하는 값을 뽑아내려면 dictionary 형식으로 
# 뽑아내야 할 거 같음


# 문제풀이(3)
def solution(numbers):
    answer = ''
    a_list = []
    
    for i, num in enumerate(numbers):
        a_list.append([str(num)*3, i])
    a_list.sort(reverse = True)
    
    for i in a_list:
        answer += str(numbers[i[1]])
    return answer

# 좌측과 같이 enumerate로 인덱스 번호를 매겨주고
# 문자열로 만든 것을 *3 하면
# [3, 30, 34, 5, 9] 
# 333, 303030, 343434, 555, 999가 된다.
# 이때 정렬을 하게 되면 문자열이기 때문에
# 34가 30보다 크다는 것을 튜플처럼 인식한다.
# 그렇기 때문에
# 999, 555, 343434, 333, 303030 으로 정렬이 됨.

# n_answer의 인덱스와 맞는 값을 출력

# 90.9로 한문제가 탈락함
# 예상 이유 : numbers=0일 경우를 생각하지 않음


# 문제풀이(4)
def solution(numbers):
    answer = ''
    a_list = []
    
    for i, num in enumerate(numbers):
        a_list.append([str(num)*3, i])
    a_list.sort(reverse = True)
    
    for i in a_list:
        answer += str(numbers[i[1]])
        
    if answer < "1" : 
        answer = "0"
        
    return answer

# 조건문으로 answer가 1보다 작을 경우
# answer =  “0”을 출력함


# 다른 사람의 풀이(1)
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))


# 다른 사람의 풀이(2)
import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer

print(solution([6, 10, 2]))         # "6210"
print(solution([3, 30, 34, 5, 9]))  # "9534330"