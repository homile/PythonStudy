# 문자열 내 마음대로 정렬하기

# 문제설명 : https://programmers.co.kr/learn/courses/30/lessons/12915

# 예상풀이
# 문자열 s를 오름차순으로 정렬한다.
# 문자열의 n번째 값을 추출한뒤 다시 정렬한다.
# 맨 앞의 문자를 제거해서 리스트에 정렬

# 문제풀이(1)
def solution(strings, n) : 
    answer = []
    na = []

    # 리스트  strings의 i번째 문자열에서
    # n번째 문자를 맨 앞으로 재배치 후 i번째 문자열과
    # 합친 뒤 (car -> acar) 사전순으로 정렬
    for i in strings:                      
        i = i[n] + i                            
        na. append(i)                    
        na.sort()	

    # 합친 문자열을 맨 앞 (리스트의 0번째)를 제외한 후
    # answer에 append 함수를 사용하여 재배치
    for i in na:                              
        i = i[1:]                                
        answer.append(i)
 
    return answer


# lambda 함수를 사용
# lambda (): 이름이 없는 함수를 만들 수 있으며, 함수를 한 줄로 요약해주는 함수이다.

# 다른 사람의 풀이(1)
def solution(stirngs, n) : 
    return sorted(strings, key=lambda x: x[n])



print(solution(["sun", "bed", "car"], 1))       # ["car", "bed", "sun"]
print(solution(["abce", "abcd", "cdx"], 2))     # ["abcd", "abce", "cdx"]