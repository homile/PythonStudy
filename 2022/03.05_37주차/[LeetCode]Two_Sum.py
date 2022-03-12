# Two Sum
# 링크: https://leetcode.com/problems/two-sum/

# [문제]
# 정수 배열과 정수가 주어지면 nums 두 숫자의 인덱스를 target 반환 하여 합이 target

# 각 입력에 정확히 하나의 솔루션 이 있다고 가정 하고 
# 동일한 요소를 두 번 사용하지 않을 수 있습니다 .

# 어떤 순서로든 답변을 반환할 수 있습니다.

# [문제접근]
# 정수형 배열에 있는 값을 더하여 target 값이 될 경우
# 해당 정수가 들어 있는 배열의 인덱스 번호를 반환한다.

# 문제풀이(1)
def solution(nums, target):
   
   for i in range(len(nums)):
      for j in range(i+1, len(nums)):
         if nums[i] + nums[j] == target:
            return [i, j]


print(solution([2, 7, 11, 15], 9))  # [0, 1]
print(solution([3, 2, 4], 6))       # [1, 2]
print(solution([3, 3], 6))          # [0, 1]