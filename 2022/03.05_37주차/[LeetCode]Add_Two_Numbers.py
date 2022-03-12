# Add Two Numbers
# 링크: https://leetcode.com/problems/add-two-numbers/

# [문제]
# 두 개의 음이 아닌 정수를 나타내는 두 개의 비어 있지 않은 연결 목록이 제공됩니다. 
# 숫자는 역순 으로 저장 되며 각 노드에는 단일 숫자가 포함됩니다. 
# 두 숫자를 더하고 합을 연결 목록으로 반환합니다.

# 두 숫자에 숫자 0 자체를 제외하고는 선행 0이 포함되어 있지 않다고 가정할 수 있습니다.

# [문제접근]
# 주어진 정수형 리스트 2개를 뒤집에서 더한 뒤 나온 결과값을
# 다시 뒤집어서 정수하나씩 리스트에 넣는다.

# 문제풀이(1)
def solution(l1, l2):
   l1 = ''.join(list(map(str,reversed(l1))))
   l2 = ''.join(list(map(str,reversed(l2))))

   answer = list(map(int,reversed(str(int(l1) + int(l2)))))

   return answer

print(solution([2,4,3], [5,6,4]))   # Explanation: 342 + 465 = 807 [7,0,8]
print(solution([0], [0]))           # [0]

# ListNode라는 것을 해명해


# 문제풀이(2)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def solution(self, l1: ListNode, l2: ListNode) -> ListNode:
         # ListNode에 담겨있는 값을 빼오기 위함
         l1_str = ''
         while l1 != None:
            l1_str = str(l1.val) + l1_str
            l1 = l1.next
         
         l2_str = ''
         while l2 != None:
            l2_str = str(l2.val) + l2_str
            l2 = l2.next

         result = list(str(int(l1_str) + int(l2_str)))
         print(result)

         # ListNode(val, next)로 마지막번째 값을 미리 지정
         answer = ListNode(result[0], None)
         print(answer)

         # 남은 값을 ListNode에 지정
         for i in range(1, len(result)):
            temp = ListNode(result[i], answer)
            answer = temp

         return answer


input1 = ListNode(2)
input1.next = ListNode(4)
input1.next.next = ListNode(3)

input2 = ListNode(5)
input2.next = ListNode(6)
input2.next.next = ListNode(4)

result = Solution.solution(1, input1, input2)

# print(Solution.solution(1, [2,4,3], [5,6,4]))   # Explanation: 342 + 465 = 807 [7,0,8]
# print(Solution.solution(2, [0], [0]))           # [0]

# 참고자료
# https://donghak-dev.tistory.com/119
# https://youtu.be/7TUvhk3IiOM