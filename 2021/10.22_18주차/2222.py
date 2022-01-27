
def solution(people, limit):
    answer = 0
    people.sort(reverse = True)
    start = 0
    end = len(people)-1
    while start < end: #end 값은 for i in range(len(people)): 이라고 생각. 마지막값.
        if people[start]+people[end] <= limit:
            answer += 1
            start += 1
            end -= 1
        else:
            answer += 1
            start += 1
    answer += len(people[start:end+1]) #슬라이싱 끝낼 위치로 end는 포함이 안되기 떄문에 +1
    print(start)
    print(end)
    print(people) #len([3:3]) = 0 , len([2:3]) = 1
    return answer
print(solution([70, 50, 80, 50],100)) #3
# print(solution([70, 80, 50],100)) #3