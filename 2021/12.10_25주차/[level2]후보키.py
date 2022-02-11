# 후보키

# 문제설명: https://programmers.co.kr/learn/courses/30/lessons/42890
# 모든 인적사항을 DB에 넣고, 이를 위해 정리를 하던중 후보키에 대한 고민

# 관계 데이터베이스에서 릴레이션(Relation)의 튜플(Tuple)을 유일하게 식별할 수 있는 
# 속성(Attribute) 또는 속성의 집합 중, 
# 다음 두 성질을 만족하는 것을 후보 키(Candidate Key)라고 한다.

# 유일성(uniqueness) : 릴레이션에 있는 모든 튜플에 대해 유일하게 식별되어야 한다.

# 최소성(minimality) : 유일성을 가진 키를 구성하는 속성(Attribute) 중 하나라도 
# 제외하는 경우 유일성이 깨지는 것을 의미한다. 
# 즉, 릴레이션의 모든 튜플을 유일하게 식별하는 데 꼭 필요한 속성들로만 구성되어야 한다.

# 문제접근
# 유일한 데이터인 학번 = 후보키
# 이름 = 후보키X
# [이름,전공] = 후보키
# [이름,전공,학년] = 후보키X (최소성X)

# 1. 전체적인 조합을 구한다. combinations사용
# 2. 유일성을 구한다.
# 3. 2번의 값을 참고하여 최소성을 구한다.

# 참고자료 : https://youtu.be/7f1yXtfbWKY

# 문제풀이(1)
from itertools import combinations
def solution(relation):
    row = len(relation)
    col = len(relation[0])

    # print(row, col)
    # 전체적인 값을 가지고 조합을 만든다.
    combi = []
    for i in range(1, col+1):
        combi.extend(combinations(range(col),i))
    print(combi)

    # 유일성
    unique = []
    # a_list = []
    for i in combi:
        tmp = [tuple([item[key] for key in i]) for item in relation]

        # tmp 한줄 풀어봄
        # for item in relation:
        #     for key in i:
        #         ams = tuple([item[key]])
        #         a_list.append(ams)
        #     print(a_list)

        print(tmp)
        print('-')
        # 유일성
        if len(set(tmp)) == row:
            put = True

            # 최소성
            for x in unique:
                if set(x).issubset(set(i)): # 부분집합 : A가 B에도 속하는 집합
                    put = False
                    break

            if put: unique.append(i)

    return len(unique)
    

# 문제풀이(2)


# 2
print(solution([
    ["100","ryan","music","2"],
    ["200","apeach","math","2"],
    ["300","tube","computer","3"],
    ["400","con","computer","4"],
    ["500","muzi","music","3"],
    ["600","apeach","music","2"]]))