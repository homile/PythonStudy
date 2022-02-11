# [3차] 파일명 정렬

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/17686
# 파일목록: ["img12.png", "img10.png", "img2.png", "img1.png"]
# 일반정렬: ["img1.png", "img10.png", "img12.png", "img2.png"]
# 숫자정렬: ["img1.png", "img2.png", "img10.png", "img12.png"]

# 구해야 하는 것은 문자 코드 순이 아닌, 파일명에 포함된 숫자를 반영한 정렬 기능
# 파일명은 크게 HEAD, NUMBER, TAIL의 세 부분으로 구성
# (muzi1.txt, MUZI1.txt, muzi001.txt, muzi1.TXT는 함께 입력으로 주어질 수 있다.)

# 문제접근
# 앞의 문자는 소문자 -> 숫자 -> 대문자-> 숫자 이순으로 정렬하며
# 마침표 뒷 부분은 위의 정렬한 후 소문자 -> 대문자로 정렬한다. (숫자 없음)
# split 함수를 사용하여 숫자와 문자를 분할한 뒤 
# 배열에 넣어 정렬을 하면되나???

# 문제풀이(1)
def solution(files):
    answer = []
    temp = []

    for i in files:
        head = ''
        number = ''
        tail = ''
        for j in range(len(i)):
            if i[j].isdigit():
                number += i[j]   
            else:
                head += i[j]
        temp.append([head, number, tail])
        print(temp)       

    return answer

# tail부분을 따로 추출해야함.
# 어떻게 -> head와 tail을 구분해야하지??
# number가 끝났을 경우를 판단해야할 듯


# 문제풀이(2)
def solution(files):
    answer = []
    temp = []

    for i in files:
        head = ''
        number = ''
        tail = ''
        check = 0       # 0이면 숫자를 만나지 못함, 1이면 숫자를 만남
        for j in range(len(i)):
            if i[j].isdigit():
                number += i[j]
                check = 1
            elif check == 0:
                head += i[j]
            else:
                tail += i[j]

        temp.append([head, number, tail])
        print(temp)       

    return answer

# 숫자와 문자를 구분하는데 성공!!
# 이제는 head -> number -> tail 순으로 정렬을 시행해야함.


# 문제풀이(3)
def solution(files):
    answer = []
    temp = []

    for i in files:
        head = ''
        number = ''
        tail = ''
        check = 0       # 0이면 숫자를 만나지 못함, 1이면 숫자를 만남
        for j in range(len(i)):
            if i[j].isdigit():
                number += i[j]
                check = 1
            elif check == 0:
                head += i[j]
            else:
                tail += i[j]

        temp.append([head, number, tail])
        print(temp)
    temp.sort()

    for i in range(len(temp)):
        answer.append(''.join(temp[i]))
    
    return answer

# sort로 정렬해봤지만 되지 않음
# 2021.12.03에 lambda를 사용하여 정렬한 적이 있으니
# 그것을 토대로 lambda를 사용해 봐야겠음.


# 문제풀이(4)    55.5/100.0
def solution(files):
    answer = []
    temp = []

    for i in files:
        head = ''
        number = ''
        tail = ''
        check = 0       # 0이면 숫자를 만나지 못함, 1이면 숫자를 만남
        for j in range(len(i)):
            if i[j].isdigit():
                number += i[j]
                check = 1
            elif check == 0:
                head += i[j]
            else:
                tail += i[j]

        temp.append([head, number, tail])
        print(temp)
    
    # temp.sort(temp, key=lambda x: (x[0].lower(), int(x[1])))
    temp = sorted(temp, key=lambda x: (x[0].lower(), int(x[1])))

    for i in range(len(temp)):
        answer.append(''.join(temp[i]))

    return answer

# 제출 시 점수가 55점이 나옴 이유를 생각해야함.
# tail부분이 문제일 수 있다는 질문하기를 봄
# https://programmers.co.kr/questions/13907


# 문제풀이(5)    통과
def solution(files):
    answer = []
    temp = []

    for i in files:
        head = ''
        number = ''
        tail = ''
        check = 0       # 0이면 숫자를 만나지 못함, 1이면 숫자를 만남
        for j in range(len(i)):
            if i[j].isdigit():  # 숫자일 경우
                number += i[j] 
                check = 1       # 숫자일 경우와 숫자가 끝난경우를 판별하기 위해서
            elif check == 0:
                head += i[j]
            else:
                tail = i[j:]    # 슬라이싱으로 해결(tail 부분이 없을 수 있다함.)
                break

        temp.append([head, number, tail])
        print(temp)
    
    # temp.sort(temp, key=lambda x: (x[0].lower(), int(x[1])))
    # 람다식사용 (0번째 인덱스를 소문자로 정렬 후 1번째 인덱스를 정수형으로 정렬)
    temp = sorted(temp, key=lambda x: (x[0].lower(), int(x[1])))    

    # 나누어진 문자열을 하나로 만들기
    for i in range(len(temp)):
        answer.append(''.join(temp[i]))

    return answer


# 다른 사람의 풀이(1)
import re

def solution(files):

    a = sorted(files, key=lambda file : int(re.findall('\d+', file)[0]))
    b = sorted(a, key=lambda file : re.split('\d+', file.lower())[0])

    return b

# re라이브러리를 통해 정규식사용
# 175 -> 문자로된 숫자를 int로 변환하여 정렬
# 176 -> 위의 정렬을 거친 값을 가지고 문자형으로 정렬

# 재홍이 풀이
# 3중 for문을 사용하여 head부분을 짜르고 남은 것을
# temp에 넣어주고 안에 있는 값을 넘버랑 tail로 잘라서 사용할 수 있다.

# ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))

# ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
