# 모의고사

# 문제설명: 

# 문제접근

# 문제풀이(1)
# def solution(answers):
#     answer = []
#     list1 = [1, 2, 3, 4, 5]                
#     list2 = [2, 1, 2, 3, 2, 4, 2, 5]      
#     list3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  
    
#     count1 = 0
#     count2 = 0
#     count3 = 0
    
#     for i in range(len(answers)):
#         if answers[i] == list1[i]:
#             count1 += 1
#         if answers[i] == list2[i]:
#             count2 += 1
#         if answers[i] == list3[i]:
#             count3 += 1
#     m = max(count1, count2, count3)
    
#     if count1 == m : answer.append(1)
#     if count2 == m : answer.append(2)
#     if count3 == m : answer.append(3)
    
#     return answer

# 테스트 케이스는 통과하지만
# 제출 결과는 런타임 에러
# 예상오류 정답(answers)의 길이가 list1,2,3보다 큰 경우
# 오류발생 할 가능성 있음

# 문제풀이(2)
def solution(answers):
    answer = []
    list1 = [1, 2, 3, 4, 5]                 
    list2 = [2, 1, 2, 3, 2, 4, 2, 5]        
    list3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  
    
    count1 = 0
    count2 = 0
    count3 = 0
    
    for i in range(len(answers)):
        if answers[i] == list1[i%len(list1)]:
            count1 += 1
        if answers[i] == list2[i%len(list2)]:
            count2 += 1
        if answers[i] == list3[i%len(list3)]:
            count3 += 1
    m = max(count1, count2, count3)
    
    if count1 == m : answer.append(1)
    if count2 == m : answer.append(2)
    if count3 == m : answer.append(3)
    
    return answer

print(solution([1,2,3,4,5]))    # [1]
print(solution([1,3,2,4,2]))    # [1,2,3]