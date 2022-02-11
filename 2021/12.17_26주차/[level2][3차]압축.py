# [3차]압축

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/17684
# 무손실 압축 알고리즘을 구현
# LZW 압축 (Lempel-Ziv-Welch)
# 1. 길이가 1인 모든 단어를 포함하도록 사전을 초기화한다.
# 2. 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다.
# 3. w에 해당하는 사전의 색인 번호를 출력하고, 입력에서 w를 제거한다.
# 4. 입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록한다.
# 5. 단계 2로 돌아간다.

# 문제접근
# ord,chr 를 사용하여 번호를 가져오고
# A-Z까지의 아스키 값을 담은 딕셔너리를 만들고
# 배열에 없는 새로운 단어가 나온다면 추가하고
# 있는 단어가 나온다면 그 값을 출력하면 될듯?

# 문제풀이(1)
def solution(msg):
    answer = []
    english_dict = {}

    # A~Z까지의 아스키코드 값을 딕셔너리에 넣음
    for i in range(65, 91):
        english_dict[chr(i)] = i-64
    print(english_dict)

    return answer

# 딕셔너리에 넣은 값을 msg의 i번째 값과 비교하여
# 맞는 값을 추출하고, 현재 글자 i와 다음 글자 i+1을 합친 문자열을
# 딕셔너리에 key와 value 값을 추가해야한다.


# 문제풀이(2)
def solution(msg):
    answer = []
    english_dict = {}

    # A~Z까지의 아스키코드 값을 딕셔너리에 넣음
    for i in range(65, 91):
        english_dict[chr(i)] = i-64
    # print(english_dict, english_dict.keys())

    for i in range(len(msg)):
        # msg[i] 문자가 english_dict 안에 있다면 answer에 append
        if msg[i] in english_dict.keys():
            answer.append(english_dict[msg[i]])

    return answer

# 해당하는 문자열의 아스키 값을 추출하는데 까진 성공
# 이제는 새로운 문자열을 Z문자 뒤에 KA이런식으로
# 추가하는 작업을 해야함.


# 문제풀이(3)
def solution(msg):
    answer = []
    english_dict = {}

    # A~Z까지의 아스키코드 값을 딕셔너리에 넣음 (26개)
    for i in range(65, 91):
        english_dict[chr(i)] = i-64
    # print(english_dict, english_dict.keys())

    front = 0
    end = 0
    num = 27

    while True:
        end += 1
        if end == len(msg):
            answer.append(english_dict[msg[front:end]])
            print(english_dict[msg[front:end]])
            print(msg)
            break

        # 새로운 문자열을 만들기 위함.
        if msg[front:end+1] not in english_dict.keys():
            print(msg[front:end+1], num)
            english_dict[msg[front:end+1]] = num
            num += 1
            answer.append(english_dict[msg[front:end]])
            front = end

    # print(english_dict)

    return answer

print(solution("KAKAO"))                        # [11, 1, 27, 15]
print(solution("TOBEORNOTTOBEORTOBEORNOT"))     # [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
print(solution("ABABABABABABABAB"))             # [1, 2, 27, 29, 28, 31, 30]