# Longest Substring Without Repeating Characters
# 링크: https://leetcode.com/problems/longest-substring-without-repeating-characters/

# [문제]
# 문자열이 주어지면 문자를 반복하지 않고 가장 긴 부분 문자열s 의 길이를 찾습니다.

# [문제접근]
# 문자열을 하나씩 더해서 중복되는 문자가 없다면 count를 한다.

# 문제풀이(1)     # Runtime Error
def solution(s):
   answer = []

   for i in range(len(s)):
      count = 1
      s_str = s[i]
      for j in range(i+1, len(s)):
         if s[j] not in s_str:
            s_str += s[j]
            count += 1
         else:
            answer.append(count)
            break

   return max(answer)

# max함수를 사용시 에러남
# 빈 리스트일 경우의 에러라함


# 문제풀이(2)
def solution(s):
   answer = 0

   for i in range(len(s)):
      count = 1
      s_str = s[i]
      for j in range(i+1, len(s)):
         if s[j] not in s_str:
            s_str += s[j]
            count += 1
         else:
            if count >= answer:
               answer = count
            break

   return answer

# 제출 시 "" = 0, " " = 1으로 빈칸도 count를 해야함
# 그럼 위의 식은 틀림
# stack으로 풀면될듯


# 문제풀이(3)
def solution(s):
   answer = 0
   stack = []

   for i in s:
      # 스택에 들어있지 않다면 삽입
      if i not in stack:
         stack.append(i)
      else:
         # 스택에 들어있다면 몇번째인지 확인
         index = stack.index(i)
         
         # 중복되는 인덱스까지의 값을 모두 제거
         for _ in range(index + 1):
            stack.pop(0)
         
         stack.append(i)
      # 가장 긴 값 비교
      answer = max(answer, len(stack))

   return answer


print(solution("abcabcbb"))   # 3
print(solution("bbbbb"))      # 1
print(solution("pwwkew"))     # 3
print(solution(" "))          # 1
print(solution(""))           # 0