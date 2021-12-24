# 지문에 나와있는 것처럼 H-Index를 구하는 식을 알아야 풀 수 있을듯 하다.
# 과학자가 발표한 논문 n편, h번 이상 인용된 논문이 h편 이상
# 나머지 논문이 h번 이하 인용되었다면 h의 최댓값을 찾아라

# 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations(인용)
# n = len(citations), citations가 높을 수록 좋은 논문이다.
# 내림차순으로 정렬 : [6, 5, 3, 1, 0]
# i번째보다 논문이 인용된 수가 크거나 같다면 그것을 기준으로
# 좋은 논문인지 확인할 수 있다.

# def solution(citations):
#     answer = 0
#     citations.sort(reverse = True)  # 내림차순으로 정렬
    
#     for i in range(len(citations)):
#             if citations[i] >= i:
#                 answer += 1
#             else:
#                 break
#     print(citations)
#     return answer

# print(solution([3, 0, 6, 1, 5]))    # 3

# 위와 같이 할 경우 정확성 87.5가 나온다 
# 16문제중 11번과 16번이 틀렸다.
# 예상 할 수 있는 결과는
# 1. 논문별 인용횟수가 0회 이상인 경우를 계산해야하나?
# 2. len은 0부터 시작하지만 논문의 개수는 1부터 시작 해야한다는 것을 생각하지 않음
#    그러면 if citations[i] >= i: -> if citations[i] >= i+1:로 바꾸면 되나?

def solution(citations):
    answer = 0
    citations.sort(reverse = True)  # 내림차순으로 정렬
    
    for i in range(len(citations)):
        if citations[i] >= i+1:
            answer += 1
        else:
            break
            
    print(citations)
    return answer

print(solution([3, 0, 6, 1, 5]))    # 3
print(solution([0, 1, 1]))          # 1

# 예상 결과에서 0회 이상인 경우를 해보았으나 문제없이 돌아갔다
# 하지만 예상 결과 2번으로 테스트 케이스를 삽입 후 진행했다.
# [0, 1, 1] 일 경우 내림차순으로 정렬을 하게되면
# [1, 1, 0] 이다. 그렇다면 첫 번째로 인용 된 1에서 멈추고 돌았어야 했다.
# 하지만 2번째 까지 갔다
# 이유는 위에 예상한 결과와 같다.

# 다른 사람의 풀이 1
# def solution(citations):
#     citations.sort(reverse=True)
#     answer = max(map(min, enumerate(citations, start=1)))
#     return answer

# sort로 정렬해서 가장 큰값부터 작은값으로 정렬한후, enumerate로 (index, value)형태로 묶는다. 
# 그리고 최댓값(start = 1)부터 각 value에 대해 최솟값 value의 값을 min으로 추출하고,
#  이 추출된 값은 enumerate가 끝나는 citations 리스트의 크기에 해당하는 갯수가 나온다. 
# 이들을 map으로 묶으면, 한 value의 입장에서 보는 최솟값 value의 집합이 나온다. 
# 즉 h값들의 집합이나온다. h값중 최대값을 max로 뽑아서 출력하면 된다.