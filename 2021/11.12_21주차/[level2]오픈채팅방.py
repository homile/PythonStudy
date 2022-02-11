# 오픈 채팅방

# 문제 설명 : https://programmers.co.kr/learn/courses/30/lessons/42888

# 채팅방 입장시 "[닉네임]님이 들어왔습니다."
# 채팅방 퇴장시 "[닉네임]님이 나갔습니다."
# 채팅방에서 닉네임을 변경하는 방법 (2가지)
# 1. 채팅방을 나간 후, 새로운 닉네임으로 다시 들어간다.
# 2. 채팅방에서 닉네임을 변경한다.
# 2-1 닉네임을 변경할 때는 기존에 채팅방에 출력되어 있던
#     메시지의 닉네임도 전부 변경된다.
# 닉네임이 중복될 수 있음.

# 예상 풀이
# Enter(입장), Leave(퇴장), Change(변경)을 생각
# uid로 유저 고유번호 확인
# 뒤에 있는 닉네임으로 확인
# 공백을 기준으로 3분할하면 될듯? .split()


# 문제 풀이(1)
# def solution(record):
#     answer = []
    
#     for i in record:
#         com = i.split()
#         if com[0] == 'Enter':
#             a = '님이 들어왔습니다.'
#             answer.append(com[2]+a)
#         elif com[0] == 'Leave':
#             a = '님이 나갔습니다.'
#         elif com[0] == 'Change':
#             continue

#         # print(i)
#     print(com, a)
    
#     return answer

# uid를 dict형식으로 만들어야 할듯?

# 문제 풀이(2)
# def solution(record):
#     answer = []
#     r_dic = {}

#     for i in record:
#         uid = i.split()
#         if uid[0] =='Enter' or uid[0] == 'Change':
#             r_dic[uid[1]] = uid[2]
#         print(r_dic)

#     for i in record:
#         com = i.split()
#         if com[0] == 'Enter':
#             a = '님이 들어왔습니다.'
#             answer.append(com[2]+a)
#         elif com[0] == 'Leave':
#             a = '님이 나갔습니다.'

#         # print(i)
#     print(com, a)
    
#     return answer


# 문제 풀이(3)
# def solution(record):
#     answer = []
#     r_dic = {}

#     for i in record:
#         uid = i.split()
#         if uid[0] =='Enter' or uid[0] == 'Change':
#             r_dic[uid[1]] = uid[2]
#         # print(r_dic)

#     for i in record:
#         com = i.split()
#         if com[0] == 'Enter':
#             a = '님이 들어왔습니다.'
#             answer.append(r_dic[uid[1]]+'님이 들어왔습니다.')
#         elif com[0] == 'Leave':
#             a = '님이 나갔습니다.'
#             answer.append(r_dic[uid[1]]+'님이 나갔습니다.')

#         # print(i)
#     # print(com, a)
    
#     return answer

# Ryan만 출력함
# uid를 가져오는게 아니라 com으로 해야할듯 
# for문이 1회전할 때마다 변화해야 하기 때문

# 문제 풀이(4)
def solution(record):
    answer = []
    r_dic = {}

    for i in record:
        uid = i.split()
        if uid[0] =='Enter' or uid[0] == 'Change':
            r_dic[uid[1]] = uid[2]
        print(r_dic)

    for i in record:
        com = i.split()
        if com[0] == 'Enter':
            answer.append(r_dic[com[1]]+'님이 들어왔습니다.')
        elif com[0] == 'Leave':
            answer.append(r_dic[com[1]]+'님이 나갔습니다.')

        # print(i)
    # print(com, a)
    
    return answer


# 다른 사람의 풀이(1)
# def solution(record):
#     answer = []
#     namespace = {}
#     printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
#     for r in record:
#         rr = r.split(' ')
#         if rr[0] in ['Enter', 'Change']:
#             namespace[rr[1]] = rr[2]

#     for r in record:
#         if r.split(' ')[0] != 'Change':
#             answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

#     return answer

print(solution(["Enter uid1234 Muzi",  
"Enter uid4567 Prodo","Leave uid1234",
"Enter uid1234 Prodo","Change uid4567 Ryan"])) 
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", 
# "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]