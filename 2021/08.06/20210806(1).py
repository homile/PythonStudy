# 시저암호

# 문제설명: 

# 예상풀이

# 문제풀이(1)
# 문자열을 어떻게 + 시킬까? -> 아스키코드로 하면 가능 어떻게?
# chr(97) = a : 아스키코드를 문자로 바꿔주는 함수
# ord('a') = 97 : 문자를 아스키코드로 바꿔주는 함수
# def solution(s, n):
#     answer = ''
    
#     for i in range(0, len(s)):     # 테스트 1은 통과함
#         a = chr(ord(s[i])+n)       # z 일 경우 ‘{‘가 출력 해결방안?
#         		             # 공백 해결?
#         print(ord(s[i]), n, a)
#         answer += ''.join(a)
        
#     return answer	


# 문제풀이(2)	
# def solution(s, n):
#     answer = ''
#     print(ord('A'), ord('Z'), ord('a'), ord('z')) # 65, 90, 97, 122
    
#     for i in range(0, len(s)):
#         if s[i] == ' ':
#             answer += ''.join(' ')       # 공백은 해결 했으나 여전히  z, Z 후의 출력해결 X
#         else:
#             a = chr(ord(s[i])+n)
#             answer += ''.join(a)
            
#         print(ord(s[i]), n, a)
    
        
#     return answer


# 문제풀이(3)
# def solution(s, n):
#     answer = ''
#     print(ord('A'), ord('Z'), ord('a'), ord('z')) # 65, 90, 97, 122
    
#     for i in range(0, len(s)):
#         if ord(s[i])+n > 90:
#             answer += ''.join(chr(ord(s[i])-26+n))         # z, Z + n 뒤의 내용 해결
#         elif s[i] == ' ':
#             answer += ''.join(' ')
#         else:
#             answer += ''.join(chr(ord(s[i])+n))
                
#     return answer


# 아스키코드 90 - 24 + n을 하면
# A부터 +n 한 만큼의 문자가 나올 수 있다.

# 문제풀이(4)
def solution(s, n):
    answer = ''
    print(ord('A'), ord('Z'), ord('a'), ord('z')) # 65, 90, 97, 122
    
    for i in range(0, len(s)):
        if 65 <= ord(s[i]) <= 90:
            if ord(s[i])+n > 90:
                answer += ''.join(chr(ord(s[i])-26+n))
            else : 
                answer += ''.join(chr(ord(s[i])+n))
                
        if 97 <= ord(s[i]) <= 122:
            if ord(s[i])+n > 122:
                answer += ''.join(chr(ord(s[i])-26+n))
            else :
                answer += ''.join(chr(ord(s[i])+n))
        if s[i] == ' ':
             answer += ''.join(' ')    
        
    return answer



# 문자열 s를 i번째 문자를 찾기 위해 리스트로 변환한다.
# 문자가 대문자이면 char
# s[i] = ‘A’ -> 65                 # s[i] - ord(‘A’) -> 0  
# s[i] – ord(‘A’) + n -> 1 
# (s[i] – ord(‘A’) + n) % 26 -> 1 

# Z일 경우 A부터 다시 시작하기 위함

# (s[i] – ord(‘A’) + n) % 26 + ord(‘A’) -> 66
# n의 개수, Z를 판별하고 남은 수에 문자의 처음인
# A의 아스키 코드를 더하면 n번째로 shift 한 문자 출력

# s[i] = 66 = ‘B’


# 다른 사람의 풀이(1)
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)


print(solution("AB", 1))        # "BC"
print(solution("Z", 1))         # "a"
print(solution("a B z", 4))     # "e F d"