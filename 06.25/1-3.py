answer = []
n_answer = []

strings = ["sun", "bed", "car"]

n = 1

for i in strings:
    i = i[n]+i
    print(i)
    n_answer.append(i)
    print(n_answer)
    n_answer.sort()

for i in n_answer:
    i=i[1:]
    answer.append(i)
        

print(answer)
    
