# Container With Most Water
# 링크: https://leetcode.com/problems/container-with-most-water/

# [문제접근]
# 물의 부피를 모두 한 배열에 담는다. 그 중 가장 큰 값을 찾는다.
# 왼쪽과 오른쪽 끝에서 인덱스가 시작하여 차근차근 값을 구한다.
# 높이 = 배열에 있는 값, 가로 = 왼쪽 인덱스 번호 - 오른쪽 인덱스 번호

# 문제풀이(1)
def solution(height):
   # 왼쪽 시작 인덱스부터 검증
   left = 0
   # 오른쪽 끝 인덱스부터  검증
   right = len(height) - 1

   stack = []

   for i in range(len(height)):
      if left != right:    # 이 부분을 추가하면 속도는 느려지고 정확성은 올라감
         if height[left] <= height[right]:
            print('오른쪽 큼:',height[left], height[right], left, right)
            stack.append(height[left] * (right - left))
            left += 1
         else:
            print('왼쪽 큼:',height[left], height[right], left, right)
            stack.append(height[right] * (right - left))
            right -= 1

   print(stack)

   return max(stack)

print(solution([1,8,6,2,5,4,8,3,7]))     # 49