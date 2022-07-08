# Remove Duplicates from Sorted List
# 링크: https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# 문제풀이(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # head에 배열 담겨 있음
    cur = head
    # cur = [1, 1, 2]
    # cur.next = [1, 2]
    # cur.next.next = [2]
    # cur.next.next.next = []
    
    # cur.val = 1
    # cur.next.val = 1
    # cur.next.next.val = 2
    # cur.next.next = [2]
    # cur.next = [1,2] -> [2]
    # head = [1, 2]
    
    while cur:
      # cur의 next값이 있고 현재값이 다음 값과 같을 때 밀어내기
      if cur.next and cur.val == cur.next.val:
        cur.next = cur.next.next
      else:
        cur = cur.next
    
    return head