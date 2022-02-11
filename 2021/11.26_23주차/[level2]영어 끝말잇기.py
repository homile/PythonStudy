# 영어 끝말잇기

# 문제 설명 : https://programmers.co.kr/learn/courses/30/lessons/12981
# 1번부터 차례대로 진행
# 마지막 사람이 말하면 1번부터 다시시작
# 이전에 등장한 단어사용 X
# 한 글자 단어사용 X

# 예상 풀이
# 사용된 단어를 새 배열에 추가한 후 
# 다음에 말하는 단어가 추가한 배열에 존재할 경우 fail
# count를 n만큼 해서 n번째가 끝나면 다시 1번으로 돌아오도록 count
# or i%n +1

# 문제 풀이(1)
# def solution(n, words):
#     answer = []
#     use_words = []
#     count = 0
#     turn = 0

#     for i in range(len(words)):
#         turn = i%n+1
#         if words[i] in use_words:
#             answer.append(turn)
#             answer.append(count)
#             break

#         if turn == 1:
#             count += 1

#         use_words.append(words[i])

#         # print(i%n+1)
        
#     return answer

# TC2
# 끝까지 틀린사람이 없을 경우를 추가해야함.

# TC3
# 같은 단어를 말했을 경우의 답은 찾았지만
# 마지막 단어의 마지막 알파벳이
# 다음 사람의 첫 알파벳과 다를 경우를 생각하지 않음.

# 문제 풀이(2)
# def solution(n, words):
#     answer = []
#     use_words = []
#     count = 0
#     turn = 0

#     for i in range(len(words)):
#         # 순번 기억
#         turn = i%n+1
#         if words[i] in use_words:
#             answer = [turn, count]
#             break
#         # 틀린 사람이 없을 경우
#         else:
#             answer = [0, 0]

#         # 반복 횟수
#         if turn == 1:
#             count += 1

#         use_words.append(words[i])
#         # print(i%n+1)
        
#     return answer


# 앞서 생각한 TC3에 대한 코드를 작성해야함.

# 문제 풀이(3)
# def solution(n, words):
#     answer = []
#     use_words = []
#     count = 0
#     turn = 0

#     for i in range(len(words)):
#         # 순번 기억
#         turn = i%n+1
#         if words[i] in use_words:
#             answer = [turn, count]
#             break
#         # 틀린 사람이 없을 경우 (이코드 제외시 TC3 통과)
#         else:
#             answer = [0, 0]

#         # 반복 횟수
#         if turn == 1:
#             count += 1

#         # if len(use_words) >= 1:
#         #     print(use_words[-1][-1], words[i][0])
#         if len(use_words) >= 1 and use_words[-1][-1] != words[i][0]:
#             answer = [turn, count]

#         use_words.append(words[i])
#         # print(i%n+1)
        
#     return answer


# 틀린 사람이 없을 경우의 조건을 따로 계산행야 한다.
# TC는 올 통과하지만 정확성 30.0/100.0으로 실패

# 조건문을 다시 생각해보자.
# 1. words[i] in use_words을 not in으로 ??
# 2. count를 샐수있는 방안???
# 3. 알파벳 비교???

# 문제 풀이(4)
def solution(n, words):
    answer = [0, 0]
    use_words = []
    # 시작 문자 (비교할 항목을 만듬)
    use_words.append(words[0])
    count = 0
    turn = 0

    for i in range(1, len(words)):
        if words[i] not in use_words and use_words[-1][-1] == words[i][0]:
            use_words.append(words[i])
        else:
            # 순번 기억
            turn = i%n+1
            # 횟수 기억
            count = i//n+1
            answer = [turn, count]
            break
        
    return answer

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))   # [3, 3]
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", 
"ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))           # [0, 0]
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))                       # [1, 3]