# 행렬의 덧셈

# 문제설명 : https://programmers.co.kr/learn/courses/30/lessons/12950

# 예상풀이

# 문제풀이(1)
# # answer의 배열의 길이를 어떻게 할 것인가?
# IndexError: list assignment index out of range
# 배열이 지정되어 있는 arr1에 덮어써서 해결
# Answer에 배열의 길이를 새로 추가하여 해결
def solution(arr1, arr2):
    #answer = [[0]*len(arr1[0]) for _ in range(len(arr1))]
                                       
    for i in range(len(arr1)):                       
        for j in range(len(arr1[i])):  # IndexError: list assignment index out of range
            arr1[i][j] += arr2[i][j]   # answer의 배열의 길이를 어떻게 할 것인가?                                      
    
    return arr1


# 다른 사람의 풀이(1)
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer

print(solution([[1,2],[2,3]], [[3,4],[5,6]]))       # [[4,6],[7,9]]
print(solution([[1],[2]], [[3],[4]]))               # [[4],[6]]
