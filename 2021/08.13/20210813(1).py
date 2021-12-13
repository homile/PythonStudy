# k번째수

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/42748

# 문제접근
# 슬라이싱 기법을 사용한 풀이

# 문제풀이(1)
def solution(array, commands):
    answer = [] 
    for i in range(len(commands)):
        answer_list=array[commands[i][0]-1:commands[i][1]]
        answer_list.sort()
        
        answer.append(answer_list[commands[i][2]-1])
        print(answer_list)
        
    print(array[1-1], 'c', commands[1-1][1-1])
    return answer


# 다른 사람의 풀이(1)
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

print(solution([1,5,2,6,3,7,4], [[2,5,3],[4,4,1],[1,7,3]]))     # [5,6,3]