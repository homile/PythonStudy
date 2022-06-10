# Plus One
# 링크: https://leetcode.com/problems/plus-one/

# 문제풀이(1)
# 통과하긴 했는 데 먼가 쉽게 map써서 풀 수 있을듯?
def solution(digits):
  answer = ''

  for i in digits:
    answer += str(i)
  answer = str(int(answer) + 1)

  result = []

  for i in answer:
    result.append(int(i))

  return result



# 문제풀이(2)
def solution(digits):
  # str으로 한번 쪼개고 붙여준다음 정수로 변경
  answer = int(''.join(map(str, digits)))
  answer += 1

  result = []
  for i in str(answer):
    result.append(int(i))

  return result

print(solution([1,2,3]))