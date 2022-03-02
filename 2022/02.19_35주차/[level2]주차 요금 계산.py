# 주차 요금 계산

# 링크: https://programmers.co.kr/learn/courses/30/lessons/92341

# [문제 설명]
# 주차장의 요금표와 차량이 들어오고(입차) 나간(출차) 기록이 주어졌을 때, 
# 차량별로 주차 요금을 계산하려고 합니다. 아래는 하나의 예시를 나타냅니다.

# 요금표
# 기본 시간(분)	기본 요금(원)	단위 시간(분)	단위 요금(원)
#     180	      5000	          10	          600

# 입/출차 기록
# 시각(시:분)	차량 번호	내역
#    05:34	      5961	   입차
#    06:00	      0000	   입차
#    06:34	      0000	   출차
#    07:59	      5961	   출차
#    07:59	      0148	   입차
#    18:59	      0000	   입차
#    19:09	      0148	   출차
#    22:59	      5961	   입차
#    23:00	      5961	   출차

# 자동차별 주차 요금
# 차량 번호	    누적 주차 시간(분)	    주차 요금(원)
#   0000	    34 + 300 = 334	      5000 + ⌈(334 - 180) / 10⌉ x 600 = 14600
#   0148	        670	              5000 +⌈(670 - 180) / 10⌉x 600 = 34400
#   5961	    145 + 1 = 146	      5000
# 어떤 차량이 입차된 후에 출차된 내역이 없다면, 23:59에 출차된 것으로 간주합니다.
# 0000번 차량은 18:59에 입차된 이후, 출차된 내역이 없습니다. 
# 따라서, 23:59에 출차된 것으로 간주합니다.
# 00:00부터 23:59까지의 입/출차 내역을 바탕으로 차량별 누적 주차 시간을 계산하여 
# 요금을 일괄로 정산합니다.
# 누적 주차 시간이 기본 시간이하라면, 기본 요금을 청구합니다.
# 누적 주차 시간이 기본 시간을 초과하면, 기본 요금에 더해서, 
# 초과한 시간에 대해서 단위 시간 마다 단위 요금을 청구합니다.
# 초과한 시간이 단위 시간으로 나누어 떨어지지 않으면, 올림합니다.
# ⌈a⌉ : a보다 작지 않은 최소의 정수를 의미합니다. 즉, 올림을 의미합니다.
# 주차 요금을 나타내는 정수 배열 fees, 자동차의 입/출차 내역을 나타내는 문자열 배열 
# records가 매개변수로 주어집니다. 
# 차량 번호가 작은 자동차부터 청구할 주차 요금을 차례대로 정수 배열에 담아서 
# return 하도록 solution 함수를 완성해주세요.

# [제한사항]
# fees의 길이 = 4

# fees[0] = 기본 시간(분)
# 1 ≤ fees[0] ≤ 1,439
# fees[1] = 기본 요금(원)
# 0 ≤ fees[1] ≤ 100,000
# fees[2] = 단위 시간(분)
# 1 ≤ fees[2] ≤ 1,439
# fees[3] = 단위 요금(원)
# 1 ≤ fees[3] ≤ 10,000
# 1 ≤ records의 길이 ≤ 1,000

# records의 각 원소는 "시각 차량번호 내역" 형식의 문자열입니다.
# 시각, 차량번호, 내역은 하나의 공백으로 구분되어 있습니다.
# 시각은 차량이 입차되거나 출차된 시각을 나타내며, HH:MM 형식의 길이 5인 문자열입니다.
# HH:MM은 00:00부터 23:59까지 주어집니다.
# 잘못된 시각("25:22", "09:65" 등)은 입력으로 주어지지 않습니다.
# 차량번호는 자동차를 구분하기 위한, `0'~'9'로 구성된 길이 4인 문자열입니다.
# 내역은 길이 2 또는 3인 문자열로, IN 또는 OUT입니다. IN은 입차를, 
# OUT은 출차를 의미합니다.
# records의 원소들은 시각을 기준으로 오름차순으로 정렬되어 주어집니다.
# records는 하루 동안의 입/출차된 기록만 담고 있으며, 
# 입차된 차량이 다음날 출차되는 경우는 입력으로 주어지지 않습니다.
# 같은 시각에, 같은 차량번호의 내역이 2번 이상 나타내지 않습니다.
# 마지막 시각(23:59)에 입차되는 경우는 입력으로 주어지지 않습니다.
# 아래의 예를 포함하여, 잘못된 입력은 주어지지 않습니다.
# 주차장에 없는 차량이 출차되는 경우
# 주차장에 이미 있는 차량(차량번호가 같은 차량)이 다시 입차되는 경우

# [문제접근]
# fees[0] = 기본시간, fees[1] = 기본요금
# fees[2] = 단위시간, fees[3] = 단위요금
# 기본 시간 동안은 기본요금만 부여되고 기본시간 초과후 단위시간당 요금이 부여된다.
# 입차 후 출차 내역이 없다면 23:59에 출차된 것으로 간주한다.
# 23:59 -> 1,439분

# 입,출차 시간을 분으로 변경하여 비교하기 편하게 한다.
# records의 내역을 공백을 기준으로 나눠 2차원 배열을 생성한다.

# 문제풀이(1)
def solution(fees, records):
    answer = []
    re_list = []
    dic = {}

    # 입차는 했지만 출차를 안한경우 시간계산
    last_time = 23 * 60 + 59

    # 차량의 입,출차 시간 및 넘버, 내역을 구분하기 편하게 변경
    # re_list[0] - 입,출차 시간, re_list[1] - 차량 번호, re_list[2] - 입,출차 내역
    for i in range(len(records)):
        re = records[i].split()
        re_list.append(re)

    # 입,출차 시간을 분으로 변경 후 총 누적 시간 계산
    for i in range(len(re_list)):
        re_list[i][0] = int(re_list[i][0][:2]) * 60 + int(re_list[i][0][3:])
        # 입,출차했던 기록이 있다면(in이라면) 다음에 값을 추가한다.
        if re_list[i][1] in dic:
            dic[re_list[i][1]].append([re_list[i][0], re_list[i][2]])
        # 입차하지 않은 차라면 값을 설정한다.
        else:
            dic[re_list[i][1]] = [re_list[i][0], re_list[i][2]]
        
    # print(re_list)
    print(dic.items())

    return answer

# 시간을 분으로 계산하고 입출차 내역을 한 딕셔너리에 모아 넣었는데
# 이제 가장 중요한 in out 시간을 구하고 요금을 정산하는 일이 남았다.
# 는 fees 배열 사용안했음 


# 문제풀이(2)    # 실패
def solution(fees, records):
    answer = []
    re_list = []
    dic = {}

    # 입차는 했지만 출차를 안한경우 시간계산
    last_time = 23 * 60 + 59

    # 차량의 입,출차 시간 및 넘버, 내역을 구분하기 편하게 변경
    # re_list[0] - 입,출차 시간, re_list[1] - 차량 번호, re_list[2] - 입,출차 내역
    for i in range(len(records)):
        re = records[i].split()
        re_list.append(re)

    # 입,출차 시간을 분으로 변경 후 총 누적 시간 계산
    for i in range(len(re_list)):
        re_list[i][0] = int(re_list[i][0][:2]) * 60 + int(re_list[i][0][3:])
        # 입,출차했던 기록이 있다면(in이라면) 다음에 값을 추가한다.
        if re_list[i][1] in dic:
            dic[re_list[i][1]].append([re_list[i][0], re_list[i][2]])
        # 입차하지 않은 차라면 값을 설정한다.
        else:
            dic[re_list[i][1]] = [[re_list[i][0], re_list[i][2]]]
        
    # print(re_list)

    print(dic.items())
    # 차량 번호 순으로 나와야 하므로 정렬
    result_list = sorted(list(dic.items()))
    print(sorted(result_list))

    for i in result_list:
        time = 0
        for j in i[1]:
            if j[1] == "IN":
                time -= j[0]
            else:
                time += j[0]

        if i[1][-1][1] == "IN":
            time += last_time

        if time <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(int(fees[1]+((time-fees[0])/fees[2]*fees[3])))
        print(i[0], time)


    return answer

# 계산과정에서 반올림을 하지않아 14600이나와야 하는데 14240이 나옴
# Math 라이브러리에 ceil함수를 사용하면됨


# 문제풀이(3)
import math
def solution(fees, records):
    answer = []
    re_list = []
    dic = {}

    # 입차는 했지만 출차를 안한경우 시간계산
    last_time = 23 * 60 + 59

    # 차량의 입,출차 시간 및 넘버, 내역을 구분하기 편하게 변경
    # re_list[0] - 입,출차 시간, re_list[1] - 차량 번호, re_list[2] - 입,출차 내역
    for i in range(len(records)):
        re = records[i].split()
        re_list.append(re)

    # 입,출차 시간을 분으로 변경 후 총 누적 시간 계산
    for i in range(len(re_list)):
        re_list[i][0] = int(re_list[i][0][:2]) * 60 + int(re_list[i][0][3:])
        # 입,출차했던 기록이 있다면(in이라면) 다음에 값을 추가한다.
        if re_list[i][1] in dic:
            dic[re_list[i][1]].append([re_list[i][0], re_list[i][2]])
        # 입차하지 않은 차라면 값을 설정한다.
        else:
            dic[re_list[i][1]] = [[re_list[i][0], re_list[i][2]]]
        
    # print(re_list)

    print(dic.items())
    # 차량 번호 순으로 나와야 하므로 정렬
    result_list = sorted(list(dic.items()))
    print(sorted(result_list))

    for i in result_list:
        time = 0
        for j in i[1]:
            if j[1] == "IN":
                time -= j[0]
            else:
                time += j[0]

        # 마지막 기록인 IN일 경우
        if i[1][-1][1] == "IN":
            time += last_time

        if time <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(int(fees[1]+(math.ceil((time-fees[0])/fees[2])*fees[3])))
        print(i[0], time)

    return answer


# 문제풀이(4)
import math
def solution(fees, records):
    answer = []
    re_list = []
    dic = {}

    # 입차는 했지만 출차를 안한경우 시간계산
    last_time = 23 * 60 + 59

    # 차량의 입,출차 시간 및 넘버, 내역을 구분하기 편하게 변경
    for i in range(len(records)):
        re = records[i].split()
        re_list.append(re)

    # 입,출차 시간을 분으로 변경 후 총 누적 시간 계산
    for i in range(len(re_list)):
        re_list[i][0] = int(re_list[i][0][:2]) * 60 + int(re_list[i][0][3:])
        # 입,출차했던 기록이 있다면(in이라면) 다음에 값을 추가한다.
        if re_list[i][1] in dic:
            dic[re_list[i][1]].append([re_list[i][0], re_list[i][2]])
        # 입차하지 않은 차라면 값을 설정한다.
        else:
            dic[re_list[i][1]] = [[re_list[i][0], re_list[i][2]]]
        
    # 차량 번호 순으로 나와야 하므로 정렬
    result_list = sorted(list(dic.items()))

    # BaseTime, BaseRate, UnitTime, UnitRate
    bt, br, ut, ur = fees

    for i in result_list:
        time = 0
        for j in i[1]:
            if j[1] == "IN":
                time -= j[0]
            else:
                time += j[0]

        if i[1][-1][1] == "IN":
            time += last_time

        if time <= bt:
            answer.append(br)
        else:
            answer.append(int(br+(math.ceil((time-bt)/ut)*ur)))

    return answer

# [14600, 34400, 5000]
print(solution(	[180, 5000, 10, 600], 
["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", 
"07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", 
"23:00 5961 OUT"]))

# [0, 591]
print(solution([120, 0, 60, 591], 
["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", 
"23:58 3961 IN"]))

# [14841]
print(solution(	[1, 461, 1, 10], ["00:00 1234 IN"]))