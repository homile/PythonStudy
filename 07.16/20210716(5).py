# 같은 숫자는 싫어

# 문제설명 : https://programmers.co.kr/learn/courses/30/lessons/12906

# 예상풀이
# 리스트의 처음에 arr[0]의 값을 넣어준다
# answer 리스트에 0번째는 값이 들어있기 때문에 1부터 시작한다.
# 배열의 앞뒤를 비교할 수 있다. arr[i] == arr[i+1]로 처음에 비교했지만 
# 앞만 비교할 뿐 뒤를 비교하지 않아 하나만 제거하는 경우가 생겼다.

# 문제풀이(1)
def solution(arr):
    answer = []
    answer.append(arr[0])

    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i]) 
    
    return answer


# 다른 사람의 풀이(1)
# def no_continuous(s):
#     a = []
#     for i in s:
#         if a[-1:] == [i]: continue
#         a.append(i)
#     return a

print(solution([1,1,3,3,0,1,1]))    # [1,3,0,1]
print(solution([4,4,4,3,3]))        # [4,3]