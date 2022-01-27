# number에서 k개수 만큼 제거하여 큰 수를 만든다.
# 구할때 정렬을 하면 안된다.
# 순열로 구하는 것????
# itertools 중 combinations, permutations 사용??
# combination(리스트, 길이) / permutations(리스트, 길이)

# 또는 스택으로 하나씩 쌓아올려???
# 1924 -> 2개 -> [19, 12, 14, 92, 94, 24]

# First code

# from itertools import combinations

# def solution(number, k):
#     answer = ''

#     number = list(number)
#     number = list(map(''.join,combinations(number, len(number)-k)))
#     answer = str(max(number))

#     return answer

# print(solution("1924", 2))          # "94"
# print(solution("1231234", 3))       # "3234"
# print(solution("4177252841", 4))    # "775841"


# 지난주에 봤던 combinations를 사용하였으나 시간초과가 생김

# 생각할 수 있는 이유
# 모든 경우의 수를 combinations화 시키기 때문에 시간이 오래걸림
# 해결방안은 combinations 대신 효율성이 더 좋은
# stack을 사용하여 풀면 될 것 같음
# 그런데 어떻게?
# 빈스택에 number의 문자를 한글자씩 쌓아준다.
# 그다음 k개 만큼 빼준후
# stack에 있는 값을 join으로 붙여준다.

# Second code
# TC1 -> len(number) - k =  4 - 2 -> length = 2
# TC2 -> len(number) - k = 7 - 3 -> length = 4
# TC3 -> len(number) - k = 10 - 4 -> length = 6
# 위와 같은 식으로 자릿수를 정할 수 있다.
# 그러면 length = 만들어질 자릿수이다.
# 이 문제는 정렬를 해서 큰 수를 만드는 것이 아닌
# 정해진 문자를 두고 작은 수를 빼는 것이다.


# def solution(number, k):
#     answer = ''
#     stack = []

#     for i in number:
#         stack.append(i)

#     print(stack)

#     return answer

# print(solution("1924", 2))          # "94"
# print(solution("1231234", 3))       # "3234"
# print(solution("4177252841", 4))    # "775841"


# Third code
# 제출시 12번 문항이 통과하지 못함
# 12번의 경우 1000, 1 이면 100이 출려돼야함
# 하지만, 1000이 출력됨 k를 print 해본 결과
# k가 0이 되지 않고 끝나서 그럼
# 그럼 k가 0이 되지 않는 경우를 생각해야 함.

# def solution(number, k):
#     answer = ''
#     stack = []

#     for i in number:
#         while stack and stack[-1] < i and k > 0:
#             stack.pop()
#             k -= 1
#         stack.append(i)
#         print(k)

#     answer = ''.join(stack)
#     return answer

# print(solution("1924", 2))          # "94"
# print(solution("1231234", 3))       # "3234"
# print(solution("4177252841", 4))    # "775841"
# print(solution("1000", 1))          # "100" 12번 문항

# Fourth code
# 제출시 12번 문항이 통과하지 못함
# 12번의 경우 1000, 1 이면 100이 출력돼야함
# 하지만, 1000이 출력됨 k를 print 해본 결과
# k가 0이 되지 않고 끝나서 그럼
# 그럼 k가 0이 되지 않는 경우를 생각해야 함.

def solution(number, k):
    answer = ''
    stack = []

    for i in number:
        while stack and stack[-1] < i and k > 0:
            stack.pop()
            k -= 1
        stack.append(i)

    while k > 0: 
        stack.pop()
        k -= 1

    answer = ''.join(stack)
    return answer

print(solution("1924", 2))          # "94"
print(solution("1231234", 3))       # "3234"
print(solution("4177252841", 4))    # "775841"
print(solution("1000", 1))          # "100" 12번 문항