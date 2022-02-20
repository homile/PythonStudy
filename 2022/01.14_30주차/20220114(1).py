# 모음사전

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/84512
# 사전에 알파벳 모음 'A', 'E', 'I', 'O', 'U'만을 사용하여 만들 수 있는, 길이 5 이하의 모든 단어가 수록되어 있습니다. 
# 사전에서 첫 번째 단어는 "A"이고, 그다음은 "AA"이며, 마지막 단어는 "UUUUU"입니다.

# 단어 하나 word가 매개변수로 주어질 때, 이 단어가 사전에서 몇 번째 단어인지 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# word의 길이는 1 이상 5 이하입니다.
# word는 알파벳 대문자 'A', 'E', 'I', 'O', 'U'로만 이루어져 있습니다.

# 입출력 예 설명
# 입출력 예 #1
# 사전에서 첫 번째 단어는 "A"이고, 그다음은 "AA", "AAA", "AAAA", "AAAAA", "AAAAE", ... 와 같습니다. "AAAAE"는 사전에서 6번째 단어입니다.

# 입출력 예 #2
# "AAAE"는 "A", "AA", "AAA", "AAAA", "AAAAA", "AAAAE", "AAAAI", "AAAAO", "AAAAU"의 다음인 10번째 단어입니다.

# 문제접근
# combination으로 무작위로 조합한 후 찾아야 하나?
# permutation으로 순서가 있게 조합해야 하나?
# 위의 조합을 하기 위해선 A,E,I,O,U가 있는 리스트를 하나 만들어야한다.

# 문제풀이(1)
from itertools import permutations
def solution(word):
    answer = 0
    AEIOU = ['A','E','I','O','U']
    word_per = []

    for i in range(len(AEIOU)):
        word_per.append(list(permutations(AEIOU, i)))

    print(word_per)
    return answer

# 원하는 조합이 나오지 않는다. combination과 permutation은 아니다.
# 그렇다면 product?


# 문제풀이(2)
from itertools import product
def solution(word):
    answer = 0
    word_product = []

    for i in range(5):
        word_product.append(list(product("AEIOU", repeat=i+1))) # repeat = n번 반복(i+1번)

    print(word_product)
    return answer

# 원하는 조합이 전부 출력되었다.
# 하지만 리스트에 문자열이 아닌 문자로 들어있어서 이것을
# join을 사용하여 붙여주고 word가 몇번째에 있는지 찾아야 한다.
# 리스트의 번호는 0부터 시작하기 때문에 찾은 번호에 +1을 해줘야 된다.


# 문제풀이(3)
from itertools import product
def solution(word):
    answer = 0
    list1 = []

    for i in range(5):
        # word_product.append(list(product("AEIOU", repeat=i+1))) # repeat = n번 반복(i+1번)
        for j in list(product("AEIOU", repeat=i+1)):
            list1.append(''.join(j))

    # print(list1)
    list1 = sorted(list1)
    answer = list1.index(word)+1

    return answer


# 다른 사람의 풀이(1)
def solution(word):
    answer = 0
    for i, n in enumerate(word):
        answer += (5 ** (5 - i) - 1) / (5 - 1) * "AEIOU".index(n) + 1
    return answer

# 등비수열의 합을 이용한 풀이


# 다른 사람의 풀이(2)
from itertools import product

solution = lambda word: sorted(["".join(c) for i in range(5) for c in product("AEIOU", repeat=i+1)]).index(word) + 1

# 람다식을 활용한 풀이

print(solution("AAAAE"))    # 6
print(solution("AAAE"))     # 10
print(solution("I"))        # 1563
print(solution("EIO"))      # 1189