# Merge Two Sorted Lists

# 링크: https://leetcode.com/problems/merge-two-sorted-lists/

# [문제접근]
# 간단하게 생각하자면 list1과 list2의 값을 하나씩 쌓아 가는 방법이다.
# 하지만 singly-linked list 형식으로 풀어내야 한다.

# 문제풀이(1)     # 당연히 안되겠지?
# def solution(list1, list2):
#    stack = []

#    if len(list1) != 0:
#       for i in range(len(list1)):
#          stack.append(list1[i])
#          stack.append(list2[i])
#    else:
#       for i in range(len(list2)):
#          stack.append(list2[i])

#    return stack

# print(solution([1,2,4], [1,3,4]))      # [1,1,2,3,4,4]
# print(solution([], []))                # []   
# print(solution([], [0]))               # [0]


# 문제풀이(2)
# Definition for singly-linked list.
class ListNode:
   def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

class Solution:
   def solution(self, l1: ListNode, l2: ListNode) -> ListNode:

      l1_number = ''
      while l1 != None:
         l1_number += str(l1.val)
         l1 = l1.next

      print(l1_number)

      l2_number = ''
      while l2 != None:
         l2_number += str(l2.val)
         l2 = l2.next

      print(l2_number)

      answer = []
      if len(l1_number):
         for i in range(len(l1_number)):
            answer.append(int(l1_number[i]))
            answer.append(int(l2_number[i]))
      else:
         for i in range(len(l2_number)):
            answer.append(int(l2_number[i]))

      print(answer)   

      result = ListNode(answer[0], None) 

      for i in range(1, len(answer)):
         temp = ListNode(result, answer[i])
         result = temp

      return result



# 문제풀이(3)
# Definition for singly-linked list.
class ListNode:
   def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

class Solution:
   def solution(self, l1: ListNode, l2: ListNode) -> ListNode:

      head = ListNode(-1)
      cur = head

      while l1 != None and l2 != None:
         print("list1.val", l1.val)
         print("list2.val", l2.val)
         if l1.val <= l2.val:
            cur.next = l1
            l1 = l1.next
         else:
            cur.next = l2
            l2 = l2.next
         
         cur = cur.next

      print(cur)
      if l1 != None:
         cur.next = l1
      else:
         cur.next = l2

      print("head", head.next.__dict__)
      return head.next

# 직관 적으로 ListNode 넣고 보기
# input1 = ListNode(1)
# input1.next = ListNode(2)
# input1.next.next = ListNode(4)

# input2 = ListNode(1)
# input2.next = ListNode(3)
# input2.next.next = ListNode(4)

# result = Solution.solution(1, input1, input2)


# ListNode 간편하게 값 넣고 보기
print(Solution().solution(ListNode([1,2,4]), ListNode([1,3,4])).__dict__['next'].__dict__)



# https://velog.io/@kgh732/Python-으로-푸는-Leetcode21.-Merge-Two-Sorted-Lists