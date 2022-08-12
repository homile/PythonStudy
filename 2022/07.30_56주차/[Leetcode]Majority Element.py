# Majority Element
# 링크: https://leetcode.com/problems/majority-element/

# 문제풀이(1)
def solution(nums):
  numsSet = set(nums)
  answer = 0
  
  for i in numsSet:
    if nums.count(i) > len(nums)/2:
      answer = i
      break
    
  return answer

print(solution([2,2,1,1,1,2,2]))  # 2