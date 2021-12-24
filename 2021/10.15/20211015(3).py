# 소수찾기

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/42839

# 문제접근
# 소수를 판별하는 함수를 만들어 두고 
# 숫자를 조합하면 함수를 호출하여 소수 여부를 
# 확인하여 참이면 answer += 1을 해주면 될 것이다.

# 여기서 문제
# 숫자 조합을 어떻게 할 것인가? 
# 일반적으로 앞뒤를 판별하면서 하면 쉬울 것 같은데
# 길이가 7정도로 크다.
# 이에 해당하는 함수가 있나?

# 무한루프로 경우의 수를 구현해야 하나?

# 에라토스테네스의 체로 소수는 구별 할 수 있다.

# 문제풀이(1)
def PrimeNumber(n):	# 소수를 구하는 식
    if n < 2:
        return 0    
    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1


def solution(numbers):
    answer = 0
    # n_list = [numbers[i] for i in range(len(numbers))]
    n_list = []
    print(n_list)
        
    return answer

# 소수를 무작위로 구하는 식으로 했다.
# 에라토스테네스의 체를 쓰는게 조금 더 좋을 뻔했다.

# 이제는 경우의 수를 만드는 작업을 해야 하는데
# 막막 하다.!!


# 문제풀이(2)
def PrimeNumber(n):
    if n < 2:
        return 0    
    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1

def solution(numbers):
    answer = 0
    n_list = []
    for i in range(len(numbers)):
        set(n_list)
        n_list.append(numbers[i])
        answer += PrimeNumber(int(n_list[i]))
        for j in range(len(numbers)):
            set(n_list)
            n_list.append(numbers[i] + numbers[j])
            answer += PrimeNumber(int(n_list[i]))
        
    return answer

# 나의 풀이 2번에서 조금 더 풀어서 해봤는데
# TC 2번이 안되는 이유를 알았다 2중 for 문일 경우 2자리 수 까지 만들어주고
# 3자리 수 부터는 만들어지지 않았다. 


# 문제풀이(3)
def PrimeNumber(n):
    if n < 2:
        return 0    
    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1


def solution(numbers):
    answer = 0
    n_list = []
    for i in range(len(numbers)):
        n_list.append(numbers[i])
        for j in range(len(numbers)):
            n_list.append(numbers[i] + numbers[j])
    
    n_list = list(set(n_list))
    
    for k in range(len(n_list)):
        answer += PrimeNumber(int(n_list[k]))
        
    return answer

# 나의 풀이 2번에서 조금 더 풀어서 해봤는데
# TC 2번이 안되는 이유를 알았다 2중 for 문일 경우 2자리 수 까지 만들어주고
# 3자리 수 부터는 만들어지지 않았다. 


# 문제풀이(4)
from itertools import permutations

def PrimeNumber(n):
    if n < 2:
        return 0    
    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1

def solution(numbers):
    answer = 0
    n_list = []
    result = []
    for i in range(1, len(numbers)+1):
        n_list.extend(permutations(numbers, i))
        result = [int(''.join(i)) for i in n_list]
        
    result = list(set(result))
        
    for j in result:
        if PrimeNumber(j):
            answer += 1
    
    return answer

# itertools 라이브러리의 permutations 
# 내장함수를 사용하여 모든 경우의 수를
# 나타내고 중복을 제거하여
# 소수를 판별해주는 방법

# 저번 주 itertools의 사용법을 찾아보고
# 깨닫게 된 함수


# 다른 사람의 풀이(1)
def permutations(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in permutations(array[:i] + array[i+1:], r-1):
                yield [array[i]] + next

def check(num):
    if num == 0 or num == 1:
        return 0
    for x in range(2, num):
        if num % x == 0:
            return 0
    return 1

def solution(numbers):
    answer = set()
    for ll in range(1, len(numbers)+1):
        for arr in permutations(list(numbers), ll):
            tmp = int(''.join(arr))
            if check(tmp) == 1:
                answer.add(tmp)
    return len(answer)

# 이 풀이는 permutations 함수를 직접 만들어서 
# 풀이에 참조한 케이스를 가져와 보았다.
# 함수의 구조에 대해서 알 수 있었고
# 함수를 사용하지 못하는 경우에도 저 방법을 사용해서
# 풀면 될 것 같다.

print(solution("17"))   # 3
print(solution("011"))  # 2