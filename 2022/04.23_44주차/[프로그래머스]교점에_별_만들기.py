# 교점에 별 만들기
# 링크: https://programmers.co.kr/learn/courses/30/lessons/87377

# [문제접근]
# 그래프를 그려서 거기에 만나는 교점에 별을 찍어준다는 것 까지는 이해를 했다.
# 하지만 어떻게?가 머리에서 나오지 않는다.
# 일단 주어진 식 Ax + By + c = 0으로 직선을 표현할 수 있다고 한다.

# 다른 사람 문제풀이(1)
# https://youngyin.tistory.com/145
def solution(line):
    # 교점구하기
    nodeList = []
    for i in range(len(line)) : 
        a, b, e = line[i]
        
        for c, d, f in line[i+1:] : 
            if a*d-b*c==0 : continue
            x = (b*f-e*d)/(a*d-b*c)
            y = (e*c-a*f)/(a*d-b*c)
            print(x, y)
            
            if int(x)==x and int(y)==y and (x, y) not in nodeList: 
                nodeList.append((int(x), int(y)))
                print(nodeList)
    
    # 교점의 가장 큰/작은 값 구하기
    nodeList.sort(key = lambda x : x[0])
    minx, maxx = nodeList[0][0], nodeList[-1][0]
    nodeList.sort(key = lambda x : x[1])
    miny, maxy = nodeList[0][1], nodeList[-1][1]
    
    # 배열에 별 그리기
    arr = [["."for j in range(maxx-minx+1)] for i in range(maxy-miny+1)]
    for x, y in nodeList : 
        r, c = y-miny, x-minx
        arr[r][c] = "*"
        
    return ["".join(item) for item in arr][::-1] # r방향이 좌표와 반대이므로 뒤집어서 출력


print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
# ["....*....", 
#  ".........", 
#  ".........", 
#  "*.......*", 
#  ".........", 
#  ".........",
#  ".........", 
#  ".........", 
#  "*.......*"]
