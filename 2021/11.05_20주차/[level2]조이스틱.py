# 조이스틱

# 문제 설명 : https://programmers.co.kr/learn/courses/30/lessons/42860

# 예상 풀이
# 아스키 코드를 생각해보자
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# A = 65, Z = 90
# 문자열에 맞게 A의 개수를 맞춰준다.
# 문자열을 리스트로 치환한다.

# # 문제 풀이(1)
# def solution(name):
#     answer = 0
#     n_list = []
    
#     # 문자열을 아스키코드로 변환하여 리스트로 변환한다.
#     for i in name:
#         n_list.append(ord(i))        
    
#     print(n_list)
#     return answer


# # 문제 풀이(2)
# def solution(name):
#     answer = 0
#     n_list = []
#     num = 0
    
#     # 문자열을 아스키코드로 변환하여 리스트로 변환한다.
#     for i in name:
#         n_list.append(ord(i))        
    
#     while len(n_list) > num:
#         # num번째 값이 A가 아니라면 up, down 해서 가장 작은 값을 추출
#         if n_list[num] != 'A':
#             up = ord(name[num])-ord('A')
#             down = ord('Z')-ord(name[num])
#             answer += min(up,down)
#             print(up, down, min(up,down))
#         num += 1
    
#     print(n_list)
#     return answer

# 마지막 위치에서 조이스틱을 조작하는 방법을 찾아야함.
# 왼쪽과 오른쪽 이동에 대한 코드를 생성해야함.
# while을 2개 추가하여 만들면 될 듯?
# 아스키 코드로 바꿔두고 그걸 사용하지 않음 
# 처음부터 아스키코드로 안바꾸고 리스트화만 시키면 될 듯?

# # 문제 풀이(3)
# def solution(name):
#     answer = 0
#     n_list = list(name)
#     num = 0     
    
#     while True:
#         # num번째 값이 A가 아니라면 up, down 해서 가장 작은 값을 추출
#         if n_list[num] != 'A':
#             up = ord(n_list[num])-ord('A')
#             down = ord('Z')-ord(n_list[num])+1
#             answer += min(up,down)
#             print(up, down, min(up,down))

#         # 비교가 끝난 문자를 A로 치환
#         n_list[num] = 'A'
#         # 리스트의 모든 문자가 A일 경우 break
#         if n_list == ['A']*len(n_list): break
            
#         if n_list[num] == 'A': answer += 1
#         num += 1
    
#     print(n_list)
#     return answer

# TC 1번은 통과하였지만 2번은 통과하지 못함
# 예상 오류
# 다음 문자로 이동하는 중 76줄에 나온 answer += 1이
# 너무 많이 사용됨.
# 저 문장을 넣은 이유 : 다음 문자가 A일 경우 
# 뒤에부터 판별하기 위함 (왼쪽 이동)
# 해결 방안 오른쪽, 왼쪽 이동에 대한 부분을 조금 더 
# 명확하게 해줘야 함.

# # 문제 풀이(4)
# def solution(name):
#     answer = 0
#     n_list = list(name)
#     num = 0     
    
#     while True:
#         right = 1
#         left = 1
#         # num번째 값이 A가 아니라면 up, down 해서 가장 작은 값을 추출
#         if n_list[num] != 'A':
#             up = ord(n_list[num])-ord('A')
#             down = ord('Z')-ord(n_list[num])+1
#             answer += min(up,down)
#             # print(up, down, min(up,down))

#         # 비교가 끝난 문자를 A로 치환
#         n_list[num] = 'A'

#         # 리스트의 모든 문자가 A일 경우 break
#         if n_list == ['A']*len(n_list): break
        
#         # 오른쪽으로 이동시 A가 있다면 넘어가기 위해 answer += i 카운트
#         for i in range(1, len(n_list)):
#             if n_list[num+i]== 'A':
#                 right += i
#                 answer += i
#             else:
#                 break
        
#         num += 1
            
    
#     print(n_list)
#     return answer

# TC2는 통과하지만 TC1은 통과하지 못함
# 예상 이유
# 1. 오른쪽 단어가 A가 아닌 경우 answer += 1이 없음
# 2. 첫 번째 위치에 서 왼쪽으로 이동하는 경우가 없음

# # 문제 풀이(5)
# def solution(name):
#     answer = 0
#     n_list = list(name)
#     num = 0     
    
#     while True:
#         right = 1
#         left = 1
#         # num번째 값이 A가 아니라면 up, down 해서 가장 작은 값을 추출
#         if n_list[num] != 'A':
#             up = ord(n_list[num])-ord('A')
#             down = ord('Z')-ord(n_list[num])+1
#             answer += min(up,down)
#             # print(up, down, min(up,down))

#         # 비교가 끝난 문자를 A로 치환
#         n_list[num] = 'A'

#         # 리스트의 모든 문자가 A일 경우 break
#         if n_list == ['A']*len(n_list): break
        
#         # 오른쪽으로 이동시 A가 있다면 넘어가기 위해 right += i
#         for i in range(1, len(n_list)):
#             if n_list[num+i]== 'A':
#                 right += i
#             else:
#                 break
        
#         # 왼쪽으로 이동시 A가 있다면 넘어가기 위해 left += i
#         for i in range(1, len(n_list)):
#             if n_list[num-i] =='A':
#                 left += i
#             else:
#                 break
        
#         if right > left :
#             answer += left
#         else:
#             answer += right
#         num += 1
            
    
#     print(n_list)
#     return answer

# TC1은 통과하지만 TC2는 통과하지 못함 ㅠㅠㅠㅠㅠㅠ
# 이유가 멀까요?? num += 1???

# 문제 풀이(5)
def solution(name):
    answer = 0
    n_list = list(name)
    num = 0     
    
    while True:
        right = 1
        left = 1
        # num번째 값이 A가 아니라면 up, down 해서 가장 작은 값을 추출
        if n_list[num] != 'A':
            up = ord(n_list[num])-ord('A')
            down = ord('Z')-ord(n_list[num])+1
            answer += min(up,down)
            # print(up, down, min(up,down))

        # 비교가 끝난 문자를 A로 치환
        n_list[num] = 'A'

        # 리스트의 모든 문자가 A일 경우 break
        if n_list == ['A']*len(n_list): break
        
        # 오른쪽으로 이동시 A가 있다면 넘어가기 위해 right += i
        for i in range(1, len(n_list)):
            if n_list[num+i]== 'A':
                right += i
            else:
                break
        
        # 왼쪽으로 이동시 A가 있다면 넘어가기 위해 left += i
        for i in range(1, len(n_list)):
            if n_list[num-i] =='A':
                left += i
            else:
                break
        
        if right > left :
            answer += left
            num -= left
        else:
            answer += right
            num += right
            
    
    print(n_list)
    return answer

print(solution("JEROEN"))   # 56
print(solution("JAN"))      # 23