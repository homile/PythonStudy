def solution(s):
    answer = s
    num_s = 'zero one two three four five six seven eight nine'
    num = [0,1,2,3,4,5,6,7,8,9]
    numbers = dict(zip(num_s.split(),num))
    for k,i in numbers.items():
        answer = s.replace(k, str(i))

    print(numbers)
    return answer

print(solution("one4seveneight"))