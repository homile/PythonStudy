# Merge Sorted Array
# 링크: https://leetcode.com/problems/merge-sorted-array/

# 문제풀이(1)   # 실패
# m, n을 생각하지 못했다.
# nums1의 m만큼 뒤부터 num2를 합쳐줘야한다.
# def solution(nums1, m, nums2, n):
#   nums1 += nums2

#   while 0 in nums1:
#     nums1.remove(0)
    
#   nums1.sort()

# [1,2,2,3,5,6]
# print(solution([1,2,3,0,0,0], 3, [2,5,6], 3))


# 문제풀이(2)
def solution(nums1, m, nums2, n):
  for i in range(m , m+n):
    nums1[i] = nums2[i-m]

  nums1.sort()

# [1,2,2,3,5,6]
print(solution([1,2,3,0,0,0], 3, [2,5,6], 3))