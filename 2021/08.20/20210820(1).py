# 상호평가

# 문제설명: 

# 문제접근

# 문제풀이(1)
def solution(scores):
    answer = ''
    a = []
    for i in range(len(scores)):
        for j in range(len(scores)):
            a.append(scores[j][i])
            
            
    print(a)
    return answer

# 자신이 받은 점수를 가져오는 풀이지만
# 다른 사람이 받은 점수도 순차적으로 오는 문제 발생
# 해결 방안 a = []을 for i에 넣어준다.


# 문제풀이(2)
def scores_grade(g):
    
    if g >= 90 : grade = 'A'
    elif g >= 80 : grade = 'B'
    elif g >= 70 : grade = 'C'
    elif g >= 50 : grade = 'D'
    else : grade = 'F'
    
    return grade

def solution(scores):
    answer = ''
    for i in range(len(scores)):
        a = []
        for j in range(len(scores)):
            a.append(scores[j][i])
            
        if a[i] == min(a) and a.count(a[i]) == 1 : 
            del a[i]
        elif a[i] == max(a) and a.count(a[i]) == 1:
            del a[i]
            
        mean = sum(a) / len(a)
        # print(a, mean)
        answer += scores_grade(mean)
        # print(scores_grade(mean))
            
            
    return answer


print(solution([[100, 90, 98, 88, 65],
[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],
[24,90,94,75,65]]))     # FBABD