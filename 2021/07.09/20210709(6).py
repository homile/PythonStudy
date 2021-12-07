# 핸드폰 번호 가리기

# 문제설명 : https://programmers.co.kr/learn/courses/30/lessons/12948

# 예상풀이
# 문자열 phone_number의 길이보다 -4 만큼 *을 answer에  삽입하고, 
# *표 뒤에 phone_numbe의 -4(뒤에서 4번째부터) 
# 뒷자리 4자리를 붙여준다.

# 문제풀이(1)
def solution(phone_number):
    
    answer = "*" * (len(phone_number)-4)
    answer += phone_number[-4:]
    
    return answer


# kang 풀이(1)
# replace 함수를 사용한 풀이
# def solution(phone_number):
    
#     answer = ''
    
#     for i in range(len(phone_number)-4):
#         answer += phone_number[i].replace(phone_number[i], '*')
#     answer += phone_number[-4:]
    
#     return answer

print(solution("01033334444"))      # "*******4444"
print(solution("027778888"))        # "*****8888"