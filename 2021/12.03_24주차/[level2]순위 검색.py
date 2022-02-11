# 순위검색

# 문제설명 : https://programmers.co.kr/learn/courses/30/lessons/72412
# 개발언어 항목에 cpp, java, python 중 하나를 선택해야 함.
# 지원 직군 항목에 backend와 frontend 중 하나를 선택해야 함.
# 지원 경력구분 항목에 junior와 senior 중 하나를 선택해야 함.
# 선호하는 소울푸드로 chicken과 pizza 중 하나를 선택해야 함.
# 위의 4개 항목에 맞는 지원자가 몇명인지 알아내고
# 획득한 코딩테스트 점수 하나의 문자열로 구성한 값의 배열 info
# 문의조건에 해당하는 사람들의 숫자를 순서대로 배열에 담아서 return

# 예상풀이
# 띄어쓰기를 기준으로 split해주고
# 그 값을 리스트에 담아 query에 해당하는 값을 가져온다?
# 점수는 무조건 있어야하지만 
# 개발언어, 직군, 경력, 소울푸드는 -로 제한사항이 없는 경우가 있다.

# 문제풀이(1)
# def solution(info, query):
#     answer = []

#     for j in query:
#         cnt = 0
#          # ' and '을 ' '으로 변경후 ' '으로 split
#         query_split = j.replace(' and ', ' ').split()
#         query_spec = query_split[:-1]
#         query_score = int(query_split[-1])
#         # print(query_spec, query_score)
#         for i in info:
#             user_info = i.split()
#             user_spec = user_info[:-1]
#             user_score = int(user_info[-1])

#             if user_score >= query_score :
#                 if user_spec[0] == query_spec[0] or query_spec == '-':
#                     print(user_spec[0], query_spec[0])
#                     cnt += 1
#             else:
#                 break
#         # print('===============================')
#         # print(user_info, user_spec, user_score, cnt)
#         # print(query_split, query_spec, query_score)

#     return answer


# 첫번째 것은 변화가 잘되었지만 2번째 지원자부터는
# split이 제대로 적용되지 않음

# 문제풀이(2)
# def solution(info, query):
#     answer = []

#     for j in query:
#         user = 0 
#          # ' and '을 ' '으로 변경후 ' '으로 split
#         query_split = j.replace(' and ', ' ').split()
#         query_spec = query_split[:-1]
#         query_score = int(query_split[-1])

#         for i in info:
#             cnt = 0
#             user_info = i.split()
#             user_spec = user_info[:-1]
#             user_score = int(user_info[-1])

#             if user_score >= query_score :
#                 for num in range(4):
#                     if user_spec[num] == query_spec[num] or query_spec[num] == '-':
#                         cnt += 1
                    
#         #     print(user_info, user_spec, user_score, cnt)
#             # print(cnt)
#             if cnt == 4 : 
#                 user += 1
#         answer.append(user)
#         # print('===')
#         # print(query_split, query_spec, query_score)

#     return answer


# TC와 제출시 18문제 올 통과하지만 효율성에서 0점 처리..
# 이걸 풀어나가야함..

# 문제풀이(3)
# def solution(info, query):
#     answer = []

#     for j in query:
#         user = 0 
#          # ' and '을 ' '으로 변경후 ' '으로 split
#         query_split = j.replace(' and ', ' ').split()
#         query_spec = query_split[:-1]
#         query_score = int(query_split[-1])

#         for i in info:
#             cnt = 0
#             user_info = i.split()
#             user_spec = user_info[:-1]
#             user_score = int(user_info[-1])

#             if user_score >= query_score :
#                 for num in range(4):
#                     if user_spec[num] == query_spec[num] or query_spec[num] == '-':
#                         cnt += 1
#                     else:
#                         break
                    
#         #     print(user_info, user_spec, user_score, cnt)
#             # print(cnt)
#             if cnt == 4 : 
#                 user += 1
#         answer.append(user)
#         # print('===')
#         # print(query_split, query_spec, query_score)

#     return answer


# 다른 사람의 풀이(1)
# https://dev-note-97.tistory.com/131
# https://whwl.tistory.com/193
from itertools import combinations
def solution(info, query):
    answer = []
    db = {}
    for i in info:                   # info에 대해 반복
        temp = i.split()
        conditions = temp[:-1]       # 조건들만 모으고, 점수 따로
        score = int(temp[-1])  
        for n in range(5):           # 조건들에 대해 조합을 이용해서  
            combi = list(combinations(range(4), n))
            for c in combi:
                t_c = conditions.copy()
                for v in c:          # '-'를 포함한 새로운 조건을 만들어냄.
                    t_c[v] = '-'
                changed_t_c = '/'.join(t_c)
                if changed_t_c in db:     # 모든 조건의 경우에 수에 대해 딕셔너리
                    db[changed_t_c].append(score)
                else:
                    db[changed_t_c] = [score]

    for value in db.values():             # 딕셔너리 내 모든 값 정렬
        value.sort()
 
    for q in query:                       # query의 모든 조건에 대해서
        qry = [i for i in q.split() if i != 'and']
        qry_cnd = '/'.join(qry[:-1])
        qry_score = int(qry[-1])
        if qry_cnd in db:                 # 딕셔너리 내에 값이 존재한다면,
            data = db[qry_cnd]
            if len(data) > 0:          
                start, end = 0, len(data)     # lower bound 알고리즘 통해 인덱스 찾고,
                while start != end and start != len(data):
                    if data[(start + end) // 2] >= qry_score:
                        end = (start + end) // 2
                    else:
                        start = (start + end) // 2 + 1
                answer.append(len(data) - start)      # 해당 인덱스부터 끝까지의 갯수가 정답
        else:
            answer.append(0)

    return answer

print(solution(["java backend junior pizza 150",
"python frontend senior chicken 210","python frontend senior chicken 150",
"cpp backend senior pizza 260","java backend junior chicken 80",
"python backend senior chicken 50"],
["java and backend and junior and pizza 100","python and frontend and senior and chicken 200",
"cpp and - and senior and pizza 250","- and backend and senior and - 150",
"- and - and - and chicken 100","- and - and - and - 150"]))        # [1,1,1,1,2,4]