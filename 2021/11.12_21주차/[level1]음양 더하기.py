# 음양더하기

# 문제 설명
# 어떤 정수들이 있습니다. 이 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와 
# 이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다. 
# 실제 정수들의 합을 구하여 return 하도록 solution 함수를 완성해주세요.

# 예상 풀이
# 1. signs[i] = True 이면 absolutes[i]를 -로 변경후 sum

# 문제 풀이(1)
def solution(absolutes, signs):
    answer = 0

    for i in range(len(absolutes)):
        if signs[i] == False:
            absolutes[i] = -absolutes[i]
    
    answer = sum(absolutes)

    return answer

print(solution([4,7,12],[True,False,True]))
print(solution([1,2,3],[False,False,True]))

