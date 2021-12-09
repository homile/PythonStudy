# 완주하지 못한 선수 (hash)

# 문제설명 : https://programmers.co.kr/learn/courses/30/lessons/42576

# 예상풀이
# Hash를 사용하지 않은 풀이다. (성공하지 못한풀이(결과x))

# 문제풀이(1)
# def solution(participant, completion):
    
#     participant.sorted()
#     completion.sorted()
    
#     for i in range(len(participant)):
#         for j in range(len(completion)):
#             if participant[i] == completion[j]:
#                 participant[i].remove()
    
#     return participant


#Hash를 사용하지 않은 풀이다. (성공하지 못한풀이(결과x))

# 문제풀이(2)
# def solution(participant, completion):
#     answer = ''
#     participant.sort()
#     completion.sort()
    
#     for i in range(len(completion)):
#         if participant[i] != completion[i]:
#             answer = participant[i]
#         else:
#             answer = participant[-1]
    
#     return answer


# 테스트 케이스는 통과했지만, 제출은 성공하지 못했다

# 문제풀이(3)
def solution(participant, completion):
    
    participant.sort()
    completion.sort()
    
    for i, j in zip(participant, completion):
        if i != j :
            return i   
    return participant[-1]

# 처음에 participant와 completion 배열을 정렬을 해준다.
# zip 함수를 사용하여 participant와 completion 배열을 묶어준 뒤
# i와 j의 값이 같지 않다면 i를 return해주고
# 아니라면 participant배열의 마지막 값을 return 해준다.


# 다른 사람의 풀이(1)
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

# collections 모듈을 사용한 풀이다.


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))      # "leo"
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))        # "leo"
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))     # "mislav"