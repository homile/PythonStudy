# 메뉴 리뉴얼

# 문제설명 : https://programmers.co.kr/learn/courses/30/lessons/72411
# 각 손님들이 주문한 단품메뉴들이 담긴 배열 = orders
# 스카피가 추가하고 싶어하는 코스 요리를 구성하는 
# 단품메뉴들의 개수가 담긴 배열 = course

# 예상풀이
# 각 손님의 구성메뉴를 combination을 통해 조합
# 조합한 것의 
# 메뉴의 구성은 2개 이상의 단품이 있어야 함.
# 원하는 단품메뉴들의 개수가 담긴만큼 조합해야함

# 문제풀이(1)
# combinations로 단품 2개씩 들어간 조합을 찾음
# 그런데 스카피가 원하는 개수는 다를 수 있음 그 배열을 사용해야함.

# from itertools import combinations
# def solution(orders, course):
#     answer = []
#     o_list = []

#     for order in orders:
#         com = combinations(order, 2)
#         o_list += com

#         print(o_list)

#     return answer


# 원하는 개수 만큼의 조합을 만들었는데
# 듀플 형식으로 리스트에 삽입됨.
# 이걸 join으로 이어 붙인 다음에 비교해야함.

# 문제풀이(2)
# from itertools import combinations
# def solution(orders, course):
#     answer = []
#     num = 0

#     for order in orders:
#         o_list = []
#         num += 1
#         for i in course:
#             com = combinations(sorted(order), i)
#             for j in com :
#                 o_str = ''.join(sorted(j))
#                 o_list.append(o_str)
#                 o_list.sort()
#         print(num)
#         print(o_list)

#     return answer


# join으로 붙였고 이제는 비교하여
# count하는것만 남음.

# 문제풀이(3)
# from itertools import combinations
# def solution(orders, course):
#     answer = []
#     o_list = []

#     for order in orders:
#         for i in course:
#             com = combinations(sorted(order), i)
#             for j in com :
#                 o_str = ''.join(sorted(j))
#                 o_list.append(o_str)
#                 o_list.sort()
#     print('--------------------')
#     print(o_list)
#     for i in course:
#         cnt = 0
#         for k in range(1, len(o_list)):
#             if len(o_list[k]) >= i and o_list[k-1] == o_list[k]:
#                 cnt += 1
#             else :
#                 cnt = 0
#             if cnt >= 1 :
#                 answer.append(o_list[k])

#     return answer


# count해서 비교하여 손님이 고른 단품메뉴의 조합이 1이상인 것을 확인함.
# 하지만 ac, ac, ad, ad, ad의 경우 ad가 선택되야하지만
# ac와 ad가 둘 다 선택되는 경우 발생
# count를 할 때 max값을 비교해줘야함?

# 문제풀이(4)
from itertools import combinations
def solution(orders, course):
    answer = []
    o_list = []

    for order in orders:
        for i in course:
            com = combinations(sorted(order), i)
            for j in com :
                o_str = ''.join(sorted(j))
                o_list.append(o_str)
                o_list.sort()
    print('--------------------')
    print(o_list)

    tmp = []
    for i in course:
        cnt = 0
        max_cnt = 0
        for k in range(1, len(o_list)):
            if len(o_list[k]) >= i and o_list[k-1] == o_list[k]:
                cnt += 1
                if cnt >= max_cnt:
                    max_cnt = cnt
                    tmp.append(o_list[k])
            else :
                cnt = 0
                
    answer = list(set(sorted(tmp, reverse=False)))

    return answer


# 가장 큰 값을 비교하는 문항을 작성하지 못함.
# 검색 결과 collections 라이브러리의 Counter를 사용하는 방안있음.
# Counter는 딕셔너리 형식으로 key, value를 사용하여 count하는 방안
# 이 메커니즘을 생각할 수 있다면 Counter함수 없이 풀이 가능할듯

# 문제풀이(5)
from itertools import combinations
from typing import Counter
def solution(orders, course):
    answer = []

    for i in course:
        temp = []
        for order in orders:
            com = combinations(sorted(order), i)
            temp += com
        counter = Counter(temp)

        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]

    return sorted(answer)



# 다른 사람의 풀이(1)
from itertools import combinations
def solution(orders, course):

    temp = dict()

    for num in course:
        temp[num] = []

    for order in orders:
        for num in course:
            if num > len(order):
                break
            else:
                temp[num] += list(combinations(sorted(list(order)),num))

    result = []
    for menus in temp.values():
        max_num = 2
        for menu in menus:
            cnt = menus.count(menu)
            if cnt>max_num:
                max_num = cnt

        for menu in menus:
            m = ''.join(menu)
            if max_num == menus.count(menu) and m not in result:
                result.append(m)

    return sorted(result)

# ["AC", "ACDE", "BCFG", "CDE"]
print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
# ["ACD", "AD", "ADE", "CD", "XYZ"]
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
# ["WX", "XY"]
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))