# [1차] 비밀지도

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/17681

# 문제접근
# 가장 처음으로 해야 할 일 10진수를 2진법으로 바꾼다.
# 2진법으로 바꾼 뒤 i번째 값이 1이면 #을 반환하는 함수를 작성한다.

# arr1, arr2의 #(벽)이 담길 배열을 두 개를 생성한다?
# answer 배열에 arr1, arr2의 #을 추가한다. 
# 어떻게?   answer[i] = arr1[i]
# arr1의 #을 먼저 추가 한 후 if문을 사용하여
# answer[i] == '' : answer[i] == arr2[i]


# 문제풀이(1)
def solution(n, arr1, arr2):
    answer = []
    a = []
    b = []
    
    for i in range(5):
        while arr1[i]:
            a.append(arr1[i]%2)
            arr1[i] = arr1[i]//2
        answer.append(a[i])
    print(a)
        # print(arr1[i], arr2[i])
    return answer


# 문제풀이(2)
def solution(n, arr1, arr2):
    answer = []
    a_list = []
    b_list = []    
    
    for i in range(5):
        a = ''
        b = ''
        while arr1[i]:
            a += str(arr1[i]%2)
            arr1[i] = arr1[i]//2
        a_list.append(a)
        while arr2[i]:
            b += str(arr2[i]%2)
            arr2[i] = arr2[i]//2
        b_list.append(b)
        
    print(a_list, b_list)
        # print(arr1[i], arr2[i])
    return answer

# 10진수를 2진수로 바꿈
# 이제 해야 할 것??
# 1을 #으로 바꾸고
# arr1과 arr2의 배열을 합친다.
# 배열의 수가 1일 경우
# 1만 출력하는 경우를 해결해야함
# arr2의 2진수 변환이 잘못됨


# 문제풀이(3)
def solution(n, arr1, arr2):
    answer = []   
    
    for i in range(n):
        a = ''
        b = ''
        
        while arr1[i]:
            a += str(arr1[i]%2)
            arr1[i] = arr1[i]//2
        
        while arr2[i]:
            b += str(arr2[i]%2)
            arr2[i] = arr2[i]//2
        if len(a) != n:
            a = a.rjust(n, '0')
        elif len(b) != n:
            b = b.rjust(n, '0')
        
        temp = ''
        print(a)
        for j in range(n):
            if a[j] == '1' or b[j] == '1':
                temp += '#'
            elif a[j] == '0' and b[j] =='0':
                temp += ' '
        answer.append(temp)
        
    # print(a_list, b_list)
        # print(arr1[i], arr2[i])
    return answer


# 문제풀이(4)
def solution(n, arr1, arr2):
    answer = []   
    
    for i in range(n):
        a = ''
        b = ''
        
        while arr1[i]:
            a += str(arr1[i]%2)
            arr1[i] = arr1[i]//2
        
        while arr2[i]:
            b += str(arr2[i]%2)
            arr2[i] = arr2[i]//2
        a,b = a.rjust(n,'0'),b.rjust(n,'0')
        temp = ''
        print(a,b)
        for j in range(n):
            if a[j] == '1' or b[j] == '1':
                temp += '#'
            elif a[j] == '0' and b[j] == '0':
                temp += ' '
        
        answer.append(temp)
        
    # print(a_list, b_list)
        # print(arr1[i], arr2[i])
    return answer


# 문제풀이(5) 성공
def solution(n, arr1, arr2):
    answer = []   
    
    for i in range(n):
        a = ''
        b = ''
        
        while arr1[i]:
            a += str(arr1[i]%2)
            arr1[i] = arr1[i]//2
        a = a[::-1]       
        while arr2[i]:
            b += str(arr2[i]%2)
            arr2[i] = arr2[i]//2
        b = b[::-1]
            
        a,b = a.rjust(n,'0'),b.rjust(n,'0')
        
        temp = ''
        print(a,b)
        for j in range(n):
            if a[j] == '1' or b[j] == '1':
                temp += '#'
            elif a[j] == '0' and b[j] == '0':
                temp += ' '
        answer.append(temp)
        
    return answer


# 문제풀이(6)
def solution(n, arr1, arr2):
    answer = []   
    
    for i in range(n):
        
        a = format(arr1[i],'b').zfill(n)
        b = format(arr2[i],'b').zfill(n)
        
        temp = ''
        print(a,b)
        for j in range(n):
            if a[j] == '1' or b[j] == '1':
                temp += '#'
            elif a[j] == '0' and b[j] == '0':
                temp += ' '
        answer.append(temp)
        
    # print(a_list, b_list)
        # print(arr1[i], arr2[i])
    return answer

# 10진수를 2진수로 변환하는 과정에 오류가 발생 
# format 형식으로 2진수로 변환 (2진수 변환하는 거 다시 찾아볼 것)
# ‘b’ = 2진수로 변환하는 내장함수
# zfill(n) = 문자열 n의 개수만큼 앞에 0을 삽입 == rjust


# 다른 사람의 풀이(1)
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer

# 내장함수 bin을 사용하여 2진수 변환
# 슬라이싱으로 앞자리 2번째 부터 시작하는 이유
# bin 함수를 사용하여 변환할 경우 앞에 2자리에 0b라고
# 2진수로 변환했다고 알려주는 문자가 삽입 되기 때문
# rjust로 문자열 n의 크기만큼 왼쪽 빈 곳에 0을 삽입

# 왼쪽이 비는 이유 만약 10진수 1일 경우
# 2진수로 변환 시 00001 이지만
# 실제로는 1만 나타나게 됨


# ["#####","# # #", "### #", "# ##", "#####"]
print(solution(5, [9, 20, 28, 18, 11], 	[30, 1, 21, 17, 28]))
# ["######", "### #", "## ##", " #### ", " #####", "### # "]
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))