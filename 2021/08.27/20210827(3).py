# 최댓값과 최솟값

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/12939

# 문제접근

# 문제풀이(1)
def solution(s):
    answer = ''
    a = s.split(' ')
    a_min = min(a)
    a_max = max(a)
    
    answer += a_min
    answer += ' '
    answer += a_max
        
    # print('min' + a_min +'max'+ a_max)
    
    return answer

# 문자열을 빈공간을 기준으로 나눠서 정수를 입력 받는다
# 어떻게? split 함수 사용
# 정수를 입력 받고 최솟값과 최대값을 구한다.
# Testcase 2번을 보면 -4가 앞에 -1이 뒤에 있다.
# 그런데 min, max 함수를 사용하여 풀면
# -1이 최솟값으로 -4가 최대값으로 return 하는 상황이 발생했다.
# 음수일 경우 위치를 바꿔주는 방법을 생각해야한다.

# Testcase 2번을 통과하지 못함
# 예상 오류 : 문자열로 받아서 –를 부호가 아닌 문자로 인식
# 해결 방안 : 문자열대신 int(정수형)으로 받아본다


# 문제풀이(2)
def solution(s):
    answer = ''
    
    s_list = list(map(int, s.split(' ')))
    
    s_min = min(s_list)
    s_max = max(s_list)
    
    answer = str(s_min) + ' ' + str(s_max)
    
    return answer

# List(map)으로 문자열을 정수형으로 받은 다음
# S_list의 최솟값과 최댓값을 구해서
# Answer에 문자열로 합쳐준다.


# 다른 사람의 풀이(1)
def solution(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))

print(solution("1 2 3 4"))      # "1 4"
print(solution("-1 -2 -3 -4"))  # "-4 -1"
print(solution("-1 -1"))        # "-1 -1"