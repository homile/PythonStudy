# 신고 결과 받기

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/92334
# 신입사원 무지는 게시판 불량 이용자를 신고하고 처리 결과를 메일로 발송하는 
# 시스템을 개발하려 합니다. 무지가 개발하려는 시스템은 다음과 같습니다.

# 각 유저는 한 번에 한 명의 유저를 신고할 수 있습니다.
# 신고 횟수에 제한은 없습니다. 서로 다른 유저를 계속해서 신고할 수 있습니다.
# 한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리됩니다.
# k번 이상 신고된 유저는 게시판 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 
# 정지 사실을 메일로 발송합니다.
# 유저가 신고한 모든 내용을 취합하여 마지막에 한꺼번에 게시판 이용 정지를 시키면서 
# 정지 메일을 발송합니다.
# 다음은 전체 유저 목록이 ["muzi", "frodo", "apeach", "neo"]이고, k = 2
# (즉, 2번 이상 신고당하면 이용 정지)인 경우의 예시입니다.

# 유저 ID	유저가 신고한 ID	설명
# "muzi"	"frodo"	"muzi"가 "frodo"를 신고했습니다.
# "apeach"	"frodo"	"apeach"가 "frodo"를 신고했습니다.
# "frodo"	"neo"	"frodo"가 "neo"를 신고했습니다.
# "muzi"	"neo"	"muzi"가 "neo"를 신고했습니다.
# "apeach"	"muzi"	"apeach"가 "muzi"를 신고했습니다.
# 각 유저별로 신고당한 횟수는 다음과 같습니다.

# 유저 ID	신고당한 횟수
# "muzi"	1
# "frodo"	2
# "apeach"	0
# "neo"	2
# 위 예시에서는 2번 이상 신고당한 "frodo"와 "neo"의 게시판 이용이 정지됩니다. 
# 이때, 각 유저별로 신고한 아이디와 정지된 아이디를 정리하면 다음과 같습니다.

# 유저 ID	유저가 신고한 ID	정지된 ID
# "muzi"	["frodo", "neo"]	["frodo", "neo"]
# "frodo"	["neo"]	["neo"]
# "apeach"	["muzi", "frodo"]	["frodo"]
# "neo"	없음	없음
# 따라서 "muzi"는 처리 결과 메일을 2회, "frodo"와 "apeach"는 
# 각각 처리 결과 메일을 1회 받게 됩니다.

# 이용자의 ID가 담긴 문자열 배열 id_list, 각 이용자가 신고한 이용자의 ID 정보가 담긴 
# 문자열 배열 report, 정지 기준이 되는 신고 횟수 k가 매개변수로 주어질 때, 
# 각 유저별로 처리 결과 메일을 받은 횟수를 배열에 담아 
# return 하도록 solution 함수를 완성해주세요.

# 문제접근
# https://ryu-e.tistory.com/109
# report에 있는 값을 set으로 중복을 제거한다.
# 제거하는 이유는 한명이 한명을 여러번 신고해도 누적횟수는 1로 증가하지 않는다.
# split으로 report에 있는 값중 신고자와 신고당한사람을 구분하여
# 신고 당한 사람을 count한 후 k와 비교한다.

# 문제풀이(1)
def solution(id_list, report, k):
    answer = []
    report_list = []
    
    for i in set(report):
        a = i.split()
        report_list.append(a)
    print(report_list)
    
    return answer

# 리스트보단 dictionary를 사용해야 할 것 같다.
# 초기 딕셔너리를 생성한다.

# 문제풀이(2)
def solution(id_list, report, k):
    answer = []
    user = {}   # 신고당한 사람 : 신고한 사람
    cnt = {}    # 신고당한 횟수

    for i in id_list:
        user[i] = []    # 유저명을 넣기 위함
        cnt[i] = 0      # 횟수를 count 하기 위함
    # print(user, cnt)
 
    for i in set(report):
        a, b = i.split()    # a가 b를 신고함
        user[a].append(b)
        cnt[b] += 1         # b가 신고당한 횟수
        print(a, b)
    print(user)
    print(cnt)

    for i in id_list:
        result = 0
        for j in user[i]:
            if cnt[j] >= k:
                result += 1
        answer.append(result)
        
    return answer


# 다른 사람의 풀이(1)
def solution(id_list, report, k):
    answer = []
    a = list(set(report))
    dictionary2 = {name : 0 for name in id_list}
    dictionary = {name : [] for name in id_list}
    for i in a:
        dictionary[i.split()[1]].append(i.split()[0])

    for i in dictionary:
        if len(dictionary[i]) >= k:
            for j in dictionary[i]:
                dictionary2[j] += 1

    for i in dictionary2:
        answer.append(dictionary2[i])

    return answer


# 다른 사람의 풀이(2)
def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer

# [2,1,1,0]
print(solution(["muzi", "frodo", "apeach", "neo"],
["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))

# [0,0]
print(solution(["con", "ryan"], 
["ryan con", "ryan con", "ryan con", "ryan con"], 3))