# Longest Palindromic Substring

# 링크: https://leetcode.com/problems/longest-palindromic-substring/

# Palindrome: 원본과 거꾸로된 것과 같은 문장이나 단어

# 문제풀이(1)
def solution(s):
   answer = ""

   for i in range(len(s)+1):
      if s[:i] == ''.join(list(reversed(s[:i]))):
         answer = s[:i]

   return answer

# 한자리씩 증가하면서 체크해야하기 때문에 2중for문 or while?
# 앞 뒤로 줄여가면서도 만들어 줘야함. 

# 문제풀이(2)
def solution(s):
   answer = ""
   stack = []
   count = 0

   for i in range(1, len(s)+1):
      stack.append(s[:i])
   print(stack)

   for j in range(count, len(s)):
      # print(j, s[j:])
      stack.append(s[j:])
      count += 1

   right, left = 0, 0
   for j in range(1, len(s)):
      stack.append(s[right:left])
      right += 1
      left -= 1

   stack.sort(key=lambda x:len(x))
   print(stack)

   for k in range(len(stack)):
      if stack[k] == stack[k][::-1]:
         answer = stack[k]

   return answer

# 홀 수 일 경우 풀리지 않음
# for문을 너무 많이 사용하여 시간초과 날 듯 -> 의외로 안남
# https://leetcode.com/problems/longest-palindromic-substring/discuss/2925/Python-O(n2)-method-with-some-optimization-88ms.


# 문제풀이(3)
def solution(s):
   if len(s) == 0:
      return 0
   
   maxLen = 1
   start = 0
   for i in range(len(s)):
      print(i, s[i-maxLen-1:i+1], s[i-maxLen:i+1])
      if i-maxLen >= 1 and s[i-maxLen-1:i+1] == s[i-maxLen-1:i+1][::-1]:
         start = i-maxLen-1
         maxLen += 2
         continue

      if i-maxLen >= 0 and s[i-maxLen:i+1] == s[i-maxLen:i+1][::-1]:
         start = i-maxLen
         maxLen += 1

   return s[start:start+maxLen]

# https://siahn95.tistory.com/entry/Python-LeetCode-5-Longest-Palindromic-Substring

print(solution("babad"))   # "bab"
print(solution("cbbd"))    # "bb"
print(solution("aacabdkacaa")) # "aca"