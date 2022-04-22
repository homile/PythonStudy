# Remove Duplicates from Sorted Array

# 링크: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# [문제접근]
# nums는 내림차순으로 정렬되어 있다. (따로 정렬하지 않아도 됨)
# 중복인 값은 _로 치환하고 뒤에 이어 붙인다.
# 중복을 count 한다.
# 입력받은 리스트 nums의 길이 - count를 하면 K가 나온다.
# 입력받은 리스트 nums에서 중복을 제거하여 stack에 담고 뒤에 count 만큼 _을 붙여준다.

# 문제풀이(1)
def solution(nums):
   # 중복 제거한 값을 넣을 리스트
   stack = []
   # 중복 개수 count
   count = 0

   for i in range(len(nums)):
      if len(stack) == 0:
         stack.append(nums[i])
      
      if nums[i] not in stack:
         stack.append(nums[i])
      else:
         count += 1
   
   print(count, stack)
   k = len(stack)

   for i in range(len(nums)-count):
      stack.append('_')

   return k, stack

# 번역 에러: 뒤에 _을 남기는 것이 아니다.
# nums를 조작해야 하기 때문에 다시 접근을 한다.
# nums에 중복되는 값을 지워준다. (count함수 사용)


# 문제풀이(2)
def solution(nums):
   
   for i in nums:
      # 현재 값이 1보다 크다면 중복되는 값이기 때문에 remove해준다.
      while nums.count(i) > 1:
         nums.remove(i)

   return len(nums)

print(solution([1,1,2]))                  # 2, nums = [1,2,_]
print(solution([0,0,1,1,1,2,2,3,3,4]))    # 5, nums = [0,1,2,3,4,_,_,_,_, _]