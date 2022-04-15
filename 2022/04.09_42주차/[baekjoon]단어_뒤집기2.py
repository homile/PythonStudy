# 단어 뒤집기2(17413번)
# 링크: https://www.acmicpc.net/problem/17413

# 문제풀이(1)
# import sys

# input_str = sys.stdin.readline()
# stack = []
# sum_str = ''
# answer = ''

# for i in range(len(input_str)):
#    if input_str[i] == '<' or '<' in stack:
#       stack.append(input_str[i])
#       if input_str[i] == '>':
#          print(stack[::-1])
#          answer += ''.join(list(reversed(sum_str)))
#          sum_str = ''
#          stack = []
#    elif input_str[i] == ' ' or i == len(input_str)-1:
#       answer += ''.join(list(reversed(sum_str))) + ' '
#       sum_str = ''
#    else:
#       sum_str += input_str[i]


# print(answer[:-1])

# TC1은 완성 <>를 판별해줘야 함.
# 는 자꾸 <>안을 거꾸로 뒤집어야한다고 착각함.
# 쉽게 풀릴수 있는 문제


# 문제풀이(2)
import sys

input_str = sys.stdin.readline()
stack = []
sum_str = ''
answer = ''

for i in range(len(input_str)):
   if input_str[i] == '<' or '<' in stack:
      stack.append(input_str[i])
      if input_str[i] == '>':
         answer += ''.join(list(reversed(sum_str)))
         sum_str = ''
         answer += ''.join(stack)
         stack = []
   elif input_str[i] == ' ' or i == len(input_str)-1:
      answer += ''.join(list(reversed(sum_str))) + ' '
      sum_str = ''
   else:
      sum_str += input_str[i]


print(answer[:-1])


# baekjoon online judge
# <open>tag<close>
# <int><max>2147483647<long long><max>9223372036854775807