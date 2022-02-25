# n^2 배열 자르기

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/87390
# 정수 n, left, right가 주어집니다. 다음 과정을 거쳐서 1차원 배열을 만들고자 합니다.

# n행 n열 크기의 비어있는 2차원 배열을 만듭니다.
# i = 1, 2, 3, ..., n에 대해서, 다음 과정을 반복합니다.
# 1행 1열부터 i행 i열까지의 영역 내의 모든 빈 칸을 숫자 i로 채웁니다.
# 1행, 2행, ..., n행을 잘라내어 모두 이어붙인 새로운 1차원 배열을 만듭니다.
# 새로운 1차원 배열을 arr이라 할 때, arr[left], arr[left+1], ..., arr[right]만 
# 남기고 나머지는 지웁니다.
# 정수 n, left, right가 매개변수로 주어집니다. 
# 주어진 과정대로 만들어진 1차원 배열을 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ n ≤ 107
# 0 ≤ left ≤ right < n2
# right - left < 105

# 문제접근
# 첨부된 애니메이션과 같이 2차원 배열에 값을 채워준다.
# 2차원 배열을 1차원 배열로 변환한다.
# 변환된 배열을 사용하여 인덱스번호 left부터 rigth까지의 값을 출력한다.

# 문제풀이(1)   # 실패
def solution(n, left, right):
    answer = []
    list1 = [[0 for _ in range(n)] for _ in range(n)]   # 빈 배열 생성
    list2 = []
    for i in range(len(list1)):
        for j in range(len(list1[0])):
            if j+1 < i+1:
                list1[i][j] = i + 1
                list2.append(i+1)
            else:
                list1[i][j] = j + 1
                list2.append(j+1)
    print(list1)

    for i in range(left, right+1):
        answer.append(list2[i])

    return answer

# 실패한 이유 n의 개수가 n^7까지 나오게 된다.
# 그렇기 때문에 for문이 많이 돌아가면 실행시간이 길어진다.
# 시간 초과가 난다.
# 그렇다면 다른 방법(규칙)을 찾아내야한다.


# 문제풀이(2)
def solution(n, left, right):
    answer = []
    list1 = [[0 for _ in range(n)] for _ in range(n)]   # 빈 배열 생성
    for i in range(len(list1)):
        for j in range(len(list1[0])):
            if j+1 < i+1:
                answer.append(i+1)
            else:
                answer.append(j+1)

    # for i in range(left, right+1):
    #     answer.append(answer[i])

    return answer[left:right+1]
    


# 문제풀이(3) 
def solution(n, left, right):
    answer = []
    
    for i in range(left, right+1):
        answer.append(max(divmod(i,n))+1)

    return answer

# i를 n으로 나누면 해당하는 행과 열을 구할 수 있다.
# max(행, 열) + 1 = 행과 열의 위치에 있는 값이다.
# https://sangsangss.tistory.com/197

print(solution(3, 2, 5))    # [3,2,2,3]
print(solution(4, 7, 14))   # [4,3,3,3,4,4,4,4]