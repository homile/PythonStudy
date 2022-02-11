# 스킬트리

# 문제 설명 : https://programmers.co.kr/learn/courses/30/lessons/49993
# 선행 스킬 순서 = skill
# 유저들이 만든 스킬트리 = skill_trees
# 스킬 중복 없음

# ex1) skill = "CBD" , skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
# 가능 스킬트리 = "CBADF", "AECB"

# 예상 풀이
# 1. 위의 예를 보았을때 선행스킬 순서에 존재하는 스킬을 제외시킨다.
# 2. 순서를 skill과 맞는지 확인한다.

# 문제 풀이(1)
# def solution(skill, skill_trees):
#     answer = 0
#     result = []

#     for i in range(len(skill_trees)):
#         st = ''
#         for j in range(len(skill_trees[i])):
#             if skill_trees[i][j] in skill:
#                 st += skill_trees[i][j]
#         print(st)
#         result.append(st)

#     return answer


# 스킬트리와는 상관없는 알파벳은 제거했다.
# 제거한 문자를 가지고 가능한 스킬트리의 개수를 찾으면 된다.


# 어캐?
# for, while을 써서 반복?

# 문제 풀이(2)
# def solution(skill, skill_trees):
#     answer = 0
#     result = []

#     for i in range(len(skill_trees)):
#         st = ''
#         for j in range(len(skill_trees[i])):
#             if skill_trees[i][j] in skill:
#                 st += skill_trees[i][j]
#         result.append(st)

#     for k in result:
#         if k in skill:
#             answer += 1

#     print(result)

#     return answer


# 위와 같이 풀경우 BD도 C가 없어도 통과해서 
# answer가 3이 나온다.
# skill을 리스트로 하나씩 추가해서 비교할 항목을 더 늘리면 될듯?


# TC는 통과 제출 점수 28.6
# 생각할 수 있는 이유??
# result2에 모든 경우의 수가 담기지 않음
# 선행지에 없고 일반 스킬일 경우들이 있을 수 있음
# skill = BDA skill_trees=['EWQQR']
# 일경우 result2가 비어도 통과가 되야함 
# result2에 초기값 ''을 지정하면 될 듯 

# 문제 풀이(3)
# def solution(skill, skill_trees):
#     answer = 0
#     result = []
#     result2 = []
#     skill_list = list(skill)
#     # print(skill_list)
#     skill_str = ''

#     for s in skill_list:
#         skill_str += s
#         result2.append(skill_str)

#     for i in range(len(skill_trees)):
#         st = ''
#         for j in range(len(skill_trees[i])):
#             if skill_trees[i][j] in skill:
#                 st += skill_trees[i][j]
#         result.append(st)

#     for k in result:
#         if k in result2:
#             answer += 1       
#     print(result2)

#     return answer



# 문제 풀이(4)
def solution(skill, skill_trees):
    answer = 0
    result = []
    result2 = ['']
    skill_list = list(skill)
    # print(skill_list)
    skill_str = ''

    # 선행 스킬트리 순서대로 찍는 경우의 수를 담음
    for s in skill_list:
        skill_str += s
        result2.append(skill_str)

    # 유저가 정한 스킬트리에서 선행스킬트리에 속하지 않는 것을 골라냄
    for i in range(len(skill_trees)):
        st = ''
        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] in skill:
                st += skill_trees[i][j]
        result.append(st)

    # 위에서 골라낸 유저가 정한 스킬트리 중
    # 경우의 수에 해당하는 것을 찾아냄
    for k in result:
        if k in result2:
            answer += 1
    print(result2)

    return answer

# 재홍이 문제풀이(1)
# def solution(skill, skill_trees):
#     answer = 0
#     cnt = 0
#     for i in skill_trees:
#         skill_list = list(skill)
#         for j in range(len(i)):
#             if i[j] in skill_list:
#                 if i[j] == skill_list[0]:
#                     skill_list.pop(0)
                    
#                 else:
#                     cnt +=1
#                     break
                
#     answer = len(skill_trees) - cnt
    
#     return answer
# print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"])) #re


# 다른 사람의 풀이(1)
# def solution(skill, skill_trees):
#     answer = 0

#     for skills in skill_trees:
#         skill_list = list(skill)

#         for s in skills:
#             if s in skill:
#                 if s != skill_list.pop(0):
#                     break
#         else:
#             answer += 1

#     return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))   # 2