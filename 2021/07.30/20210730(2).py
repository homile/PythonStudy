# 2016년

# 문제설명 : 

# 예상풀이
# Month의 인덱스 배열에 week 배열을 매칭 시켜야 하는 것을
# 생각하지 못한 풀이다.

# 문제풀이(1)
# def solution(a, b):
#     answer = ''
#     month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    
#     for i in range(len(month)):
#         if i == a:
#             for j in range(1, month[i]+1):
#                 if j == b:
#                     answer = week[i]
            
#     return answer


# 문제풀이(2)
def solution(a, b):
    answer = 0
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    
    # 4월달까지의 마지막 일 수를 더한다.
    for i in range(a-1):
        answer += month[i]
        print(month[i])
    
    # 마지막 일 수를 더한 값에서 b의 일수를 더한다.
    answer += b-1
    print(answer)
    # 모든 일수를 더한 값을 일주일인 7을 나눈 나머지 값을 answer에 매치 시켜준다.
    answer = answer % 7
    print(answer)  
    # week 배열에서 나머지 값의 배열번호를 넣어주면 요일이 나온다.
    return week[answer]


# 다른 사람의 풀이(1)
# def getDayName(a,b):
#     months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
#     return days[(sum(months[:a-1])+b-1)%7]

print(solution(5, 24))      # "TUE"