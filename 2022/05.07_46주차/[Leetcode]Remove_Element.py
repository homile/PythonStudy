# Remove Element
# 링크: https://leetcode.com/problems/remove-element/

# [문제접근]
# num배열에 val의 값이 존재하면 삭제한다.

# 문제풀이(1)  # 통과 x 
def solution(nums, val):

   while True:
      nums.remove(val)
      if nums.count(val) == 0:
         break

   return len(nums)


# while문 조건에서 error
# 처음에 for문으로 작성했지만 stack이 변화하여 힘듬

# 문제풀이(2)
def solution(nums, val):
   if len(nums) == 0 : return 0
         
   while nums.count(val):
      nums.remove(val)

   return len(nums)

print(solution([3,2,2,3], 3))    # 2, nums = [2,2,_,_]