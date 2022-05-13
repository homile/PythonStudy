# Search Insert Position
# 링크: https://leetcode.com/problems/search-insert-position/

# 문제풀이(1)
def solution(nums, target):
   answer = 0
   
   for i in range(len(nums)):
      if nums[i] == target:
         return i

   return answer

# 들어오지 않는 경우 근접한 값의 인덱스번호를 +한다?


# 문제풀이(2)
def solution(nums, target):
   
   if target in nums:
      return nums.index(target)

   count = 0
   for i in nums:
      print(i, count)
      # i가 target보다 커지면 count를 하나 증가시켜서 return
      if i > target:
         return count
      count += 1

   return len(nums) # 배열의 길이를 초과할 경우

print(solution([1,3,5,6], 5)) # 2
print(solution([1,3,5,6], 7)) # 4
print(solution([1,3,5,6], 2)) # 1