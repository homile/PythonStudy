# 두 개 뽑아서 더하기

# 문제설명 : https://programmers.co.kr/learn/courses/30/lessons/68644

# 예상풀이
# 정수를 하나씩 다 순차적으로 더해서 똑같은 값이 나온 것은
# List(set(answer))로 제거 한 뒤,
# Sorted로 정렬한 풀이다.

# 문제풀이(1)
def solution(numbers):
    answer = []        
    
    for i in range(len(numbers)):
        for j in range(1, len(numbers)):
            if i != j:
                answer += [numbers[i] + numbers[j]]
    
    answer = list(set(answer))
    
    return sorted(answer)        # sorted = list를 씌워준다

print(solution([2,1,3,4,1]))    # [2,3,4,5,6,7]
print(solution([5,0,2,7]))      # [2,5,7,9,12]