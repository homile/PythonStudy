# Longest Common Prefix (가장 긴 공통 접두사)

# 링크: https://leetcode.com/problems/longest-common-prefix/

# 문제풀이(1)
def solution(strs):
   answer = ''
   result = []

   if len(strs) == 0:
      return answer

   for i in range(len(strs)):
      str_split = []
      for j in range(1, len(strs[0])):
         str_split.append(strs[i][:j])
      result.append(str_split)

   # print(result)
   for i in range(len(result[0])):
      for j in range(1, len(result)):
         # print(result[j][i])
         if (result[0][i] != result[j][i]):
            return answer
         else:
            answer = result[0][i]

   return answer

# for문을 너무 많이썻고 answer 값이 제대로 나오지 않음.
# 2중 for문으로만 해도 될 듯 


# 문제풀이(2)
def solution(strs):
   answer = ""

   if len(strs) == 0:
      return answer

   for i in range(len(strs[0])):
      for j in range(1, len(strs)):
         if (strs[0][i] != strs[j][i]):
            return strs[0][:i]

   return answer

# 리스트가 하나이며 문자가 하나일때 
# ex) strs = ["a"] -> Expected = "a"
#     my Output = ""
# 마지막 return 부분 고치면될듯
# 리스트를 정렬해줘야함 
# ["dog","racecar","car"]일 경우 
# 비교하여 같은 값이 나올 경우 짧은 것에서 긴것을 비교해야함.


# 문제풀이(2)
def solution(strs):
   answer = ""

   if len(strs) == 0:
      return answer

   strs.sort()

   for i in range(len(strs[0])):
      for j in range(1, len(strs)):
         if (strs[0][i] != strs[j][i]):
            return strs[0][:i]

   return strs[0]

print(solution(["flower","flow","flight"]))  # "fl"
print(solution(["dog","racecar","car"]))  # ""