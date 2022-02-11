# [3차]n진수 게임

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/17687 
# 1.숫자를 0부터 시작해서 차례대로 말한다. 
#   첫 번째 사람은 0, 두 번째 사람은 1, … 열 번째 사람은 9를 말한다.
# 2.10 이상의 숫자부터는 한 자리씩 끊어서 말한다. 
#   즉 열한 번째 사람은 10의 첫 자리인 1, 열두 번째 사람은 둘째 자리인 0을 말한다.
# 진법 n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p 가 주어진다.
# 자신이 말해야 하는 숫자를 스마트폰에 미리 출력해주는 프로그램을 만들려고 한다. 
# 튜브의 프로그램을 구현하라.

# 문제풀이 끝난후 찾아보니 챔퍼나운 수라는 수학 상수를 이용한 문제라고 한다.

# 문제접근
# 딕셔너리로 10~15를 A~F로 매칭? or 문자열 지정?
# 자기가 말해야하는 숫자를 말하기 위해서는 총 게임 횟수를 구해야함. = t*m
# ex1) 4번 말해야 하므로 4*2(인원수) = 8회 중 자기차례는
#      p%8 -> p+m 반복
# 진법 계산식 

# 문제풀이(1)
# 16진법으로 풀기위한 A~F까지의 값 지정
dict_16 = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
# base = 진법
def base(n, b):
    q, r = divmod(n, b)
    return q

def solution(n, t, m, p):
    answer = ''
    # 게임 최대 길이
    game_length = t*m

    for i in range(game_length):
        if i == 0:
            answer += '0'
        else:
            answer += str(base(n,i))

    return answer

# 진수로된 값을 가져왔으나 변환된 값을 가져와야 했다.
# 값도 제대로 나오지 않음


# 문제풀이(2)
# 16진법으로 풀기위한 A~F까지의 값 지정
dict_16 = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
# base = 진법
def base(n, b):
    q, r = divmod(n, b)
    if q == 0:
        return r
    else:
        return base(q, b)

def solution(n, t, m, p):
    answer = ''
    # 게임 최대 길이
    game_length = t * m

    for i in range(game_length):
        if i == 0:
            answer += '0'
        else:
            answer += str(base(i, n))

    return answer

# 진법 변환에 대한 결과를 정확하게 했으나
# 16진법으로 변환할 경우 A~F로 반환되는 것을 하지 못함.


# 문제풀이(3)
# 16진법으로 풀기위한 A~F까지의 값 지정
dict_16 = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
# base = 진법
def base(n, b):
    q, r = divmod(n, b)
    if q == 0:
        return r
    else:
        return base(q, b)

def solution(n, t, m, p):
    answer = ''
    word = ''
    # 게임 최대 길이
    game_length = t * m

    for i in range(game_length):
        if i == 0:
            word += '0'
        else:
            word += str(base(i, n))

    # 자신이 말해야하는 답
    for i in range(len(word)):
        if (i%game_length)+1 == p:
            # print((i%game_length)+1)
            answer += word[i]
            p += m

    return answer

# 16진법으로 변환하는 과정을 거쳐야함
# 16이후의 값이 111111로 출력됨.


# 문제풀이(4)
# base = 진법
def base(n, b):
    # 16진법으로 풀기위한 A~F까지의 값 지정
    dict_16 = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    temp = ''
    while n > 0:
        n, r = divmod(n, b)
        if r >= 10:
            temp += dict_16[r]
        else:
            temp += str(r)
    return temp[::-1]   # 17이상의 변환 값을 나타내기 위함.

def solution(n, t, m, p):
    answer = ''
    word = ''
    # 게임 최대 길이
    game_length = t * m

    # 게임의 모든 답
    for i in range(game_length):
        if i == 0:
            word += '0'
            continue

        word += str(base(i, n))
    
    print(word)

    # 자신이 말해야하는 답
    for i in range(p-1, game_length, m):    # p-1 자신의 순서부터 시작, 총 게임길이, m인원수
        answer += word[i]

    return answer


# 다른 사람의 풀이(1)
def solution(n, t, m, p):
    data = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    numbers = "0"
    for number in range(1, t*m):
        temp = ''
        while number > 0:
            temp = data[number%n] + temp
            number //= n
        numbers += "".join(temp)

    return numbers[p-1:t*m:m]

# 0~F까지의 값을 리스트에 담아 참고할 수 있음.
# while에서 진수를 변환함.

print(solution(2,4,2,1))        # "0111"
print(solution(16,16,2,1))      # "02468ACE11111111"
print(solution(16,16,2,2))      # "13579BDF01234567"